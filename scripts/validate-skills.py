#!/usr/bin/env python3
"""Verifica a estrutura e o frontmatter das skills do catálogo."""
from skillforge import ROOT, collect

skills, errors = collect(ROOT)
for error in errors:
    print(f"ERRO: {error}")
if not skills:
    print("ERRO: nenhuma skill encontrada")
    raise SystemExit(1)
if errors:
    print(f"{len(errors)} problema(s) em {len(skills)} skills legíveis.")
    raise SystemExit(1)
print(f"Estrutura e frontmatter conferidos: {len(skills)} skills.")
print("Esta verificação não executa nem comprova o comportamento das skills.")
