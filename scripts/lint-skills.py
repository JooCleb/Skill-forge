#!/usr/bin/env python3
"""Mostra sinais que podem merecer revisão manual, sem julgá-los como defeitos."""
from skillforge import ROOT, collect

skills, errors = collect(ROOT)
if errors:
    for error in errors:
        print(f"ERRO: {error}")
    raise SystemExit(1)
warnings = []
for skill in skills:
    if len(skill.description) > 500:
        warnings.append(f"{skill.name}: descrição tem {len(skill.description)} caracteres; avalie concisão")
    lines = len(skill.path.read_text(encoding="utf-8").splitlines())
    if lines > 500:
        warnings.append(f"{skill.name}: instruções têm {lines} linhas; avalie referências separadas")
for warning in warnings:
    print(f"AVISO: {warning}")
print(f"{len(warnings)} aviso(s) em {len(skills)} skills; avisos exigem julgamento humano.")
