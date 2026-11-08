---
name: plan-builder
description: >-
  Converta um objetivo definido em plano de execução ordenado, com entregas e
  verificações, no ChatGPT Work ou no Codex quando envolver código. Use mediante
  pedido explícito de planejar trabalho com várias etapas ou etapa nomeada desse
  planejamento em workflow já autorizado. Não use para ação simples, mera
  decomposição sem sequenciamento, sequência de prompts, revisão de plano
  existente ou replanejamento após mudanças; não inferir pedido de plano só pela
  complexidade da tarefa.
---

# plan-builder

Produzir um plano executável e proporcional ao objetivo. Entregar o trabalho
ordenado, sem transformá-lo em sequência de prompts ou acionar outras meta-skills
automaticamente. Planejar não autoriza executar as etapas.

## Entradas

- Aproveitar objetivo, escopo, entregáveis, critérios de sucesso, restrições,
  recursos, decisões e contexto disponíveis na conversa e em artefatos acessíveis.
- Separar fatos confirmados, premissas adotadas e lacunas materiais. Perguntar
  somente pelo que muda viabilidade, ordem ou resultado; avançar nas partes
  independentes com padrões razoáveis e premissas explícitas.
- Respeitar o ambiente e as permissões reais. Não pressupor ferramentas, acesso
  externo, memória entre conversas, equipe ou repositório. Se a ativação não
  corresponder ao pedido, atender ao pedido original sem impor um plano.

## Procedimento

1. **Fixar o destino.** Resumir o resultado final, o que está dentro e fora do
   escopo e as condições observáveis de conclusão. Vincular requisitos conhecidos
   às entregas; não ampliar o projeto por conveniência.
2. **Ordenar entregas.** Usar dependências explícitas e IDs estáveis. Antecipar
   decisões ou verificações que reduzam risco e retrabalho, sem violar a ordem
   das dependências. Agrupar ações pequenas na entrega que as exige; indicar
   trabalho independente quando útil, sem presumir execução por agentes/equipe.
3. **Especificar cada etapa.** Registrar dependências, entrada necessária, ação
   concreta, saída verificável e critério de término. Trocar “validar tudo” por
   evidência e limiar de aceitação definidos. Distinguir produzir um artefato de
   comprovar sua adequação.
4. **Tratar bloqueios prováveis.** Para cada bloqueio relevante, indicar sinal de
   ocorrência, alternativa viável e condição de retorno. Se uma dependência
   externa ainda não existe, criar ponto de decisão: qual evidência permite
   integrar, quem decide se conhecido, quando revisar por evento ou data já
   acordada e o que fazer se continuar indisponível. Planejar trabalho útil
   independente; rotular contratos provisórios e simulações. Não tratar teste
   com mock como comprovação da integração real.
5. **Dimensionar e verificar.** Estimar esforço ativo por etapa em faixas com
   unidade e premissas, por exemplo, 2–4 horas sob as condições declaradas.
   Separar espera externa de esforço; marcar incertezas e o que pode alterar a
   faixa. Não converter estimativas em datas prometidas sem disponibilidade e
   prazos confirmados. Incluir revisão, teste ou inspeção proporcional ao risco,
   com evidência esperada, sem criar cerimônia desnecessária.

### Adaptação a código

Quando houver código, usar stack, convenções e arquivos efetivamente conhecidos.
Se permitido e necessário, inspecionar apenas o contexto acessível para planejar;
se faltar repositório, propor responsabilidades e marcar caminhos como propostas.
Planejar contratos/interfaces antes da integração, parsing separado de validação
de dados quando pertinente, casos de falha e verificações de comportamento.
Indicar comandos somente quando sustentados pelo projeto; distinguir comandos
planejados de testes executados. Não impor TDD, novos testes, commits ou deploys
sem necessidade do caso. Não implementar para preencher lacunas do plano.

## Entrega

Apresentar em português brasileiro, com detalhe suficiente para iniciar:

1. **Objetivo e limites**, contexto confirmado, premissas e lacunas que importam.
2. **Plano ordenado**, em tabela ou lista, com este conteúdo por etapa:
   `ID | dependências | entrada | ação | saída verificável | critério de término
   e evidência | esforço em faixa`. Usar blocos por etapa se a tabela ficar larga.
3. **Bloqueios e decisões**, com alternativas e condições de desbloqueio.
4. **Etapa inicial**, identificada por ID, entrada disponível e próxima ação
   concreta; se bloqueada, indicar a obtenção mínima necessária e trabalho
   independente disponível.
5. **Condições de conclusão do trabalho**, ligadas às entregas e verificações.

## Verificação e parada

Antes de entregar, conferir cobertura do objetivo e das restrições, ordem sem
ciclos, entradas disponíveis ou obteníveis, critérios observáveis, esforço em
faixas e contingências para os bloqueios relevantes. Justificar a ordem e as
escolhas com dependências, artefatos e riscos observáveis; não solicitar nem
expor deliberação interna privada. Corrigir lacunas nas etapas afetadas.

Encerrar o planejamento quando as etapas puderem começar com as entradas
indicadas, ou quando bloqueios e decisões pendentes estiverem delimitados,
com etapa inicial e conclusão explícitas. Dizer o que permanece provisório e
quais verificações foram apenas planejadas. Não executar automaticamente nem
pedir confirmação ritual; continuar execução somente se ela já estiver no
escopo autorizado ou for solicitada separadamente.
