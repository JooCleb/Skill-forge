---
name: priority-ranker
description: >-
  Use mediante pedido explícito de priorizar tarefas, riscos, problemas ou hipóteses
  para um objetivo concreto, ou etapa nomeada de priorização em workflow já
  autorizado, no ChatGPT Work ou no Codex quando houver código. Não use para
  ranking genérico sem finalidade, ordenação alfabética, classificação por
  categoria ou escolha apenas da próxima ação.
---

# priority-ranker

## Entradas

Identificar itens e IDs, objetivo, horizonte, restrições, critérios/preferências,
ordem anterior e evidências disponíveis. Separar fatos, estimativas e lacunas;
perguntar somente pelo dado que muda materialmente a ordem. Sem esse dado,
entregar a parte sustentada e explicitar a limitação. Sem finalidade delimitável,
solicitar o objetivo, sem produzir ranking genérico.

## Procedimento

1. **Conferir o escopo.** Exigir pedido explícito desta priorização ou etapa
   nomeada já autorizada. Fora disso, atender à solicitação original diretamente.
   Ordenar itens existentes; não converter o pedido em plano completo nem escolher
   somente uma ação.
2. **Fixar os critérios.** Relacionar cada critério ao objetivo e declarar a regra
   de comparação antes da lista. Usar preferências informadas; na ausência,
   propor regra qualitativa provisória coerente com o objetivo, sem atribuí-la
   ao usuário. Distinguir:

   | Dimensão | Observar |
   | --- | --- |
   | Urgência | Prazo e consequência de adiar. |
   | Impacto | Contribuição para o objetivo ou dano evitado. |
   | Esforço | Tempo, custo e recursos necessários. |
   | Risco | Incerteza e consequências de agir ou adiar; distingui-las. |
   | Bloqueios | Pré-condições pendentes e trabalho que o item libera. |

   Marcar desconhecidos como desconhecidos, sem convertê-los em zero. Usar dados
   disponíveis; rotular estimativas e sua base. Não inventar probabilidades,
   pesos ou pontuações. Se um método numérico for solicitado e sustentado,
   explicitar escalas, pesos, fórmula e limitações.
3. **Preservar precedências.** Conferir pré-requisitos reais e estados atuais.
   Usar `A → B` para indicar que A é pré-requisito de B.
   Elevar pré-requisitos pelo valor do trabalho que liberam. Em ordem de execução,
   colocar o predecessor pendente antes do dependente. Pré-requisito concluído
   não bloqueia. Marcar dependências incertas, indisponibilidade externa e ciclos,
   sem desfazê-los arbitrariamente. Distinguir importância de disponibilidade:
   um item crítico bloqueado mantém sua importância; indicar o primeiro
   executável separadamente quando pertinente.
4. **Ordenar com discriminação suficiente.** Favorecer o que viabiliza o objetivo
   no horizonte informado. Esforço baixo não supera automaticamente impacto,
   urgência ou precedências. Em hipóteses, priorizar a investigação pelo efeito
   na decisão, evidência disponível e custo de verificação; não confundir essa
   prioridade com probabilidade de verdade. Agrupar empates no mesmo nível
   quando os dados não distinguirem itens; indicar o dado que poderia desfazê-los.
   Não usar posição original, nome ou precisão artificial como desempate.
5. **Explicar revisões.** Se houver ordem anterior, apontar subidas, descidas ou
   empates e o critério, evidência ou dependência que os motivou. Sem histórico,
   justificar a ordem proposta sem inventar mudanças.

Usar artefatos e justificativas observáveis, sem solicitar deliberação interna
privada. No Work, aproveitar materiais acessíveis; no Codex, associar itens a
issues, arquivos, logs ou testes disponíveis. Não inventar acessos ou resultados.
Não iniciar pesquisa, agentes ou outras meta-skills automaticamente. Priorizar
não autoriza corrigir código, executar tarefas ou contatar pessoas; continuar
execução somente se já estiver no escopo autorizado.

## Entrega

- **Objetivo e regra:** finalidade, horizonte e critérios decisivos.
- **Lista priorizada:** nível, item/ID, justificativa curta e estado; usar o mesmo
  nível para empates. Destacar precedências e primeiro executável quando útil.
- **Premissas e bloqueados:** estimativas, lacunas e condição de desbloqueio por
  item; declarar ausência de bloqueios conhecidos sem presumir verificação.
- **Mudanças:** diferenças em relação à ordem anterior, quando fornecida.

Exemplo de chamada: “Use priority-ranker para priorizar estes bugs para a
apresentação de amanhã, considerando o fluxo principal e as dependências.”

## Verificação

Conferir cobertura dos itens, vínculo dos critérios ao objetivo, precedências,
sentido das setas, empates, estimativas e coerência das justificativas. Corrigir apenas a parte
afetada. Distinguir inspeção, simulação e teste observado; não afirmar validações
não realizadas.

## Condição de parada

Encerrar ao entregar ordem ou níveis justificáveis, premissas e bloqueios, ou
registrar falta de objetivo/ativação. Se faltarem dados, preservar empates e
ordem parcial; não forçar conclusão nem ampliar a análise. Não reabrir a
priorização sem evidência nova ou novo pedido.
