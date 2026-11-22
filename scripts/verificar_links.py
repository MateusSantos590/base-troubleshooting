#!/usr/bin/env python3
"""Verifica a integridade da documentação.

O que é conferido:
  1. Links internos: o arquivo de destino existe?
  2. Âncoras (#secao): o título ou <a id="..."> existe no arquivo de destino?
  3. Links de referência ([texto][ref]): a referência [ref]: foi definida?
  4. Guias: cada arquivo em guias/ tem todas as seções obrigatórias do molde?

Links externos (http/https) não são acessados: sites mudam e bloqueiam robôs,
o que tornaria a verificação instável.

Uso:
    python3 scripts/verificar_links.py

Sai com código 0 se estiver tudo certo e 1 se encontrar algum problema.
Usa apenas a biblioteca padrão do Python 3.8+.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parent.parent

SECOES_OBRIGATORIAS = [
    "Entenda o problema",
    "Pergunte primeiro",
    "Antes de começar",
    "Passo a passo",
    "Como interpretar o resultado",
    "Como saber que resolveu",
    "O que anotar no chamado",
    "Quando encaminhar ao N2",
    "Erros comuns",
]

RE_CERCA = re.compile(r"^(```|~~~)")
RE_TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_ANCORA_HTML = re.compile(r"""<a\s+(?:id|name)=["']([^"']+)["']""")
RE_LINK_INLINE = re.compile(r"(?<!!)\[(?:[^\]\[]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_IMAGEM = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
RE_LINK_REF = re.compile(r"\[([^\]]+)\]\[([^\]]*)\]")
RE_DEF_REF = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(\S+)")
RE_CODIGO_INLINE = re.compile(r"`[^`]*`")


def linhas_fora_de_codigo(texto: str):
    """Gera (número, linha) ignorando blocos de código cercados."""
    dentro = False
    for numero, linha in enumerate(texto.splitlines(), start=1):
        if RE_CERCA.match(linha.strip()):
            dentro = not dentro
            continue
        if not dentro:
            yield numero, linha


def slug_github(titulo: str) -> str:
    """Reproduz como o GitHub transforma um título em âncora."""
    texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", titulo)  # [texto](url) -> texto
    texto = re.sub(r"<[^>]+>", "", texto)  # remove tags HTML
    texto = texto.lower()
    texto = re.sub(r"[^\w\- ]", "", texto)  # mantém letras, números, _, - e espaço
    return texto.replace(" ", "-")


def ancoras_do_arquivo(caminho: Path) -> set[str]:
    ancoras: set[str] = set()
    contagem: dict[str, int] = {}
    texto = caminho.read_text(encoding="utf-8")
    for _, linha in linhas_fora_de_codigo(texto):
        for ancora in RE_ANCORA_HTML.findall(linha):
            ancoras.add(ancora)
        titulo = RE_TITULO.match(linha)
        if titulo:
            base = slug_github(titulo.group(2))
            n = contagem.get(base, 0)
            ancoras.add(base if n == 0 else f"{base}-{n}")
            contagem[base] = n + 1
    return ancoras


def verificar_arquivo(arquivo: Path, cache: dict[Path, set[str]]) -> list[str]:
    erros: list[str] = []
    texto = arquivo.read_text(encoding="utf-8")
    relativo = arquivo.relative_to(RAIZ)

    definicoes = {
        m.group(1).lower()
        for _, linha in linhas_fora_de_codigo(texto)
        if (m := RE_DEF_REF.match(linha))
    }

    for numero, linha in linhas_fora_de_codigo(texto):
        if RE_DEF_REF.match(linha):
            continue
        sem_codigo = RE_CODIGO_INLINE.sub("", linha)

        for texto_link, ref in RE_LINK_REF.findall(sem_codigo):
            chave = (ref or texto_link).lower()
            if chave not in definicoes:
                erros.append(f"{relativo}:{numero}: referência [{chave}] não definida")

        alvos = RE_LINK_INLINE.findall(sem_codigo) + RE_IMAGEM.findall(sem_codigo)
        alvos += [m.group(1) for m in re.finditer(r'href="([^"]+)"', sem_codigo)]
        for alvo in alvos:
            if re.match(r"^(https?:|mailto:)", alvo):
                continue
            caminho_str, _, ancora = alvo.partition("#")
            destino = (arquivo.parent / unquote(caminho_str)).resolve() if caminho_str else arquivo
            if not destino.exists():
                erros.append(f"{relativo}:{numero}: arquivo não encontrado -> {alvo}")
                continue
            if ancora and destino.suffix == ".md":
                if destino not in cache:
                    cache[destino] = ancoras_do_arquivo(destino)
                if unquote(ancora) not in cache[destino]:
                    erros.append(f"{relativo}:{numero}: âncora #{ancora} não existe em {destino.relative_to(RAIZ)}")
    return erros


def verificar_molde_dos_guias() -> list[str]:
    erros: list[str] = []
    for guia in sorted((RAIZ / "guias").glob("kb-*.md")):
        titulos = {
            m.group(2).strip()
            for _, linha in linhas_fora_de_codigo(guia.read_text(encoding="utf-8"))
            if (m := RE_TITULO.match(linha)) and len(m.group(1)) == 2
        }
        for secao in SECOES_OBRIGATORIAS:
            if secao not in titulos:
                erros.append(f"{guia.relative_to(RAIZ)}: falta a seção obrigatória '## {secao}'")
    return erros


def main() -> int:
    arquivos = sorted(p for p in RAIZ.rglob("*.md") if ".git" not in p.parts)
    cache: dict[Path, set[str]] = {}
    erros: list[str] = []
    for arquivo in arquivos:
        erros += verificar_arquivo(arquivo, cache)
    erros += verificar_molde_dos_guias()

    if erros:
        print(f"Foram encontrados {len(erros)} problema(s):\n")
        print("\n".join(f"  ✗ {e}" for e in erros))
        return 1

    total_guias = len(list((RAIZ / "guias").glob("kb-*.md")))
    print(f"✓ {len(arquivos)} arquivos verificados, {total_guias} guias no molde. Nenhum link quebrado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
