---
name: decision-analyst
description: >-
  Compare alternativas concretas ou delimitáveis em decisões com critérios concorrentes
  e consequências relevantes, no Work ou Codex. Explicite restrições, preferências,
  incertezas e condições que mudam a recomendação. Não use para escolha trivial,
  simples organização de tarefas ou execução da alternativa escolhida.
---

# decision-analyst

## Entradas

Recuperar decisão, objetivo, horizonte, alternativas, restrições eliminatórias, preferências e evidências disponíveis. Incluir não agir/adiar quando viável e explicitar seu custo. Perguntar apenas sobre lacunas decisivas; desconhecimento de requisito obrigatório não equivale a aprovação ou reprovação.

## Procedimento

1. **Filtrar viabilidade.** Separar requisitos obrigatórios de preferências. Marcar alternativas como viáveis, inviáveis com motivo ou pendentes de informação. Uma pontuação alta não compensa violação de requisito obrigatório; se nenhuma satisfizer, explicar quais restrições precisariam mudar, sem alterá-las unilateralmente.
2. **Definir critérios.** Registrar direção desejável, unidade/escala e horizonte comum. Evitar dupla contagem e custos duplicados; justificar dependências e efeitos não compensáveis. Preferir comparação qualitativa ou dominância quando suficiente; não impor soma ponderada a dados incomparáveis.
3. **Fixar preferências.** Usar pesos declarados; normalizá-los se necessário e mostrar como. Sem pesos, propor valores explicitamente provisórios ou comparar cenários de preferência. Não atribuir preferências ao usuário sem evidência. Pesos dependem da escala adotada.
4. **Estimar consequências.** Distinguir fatos/fontes, cálculos, estimativas e hipóteses. Considerar custos totais, riscos, reversibilidade e custo de oportunidade. Usar faixas ou cenários coerentes quando faltarem dados; não inventar probabilidade ou transformar dado ausente em zero. Verificar informações mutáveis antes de recomendação dependente delas.
5. **Comparar.** Se usar pontuação, explicitar escalas e âncoras, direção e fórmula; manter unidades originais e cálculos auditáveis. Não ajustar escalas para favorecer uma opção. Não esconder risco assimétrico ou perda irrecuperável em uma média.
6. **Testar sensibilidade.** Variar os pesos e estimativas capazes de mudar a conclusão, incluindo cenários conjuntos coerentes. Mostrar pelo menos a comparação efetivamente calculada e, quando possível, o limiar de inversão. Sem base numérica, explicitar condições qualitativas; não inventar limiar exato. Pequenas mudanças que invertem a ordem tornam a recomendação frágil.
7. **Decidir condicionalmente.** Relacionar recomendação às premissas e robustez. Identificar qual informação/preferência mais pode alterar a decisão e custo razoável de obtê-la; distinguir avaliação qualitativa de cálculo formal do valor da informação.

No Codex, usar medições reproduzíveis de compatibilidade, desempenho e custo quando disponíveis. Analisar não autoriza comprar, contratar, alterar código ou executar a alternativa; respeitar ações já solicitadas no escopo vigente.

## Entrega

Apresentar matriz de alternativas × critérios com viabilidade, fontes/premissas e pesos quando usados. Explicar trade-offs, sensibilidade e recomendação condicional, seguida da informação mais decisiva ainda ausente. Dimensionar o formato à decisão; não gerar precisão artificial nem uma vencedora absoluta quando os dados não distinguirem as opções.

## Verificação e parada

Recalcular totais/normalização e conferir unidades, restrições, dados faltantes, dupla contagem e condições de inversão. Encerrar com comparação suficiente e incerteza visível; se não houver discriminação, entregar opções ainda plausíveis e próximo dado decisivo, sem forçar ranking.
