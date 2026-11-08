import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from skillforge import collect, read_skill, render_catalog


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def make_skill(self, category, folder, text):
        directory = self.root / "skills" / category / folder
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(text, encoding="utf-8")
        return directory / "SKILL.md"

    def test_valid_block_description_and_catalog_link(self):
        path = self.make_skill("pesquisa", "buscar", "---\nname: buscar\ndescription: >-\n  Encontra fontes.\n  Use para pesquisar.\n---\n\nBusque fontes.\n")
        skill = read_skill(path, self.root)
        self.assertEqual(skill.description, "Encontra fontes. Use para pesquisar.")
        self.assertIn("[buscar](skills/pesquisa/buscar/SKILL.md)", render_catalog([skill], self.root))

    def test_invalid_yaml_and_name_mismatch(self):
        bad = self.make_skill("meta", "broken", "---\nname: [\ndescription: x\n---\nbody\n")
        with self.assertRaisesRegex(ValueError, "YAML inválido"):
            read_skill(bad, self.root)
        bad.write_text("---\nname: outro\ndescription: x\n---\nbody\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "não corresponde"):
            read_skill(bad, self.root)

    def test_duplicate_names_and_missing_skill(self):
        text = "---\nname: repetida\ndescription: Uma descrição.\n---\nInstrução.\n"
        self.make_skill("a", "repetida", text)
        self.make_skill("b", "repetida", text)
        (self.root / "skills" / "c" / "ausente").mkdir(parents=True)
        _, errors = collect(self.root)
        self.assertTrue(any("nome duplicado" in item for item in errors))
        self.assertTrue(any("SKILL.md ausente" in item for item in errors))

    def test_catalog_is_sorted_and_escapes_table_pipes(self):
        self.make_skill("meta", "zeta", "---\nname: zeta\ndescription: 'A | B'\n---\nCorpo.\n")
        self.make_skill("meta", "alfa", "---\nname: alfa\ndescription: Primeiro.\n---\nCorpo.\n")
        skills, errors = collect(self.root)
        self.assertFalse(errors)
        result = render_catalog(skills, self.root)
        self.assertLess(result.index("[alfa]"), result.index("[zeta]"))
        self.assertIn(r"A \| B", result)


if __name__ == "__main__":
    unittest.main()
