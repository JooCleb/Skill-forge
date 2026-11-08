# Skill Forge

Uma biblioteca e oficina para guardar, entender, testar e evoluir skills usadas no ChatGPT Work e, quando aplicável, no Codex. As skills pessoais instaladas foram importadas com seus recursos; a importação registra uma cópia, não uma avaliação de qualidade ou uma sincronização automática.

## Comece por aqui

- [Catálogo de skills](CATALOGO.md): navegue por nome, finalidade e área.
- [Guia de criação de boas skills](docs/00-overview.md): anatomia, instruções, testes e evolução.
- [Como contribuir](CONTRIBUTING.md): procedimentos para alterações e revisão.
- [Histórico](CHANGELOG.md): mudanças registradas no repositório.

## Organização

| Pasta | Papel |
| --- | --- |
| `skills/` | Cópias das skills pessoais importadas, agrupadas em `aprendizagem`, `codigo`, `escrita`, `meta`, `pesquisa` e `produtividade`. Uma área é apenas um recurso de navegação. |
| `incubator/` | Ideias, experimentos, protótipos e candidatas em elaboração. |
| `workshop/` | Propostas de fusão, divisão, refatoração e descontinuação. |
| `docs/` | Manual de projeto e avaliação de skills. |
| `templates/` | Modelos para novas skills, testes, avaliação e decisões. |
| `evaluations/` | Casos, regressões e resultados efetivamente registrados. |
| `examples/` | Exemplos didáticos de decisões de projeto. |
| `scripts/` e `tests/` | Ferramentas de catálogo e verificações, com seus próprios testes. |

Uma skill importada não é automaticamente «estável»: para promover uma candidata, defina cenários, execute os testes relevantes e registre evidências. A classificação e o ciclo de vida estão em [docs/00-overview.md](docs/00-overview.md).

## Usar uma skill

Abra o arquivo `SKILL.md` no catálogo e leia também os recursos que ele indicar. Cada pasta é uma unidade: preserve `agents/`, `references/`, `assets/` e outros arquivos quando estiverem presentes. O ambiente precisa fornecer as ferramentas e permissões mencionadas nas instruções; um arquivo por si só não concede acesso a serviços.

**ChatGPT Work:** gerencie a instalação pelo mecanismo de skills disponível no seu ambiente. Os arquivos neste repositório são uma cópia independente: alterá-los aqui não atualiza automaticamente uma skill instalada, e alterar a instalada não atualiza este repositório.

**Codex:** para disponibilizar uma skill em um projeto local, uma opção é copiar a pasta completa para `.agents/skills/`, desde que não haja uma skill homônima. Por exemplo, a partir da raiz deste repositório:

```bash
mkdir -p .agents/skills
cp -R skills/pesquisa/deep-research .agents/skills/
```

Confirme os caminhos e as instruções vigentes do seu ambiente antes de instalar. Consulte a [documentação oficial sobre instalação](https://developers.openai.com/api/reference/cli) e a [visão geral de skills da OpenAI](https://developers.openai.com/plugins/concepts/skills).

## Criar e melhorar

1. Descreva o objetivo, quando a skill deve e não deve ser usada e qual saída ela produz.
2. Examine o [catálogo](CATALOGO.md) para evitar sobreposição desnecessária.
3. Adapte o [modelo](templates/skill/SKILL.md), mantendo nele apenas instruções e recursos necessários; o modelo é um ponto de partida, não uma skill instalada.
4. Prepare casos positivos, negativos e limites com [este modelo](templates/skill/test-cases.md). Execute-os no ambiente apropriado e registre resultados reais.
5. Compare a candidata com seus critérios de aceitação. Para fusão, divisão ou refatoração, registre a decisão e preserve um caminho de migração quando necessário.

O [manual](docs/00-overview.md) explica essas etapas. A simples validação do formato não demonstra que a skill será acionada ou produzirá boas respostas.

## Verificar e atualizar o catálogo

Requer Python 3.10+ e a dependência PyYAML. Em um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate-skills.py
python scripts/lint-skills.py
python scripts/generate-index.py
python scripts/generate-index.py --check
python -m unittest discover -s tests
```

O validador confere YAML, campos essenciais, nome, pasta, conteúdo e duplicação; o lint apresenta apenas indícios para revisão humana. Os testes automatizados cobrem as ferramentas do repositório, não o comportamento das 100 skills importadas. O fluxo de GitHub Actions executa as verificações estruturais e os testes em pushes e pull requests, quando habilitado.

## Licença

Nenhuma licença foi escolhida para este repositório. Definir uma licença exige uma decisão explícita do titular dos direitos.
