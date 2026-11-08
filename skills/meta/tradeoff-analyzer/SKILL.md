---
name: tradeoff-analyzer
description: >-
  Use mediante pedido explícito de analisar trade-offs ou compromissos entre
  alternativas reais com objetivos concorrentes, ou etapa nomeada dessa análise
  em workflow já autorizado, no ChatGPT Work ou no Codex com código, sem exigir
  escolha de vencedora. Não use para comparação por uma única dimensão,
  recomendação sem alternativas reais, simples menção a ganhos e perdas ou
  execução da alternativa escolhida.
---

# tradeoff-analyzer

## Entradas e escopo

- Recuperar alternativas reais, objetivo, horizonte, dimensões, restrições obrigatórias, preferências declaradas e evidências do contexto autorizado. Pedir apenas lacunas que mudem materialmente a análise; explicitar hipóteses nos demais pontos.
- Confirmar o pedido explícito ou a etapa nomeada autorizada. Se o caso estiver nas exclusões, responder diretamente ao pedido sem fabricar alternativas, dimensões ou tabela de trade-offs.
- Trabalhar com artefatos, dados, evidências e justificativas observáveis; não solicitar deliberação interna privada. Não chamar outras meta-skills automaticamente nem presumir acesso a memória, arquivos, pesquisa ou agentes.

## Procedimento

1. **Definir dimensões e restrições.** Selecionar dimensões materiais e concorrentes; registrar direção desejável, unidade ou escala e horizonte comparável. Separar requisito obrigatório de preferência; evitar dupla contagem. Marcar cada alternativa como viável, inviável com motivo ou com viabilidade pendente. Não compensar violação obrigatória com economia ou outra vantagem, nem flexibilizar requisito por conta própria.
2. **Explicitar efeitos e hipóteses.** Para cada alternativa, relacionar ganhos e perdas às mesmas dimensões, com fonte ou artefato identificável. Distinguir dados fornecidos, observações, cálculos, estimativas e hipóteses; registrar lacunas como desconhecidas. Usar comparação qualitativa ou faixas quando faltarem medidas, sem inventar números. Indicar condições que alteram os efeitos; por exemplo, distinguir latência de cache aquecido e cache vazio, taxa de acertos e estratégia de atualização quando relevantes.
3. **Verificar dominância.** Comparar opções viáveis sob as mesmas condições. Marcar uma opção como dominada somente se outra for pelo menos tão boa em todas as dimensões materiais e estritamente melhor em alguma; mostrar qual opção a domina e a evidência. Separar inviabilidade de dominância. Com dimensão decisiva desconhecida, registrar dominância não demonstrada ou condicional. Preservar opções não dominadas sem impor ordem universal.
4. **Examinar reversão.** Explicitar custos de trocar ou desfazer cada opção: tempo, dinheiro, migração, dependência de fornecedor e perdas irrecuperáveis pertinentes. Distinguir custo inicial, operação e reversão; apontar assimetrias entre os sentidos da troca. Registrar custo desconhecido sem presumir reversibilidade gratuita.
5. **Expor preferências decisivas.** Mostrar “A favorece quem prioriza X sob Y; B favorece quem prioriza Z sob W”. Separar preferência ainda não declarada de incerteza factual. Apontar limiares de mudança somente quando calculáveis com base explícita; usar condições qualitativas nos demais casos. Não atribuir pesos ao usuário nem esconder perda importante em pontuação única. Recomendar somente se isso também tiver sido pedido, de forma condicional às preferências e à viabilidade.

No Codex, vincular efeitos a arquivos, configurações, diffs, medições ou resultados acessíveis. Distinguir inspeção, simulação, teste executado e teste proposto. Usar somente capacidades e permissões reais; a análise, por si, não autoriza alterar código, executar benchmarks, contratar ou implementar opções. Respeitar ações já autorizadas no escopo vigente.

## Entrega

Apresentar brevemente o escopo e as restrições decisivas. Usar uma linha por alternativa na tabela abaixo, mantendo as seis colunas, inclusive **Decisões dependentes de preferência**. Preencher essa coluna em cada linha com a prioridade que favorece a opção ou “nenhuma preferência torna esta opção viável”, conforme o caso. Usar “não informado” para dados ausentes; dimensionar a extensão das células ao pedido.

| Alternativa e viabilidade | Ganhos por dimensão | Perdas por dimensão | Hipóteses e condições favoráveis | Custo de reversão | Decisões dependentes de preferência |
| --- | --- | --- | --- | --- | --- |

Vincular as células às evidências ou notas de hipótese identificáveis. Destacar inviáveis e dominadas com seus motivos; se só restar uma viável, informar isso sem criar equilíbrio artificial. Fechar com as preferências em aberto e os dados materiais ausentes, sem exigir escolha. Se nenhuma opção for viável, registrar o impasse e o requisito envolvido.

Exemplo: “Use tradeoff-analyzer para comparar cache agressivo e atualização imediata, explicitando ganhos, perdas e condições favoráveis sem escolher uma vencedora.”

## Verificação e parada

- Conferir unidades, horizonte, restrições, cálculos usados e base das alegações de dominância. Manter perdas relevantes visíveis, hipóteses separadas de fatos e preferências não inventadas.
- Conferir que a tabela cubra as alternativas e dimensões materiais, inclua reversão e identifique decisões pendentes. Relatar somente acesso, pesquisa e testes efetivamente realizados.
- Encerrar após tornar os compromissos e suas condições verificáveis, com preferências e lacunas delimitadas. Se faltar dado essencial, entregar análise parcial e pedir apenas esse dado; não prolongar a análise para forçar ranking, procurar novas alternativas ou executar a solução.
