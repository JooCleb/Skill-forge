---
name: bias-checker
description: "Examine vieses observáveis no enquadramento, na seleção de dados e na avaliação de alternativas de uma análise, pesquisa ou processo de decisão no ChatGPT Work, ou no Codex quando houver código. Use mediante pedido explícito de auditar vieses ou etapa nomeada dessa análise em workflow já autorizado. Não use para atribuir motivações pessoais, diagnosticar pessoas, desqualificar discordância, fazer comparações comuns sem pedido de auditoria ou tratar preferência declarada como distorção factual."
---

# bias-checker

## Entradas

- Delimitar a pergunta, a conclusão ou hipótese inicial e o material a auditar: texto, tabela, fontes, amostra, critérios ou artefatos de código disponíveis.
- Identificar população e período de referência, alternativas, exclusões justificadas e preferências declaradas. Registrar o que não foi informado; pedir apenas o que mudar materialmente a auditoria.
- Usar artefatos, evidências e justificativas observáveis. Não solicitar deliberação interna privada nem presumir acesso a arquivos, fontes, pesquisa, memória, agentes ou testes.

## Procedimento

1. Comparar a pergunta com a conclusão: verificar se a formulação já pressupõe o resultado ou restringe alternativas pertinentes sem justificativa.
2. Comparar amostra e dados com o escopo: examinar recrutamento, fontes, períodos, denominadores e exclusões. Buscar seleção assimétrica e exclusões injustificadas; distinguir ausência de informação de distorção demonstrada. Sem dados demográficos necessários, declarar que o viés de amostragem não pôde ser avaliado, sem presumir sua existência ou direção.
3. Comparar critérios entre alternativas: aplicar a mesma referência temporal, unidades, condições e exigência de evidência; examinar pesos e limiares. Distinguir prioridade declarada de distorção factual: uma preferência não demonstra viés por si só.
4. Examinar apoio e contrapontos à hipótese inicial: identificar evidências contrárias omitidas ou tratadas com exigência maior, interpretação seletivamente favorável e explicações alternativas ignoradas. Não exigir peso igual para evidências de qualidades diferentes nem inventar contrapontos para produzir equilíbrio.
5. Vincular cada possível viés a um trecho, dado, critério ou exclusão localizável. Explicar o efeito potencial na conclusão; indicar direção apenas quando sustentada e não inventar magnitude. Discordância isolada não demonstra viés; evitar inferências sobre intenção ou diagnóstico psicológico.
6. Propor uma correção verificável para cada achado: alinhar datas e condições, explicitar exclusões, aplicar critérios simétricos, buscar evidência contrária com regra de busca declarada ou reavaliar a conclusão com os mesmos critérios. Dizer como conferir a correção; não apresentar uma proposta como já executada.

No Codex, aplicar esses passos a requisitos, conjuntos de dados, filtros, métricas, benchmarks, fixtures e logs disponíveis. Citar arquivo e linha quando acessíveis; comparar versões, ambientes e cargas de trabalho. Executar comandos ou alterar código somente dentro do escopo autorizado e com capacidades reais. Identificar inspeção estática, simulação e teste executado sem confundi-los. Não chamar outras meta-skills automaticamente.

## Entrega

Apresentar escopo e limites brevemente e usar a tabela:

| Possível viés ou estado | Evidência no material | Efeito na análise | Medida corretiva e como verificar |
|---|---|---|---|

Separar achados sustentados de suspeitas condicionais e aspectos não avaliáveis. Para dados insuficientes, registrar a lacuna e o que permitiria avaliar, sem inventar um achado. Se nenhum indício for sustentado, dizer “não identifiquei indícios suficientes no material disponível”, sem certificar ausência de vieses. Priorizar o que puder mudar a conclusão.

## Verificação

Conferir se cada achado tem evidência localizável, se os critérios são simétricos e se a correção tem condição observável de conclusão. Separar preferência, discordância e falta de dados de distorção demonstrada; retirar atribuições psicológicas. Informar quais fontes ou verificações foram efetivamente acessadas ou executadas e o que ficou apenas proposto.

## Condição de parada

Encerrar após entregar achados, efeitos, correções verificáveis e limites do material. Se faltar o próprio material, indicar a lacuna e solicitar apenas o insumo indispensável, sem fabricar auditoria. Não iniciar pesquisa externa, implementar correções nem ampliar a análise além do escopo autorizado.
