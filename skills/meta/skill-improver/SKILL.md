---
name: skill-improver
description: >-
  Aprimore uma skill existente a partir de falhas, feedback de uso ou avaliações,
  mediante pedido explícito de melhoria ou etapa nomeada em workflow autorizado.
  Compare versão atual e candidata no Work ou Codex. Não use para criar do zero,
  aumentar texto sem problema identificado, otimizar só um exemplo ou substituir
  o mecanismo do ambiente para validar e persistir skills.
---

# skill-improver

## Entradas

Ler a versão atual e recursos pertinentes; recuperar casos de uso, saídas, feedback, condições observadas e requisitos que não podem regredir. Perguntar só pelo que altere a hipótese ou a verificação. Sem problema observável, entregar lacuna ou oportunidade de teste, não inventar uma melhoria.

## Procedimento

1. **Fixar baseline.** Registrar versão, casos e comportamento conhecido, distinguindo saídas reais de relatos. Definir objetivo, critérios de aceite, invariantes e orçamento de iteração antes de alterar. Mais texto ou menos palavras, isoladamente, não comprovam qualidade.
2. **Agrupar falhas.** Separar padrões recorrentes e incidentes isolados. Distinguir sintoma de causa e problemas de gatilho, instrução, recurso, dado, acesso, execução ou avaliação. Priorizar por impacto, recorrência, risco e complexidade; não apresentar estimativas como métricas medidas.
3. **Escolher patch pequeno.** Relacionar cada mudança a problema e efeito esperado. Preservar versão anterior/diff; não adicionar instrução por precaução abstrata. Separar diagnóstico pontual de melhoria sistêmica e não invocar outras meta-skills automaticamente.
4. **Preparar comparação.** Registrar expectativas antes das respostas. Selecionar casos antigos relevantes, negativos próximos, ambiguidades/falhas de ferramenta pertinentes e casos novos reservados para transferência. Usar condições comparáveis para baseline e candidata; declarar diferenças e contaminação. Em execução independente, fornecer apenas tarefa e artefatos, sem diagnóstico ou gabarito.
5. **Avaliar o ganho.** Comparar por critério e caso, sem esconder falha crítica em média. Não aceitar melhora local com regressão material ou sobreajuste. Revisar/reverter a mudança responsável; executar novamente apenas casos afetados e regressões justificadas. Medir custo/latência só quando houver instrumento e registro.
6. **Decidir e persistir.** Conservar alteração como validada apenas com evidência suficiente. Se só houver inspeção ou simulação, fornecer candidata/proposta e próximo teste; não alegar ganho comportamental. Usar o criador e o mecanismo vigente do ambiente para estrutura, validação e persistência, quando disponíveis e dentro da autorização existente. Não duplicá-los nem contorná-los.

No Work, usar referências reais aos artefatos; no Codex, revisão, diff, comandos e resultados. Não presumir acesso, memória, agentes ou roteamento observável. Trabalhar com artefatos e justificativas verificáveis, sem deliberação interna privada.

## Entrega

Fornecer versão melhorada ou patch proposto, baseline identificável, motivo/evidência de cada mudança e tabela:

`Caso/critério | Baseline observado | Candidata observada | Método/evidência | Resultado`

Marcar não executado onde faltar saída; separar inspeção, simulação, execução direta e roteamento real. Informar regressões, incertezas, restauração e estado exato de persistência. Não certificar confiabilidade geral por poucos casos.

## Verificação e parada

Conferir preservação dos requisitos, comparabilidade, independência dos casos novos e vínculo entre ganho alegado e evidência. Encerrar com melhoria sustentada, reversão justificada ou candidata pendente do teste decisivo. Não iniciar refinamento sem novo problema/critério nem executar tarefas externas dos exemplos.
