#!/usr/bin/env python3
"""Atualiza o catálogo ou confere se ele está atualizado, com --check."""
import argparse
from skillforge import ROOT, collect, render_catalog

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true", help="confere sem modificar o catálogo")
args = parser.parse_args()
skills, errors = collect(ROOT)
if errors or not skills:
    for error in errors:
        print(f"ERRO: {error}")
    if not skills:
        print("ERRO: nenhuma skill encontrada")
    raise SystemExit(1)
destination = ROOT / "CATALOGO.md"
content = render_catalog(skills, ROOT)
if args.check:
    if not destination.exists() or destination.read_text(encoding="utf-8") != content:
        print("Catálogo desatualizado; execute python scripts/generate-index.py")
        raise SystemExit(1)
    print(f"Catálogo atualizado: {len(skills)} skills.")
else:
    destination.write_text(content, encoding="utf-8")
    print(f"Catálogo gerado: {len(skills)} skills.")
