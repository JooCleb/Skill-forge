# Manual de engenharia de skills

Este manual trata uma skill como um pacote reutilizável para um objetivo reconhecível: uma descrição ajuda a decidir quando carregá-la, e as instruções orientam uma execução depois de escolhida. Uma skill não é um agente independente, não instala ferramentas e não amplia permissões por si só.

## Percurso de leitura

1. [Anatomia](01-anatomy-of-a-skill.md) e [princípios](02-design-principles.md).
2. [Gatilhos](03-trigger-design.md), [instruções](04-instruction-design.md) e [contexto](05-context-management.md).
3. [Composição](06-composition.md), [testes](07-testing.md) e [avaliação](08-evaluation.md).
4. [Refatoração](09-refactoring.md), [fusão e divisão](10-merging-and-splitting.md) e [antipadrões](11-anti-patterns.md).

## Ciclo de vida

| Estado | Significado | Próxima decisão |
| --- | --- | --- |
| Ideia | Objetivo ou problema identificado, sem contrato definido. | Explorar em `incubator/`. |
| Experimento / protótipo | Alternativas em construção; comportamento pode mudar. | Comparar com exemplos reais. |
| Candidata | Contrato definido e pronta para avaliação. | Executar casos e registrar evidências. |
| Avaliada / estável | Critérios definidos foram atendidos em ambiente e cenários registrados. | Usar e manter; reavaliar após mudanças relevantes. |
| Em revisão | Há proposta de refatorar, fundir ou dividir. | Comparar antes/depois e decidir migração. |
| Descontinuada | Não é mais recomendada para novos usos. | Indicar sucessora e preservar histórico conforme necessário. |

Estes estados são decisões documentadas, não inferências a partir do nome da pasta. A primeira importação reúne skills pessoais instaladas; não atribui automaticamente estado estável, versão ou testes a cada uma.

Fontes para aprofundamento: [anatomia de skills na OpenAI](https://developers.openai.com/plugins/build/skills) e [avaliação sistemática](https://developers.openai.com/blog/eval-skills).
