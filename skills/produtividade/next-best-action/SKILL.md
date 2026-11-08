---
name: next-best-action
description: >-
  Escolha a ação imediata mais útil entre alternativas em um problema, documento
  ou projeto no ChatGPT Work ou, com código, no Codex. Use somente mediante
  pedido explícito de decidir o próximo passo ou etapa nomeada dessa análise em
  workflow já autorizado, considerando dependências, risco e ganho de informação.
  Não use para elaborar um plano completo, executar uma próxima etapa já definida
  ou inequívoca, nem impor análise de prioridade ao trabalho rotineiro.
---

# next-best-action

## Entradas

Identificar objetivo, estado atual, evidências disponíveis, ações consideradas,
bloqueios, dependências, restrições e recursos ou prazo informados. Usar apenas
contexto, artefatos, capacidades e permissões disponíveis. Separar fatos,
hipóteses e lacunas; perguntar somente pelo dado que mude materialmente a escolha.
Não presumir acesso a outros chats, memória, fontes, agentes ou ferramentas.

## Procedimento

1. **Conferir o escopo.** Confirmar o pedido explícito ou a etapa nomeada
   autorizada. Se o objetivo já estiver atendido, indicar encerramento sem
   inventar trabalho. Se a próxima ação já estiver definida ou inequívoca,
   seguir a execução solicitada dentro da autorização existente, sem abrir
   nova comparação. Se o pedido for um plano completo, atender esse escopo sem
   substituí-lo por esta análise.
2. **Delimitar poucas candidatas.** Considerar apenas ações concretas, em geral
   duas a quatro, que possam produzir avanço ou remover um bloqueio agora.
   Conferir pré-requisitos, dependências, acesso e autorização; separar ações
   viáveis das que dependem de condição ainda ausente. Não escolher uma ação
   inacessível como se fosse executável. Se todas estiverem bloqueadas, escolher
   a solicitação mínima que viabilize avanço: especificar artefato, trecho,
   permissão estritamente necessária ou esclarecimento e sua finalidade.
   Preferir evidência suficiente ou acesso restrito; não pedir credenciais.
3. **Comparar utilidade marginal.** Relacionar cada candidata a ganho esperado
   para o objetivo, esforço/custo, risco, reversibilidade e etapas que desbloqueia.
   Considerar prazo e custo de adiar quando pertinentes. Explicar o que uma
   medição permitiria decidir; informação sem efeito sobre a decisão não basta.
   Com hipóteses concorrentes, favorecer uma observação que as distinga quando
   seu benefício justificar o custo. Não priorizar coleta por rotina se já houver
   evidência suficiente para agir. Usar comparação qualitativa proporcional ao
   caso; não inventar probabilidades, pesos, pontuações ou precisão numérica.
4. **Escolher uma ação delimitada.** Indicar a candidata de maior utilidade
   justificável nas condições observadas e o motivo de preceder as demais.
   Em empate relevante, preferir a ação de menor custo e risco, com maior
   reversibilidade, preservando opções. Se a escolha depender de premissa decisiva desconhecida, recomendar
   obter esse dado mínimo; sem ação útil viável, declarar o impasse. Não inventar
   preferência do usuário, flexibilizar requisitos nem pedir novamente permissão
   já concedida.
5. **Definir a observação de saída.** Indicar resultado, registro ou mudança
   verificável e como os resultados plausíveis determinarão a decisão seguinte,
   sem construir um roteiro inteiro. Em diagnóstico, sucesso da ação pode ser
   distinguir hipóteses, mesmo que a falha persista. No Codex, vincular a proposta
   ao arquivo, comando, entrada e saída pertinentes quando conhecidos; não
   inventar caminhos, testes ou resultados. Distinguir proposto, simulado e
   executado. Um pedido de análise não autoriza executar a recomendação; se
   execução já estiver no escopo, prosseguir nos seus limites.

Trabalhar com evidências e justificativas observáveis, sem solicitar deliberação
interna privada. Não chamar outras meta-skills, iniciar pesquisa, criar agentes,
monitoramento ou tarefas externas automaticamente.

## Entrega

Responder de forma breve, com:

- **Próxima ação:** uma ação concreta e delimitada, ou solicitação mínima de desbloqueio.
- **Motivo:** ganho esperado e comparação com as alternativas relevantes, com incerteza explícita.
- **Pré-requisitos:** dependências, dados e acesso necessários; apontar o que já está atendido.
- **Resultado decisivo:** critério observável de sucesso ou aprendizado e resultado que orientará o passo seguinte.

Não usar tabela de pontuação ou listar alternativas apenas para preencher formato.

## Verificação

Conferir que a ação respeite objetivo, dependências, recursos e autorização;
que o motivo decorra das evidências; e que o resultado possa mudar uma decisão.
Não confundir recomendação com execução nem simulação com teste observado.

## Condição de parada

Encerrar esta análise ao entregar uma ação justificável, seus pré-requisitos e
critério de resultado, ou o bloqueio com a solicitação mínima. Não reabrir a
comparação sem evidência nova ou novo pedido, nem transformar a recomendação em
ciclo autônomo. Continuar apenas a execução que já integre o escopo autorizado.
