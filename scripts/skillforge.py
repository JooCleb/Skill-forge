"""Leitura e verificação compartilhadas pelas ferramentas do repositório."""

from dataclasses import dataclass
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


@dataclass(frozen=True)
class Skill:
    name: str
    description: str
    path: Path
    category: str


def read_skill(path: Path, root: Path) -> Skill:
    """Lê YAML e confere regras básicas; não avalia comportamento."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"não foi possível ler o arquivo: {exc}") from exc
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("o frontmatter YAML deve começar com ---")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("falta o delimitador final do frontmatter") from exc
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML inválido: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("o frontmatter deve ser um mapa YAML")
    name, description = data.get("name"), data.get("description")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        raise ValueError("name deve ter até 64 caracteres, em minúsculas, números e hífens")
    if name != path.parent.name:
        raise ValueError(f"name {name!r} não corresponde à pasta {path.parent.name!r}")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("description deve ser texto não vazio com até 1024 caracteres")
    if not "\n".join(lines[end + 1:]).strip():
        raise ValueError("o corpo de instruções está vazio")
    try:
        category = path.relative_to(root / "skills").parts[0]
    except (ValueError, IndexError) as exc:
        raise ValueError("skill fora da pasta skills") from exc
    return Skill(name, description.strip(), path, category)


def collect(root: Path = ROOT):
    """Retorna (skills, problemas), incluindo nomes duplicados e pastas incompletas."""
    folder = root / "skills"
    if not folder.is_dir():
        return [], [f"{folder}: pasta de skills ausente"]
    skills, errors, seen = [], [], {}
    for category in sorted(p for p in folder.iterdir() if p.is_dir() and not p.name.startswith(".")):
        for directory in sorted(p for p in category.iterdir() if p.is_dir() and not p.name.startswith(".")):
            path = directory / "SKILL.md"
            if not path.is_file():
                errors.append(f"{directory.relative_to(root)}: SKILL.md ausente")
                continue
            try:
                skill = read_skill(path, root)
            except ValueError as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
                continue
            if skill.name in seen:
                errors.append(f"nome duplicado {skill.name!r}: {seen[skill.name]} e {path.relative_to(root)}")
            else:
                seen[skill.name] = path.relative_to(root)
            agents = directory / "agents" / "openai.yaml"
            if agents.exists():
                try:
                    parsed = yaml.safe_load(agents.read_text(encoding="utf-8"))
                    if not isinstance(parsed, dict):
                        raise ValueError("o arquivo deve conter um mapa YAML")
                except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
                    errors.append(f"{agents.relative_to(root)}: {exc}")
            skills.append(skill)
    return skills, errors


def render_catalog(skills, root: Path = ROOT) -> str:
    lines = [
        "# Catálogo de skills", "",
        "Gerado a partir de `name` e `description` dos arquivos `SKILL.md`. ",
        "A classificação por área ajuda na navegação e não indica maturidade nem testes concluídos.",
        "", f"Total: **{len(skills)} skills**.", "",
        "Atualize com `python scripts/generate-index.py`.", "",
    ]
    for category in sorted({skill.category for skill in skills}):
        members = sorted((s for s in skills if s.category == category), key=lambda s: s.name)
        lines += [f"## {category.capitalize()} ({len(members)})", "", "| Skill | Descrição |", "| --- | --- |"]
        for skill in members:
            # A descrição integral continua no arquivo; aqui apenas facilitamos a busca.
            excerpt = re.split(r"(?<=[.!?])\s+", " ".join(skill.description.split()), maxsplit=1)[0]
            excerpt = excerpt.replace("|", "\\|")
            lines.append(f"| [{skill.name}]({skill.path.relative_to(root).as_posix()}) | {excerpt} |")
        lines.append("")
    return "\n".join(lines)
