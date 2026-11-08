---
name: adaptive-planner
description: >-
  Atualize um plano de trabalho em andamento no ChatGPT Work ou no Codex quando
  houver código. Use mediante pedido explícito de replanejamento após resultado,
  mudança de prioridade, evidência ou bloqueio relevante, ou etapa nomeada de
  replanejamento em workflow já autorizado. Preserve trabalho válido e requisitos,
  revise dependências e mostre diferenças, motivos e impactos. Não use para criar
  plano inicial, executar uma próxima etapa inequívoca, mudar estratégia sem fato
  novo ou revisar planos por rotina.
---

# adaptive-planner

## Entradas e limites

- Ler objetivo, requisitos obrigatórios, flexibilizações autorizadas, plano
  anterior, estado das etapas, artefatos produzidos e evidência nova. Usar apenas
  contexto e recursos acessíveis e autorizados; não presumir memória entre chats,
  acesso a arquivos, pesquisa ou ferramentas.
- Identificar fonte ou relato e momento/versão relevantes da mudança. Separar
  fato observado ou informado, hipótese e lacuna. Usar justificativas e evidências
  observáveis, sem pedir deliberação interna privada.
- Perguntar apenas pelo dado que altere materialmente o replanejamento. Se faltar
  o plano anterior, reconstruir somente o que o contexto sustenta e marcar a
  baseline como parcial; pedir o trecho indispensável antes de alterar dependências
  desconhecidas. Não inventar um plano anterior para produzir diferenças.
- Restringir a análise ao pedido ou à etapa nomeada autorizada. Não chamar outras
  meta-skills automaticamente. Recomendar mudanças não concede permissão nova
  para executar ações de domínio; respeitar a execução já autorizada.

## Procedimento

1. **Conferir a mudança.** Comparar a evidência nova com as premissas do plano.
   Identificar o que mudou e por que afeta viabilidade, prioridade ou critério de
   aceite. Sem mudança material, manter o plano e explicar brevemente; não gerar
   replanejamento cosmético. Com evidência inconclusiva, propor a verificação mínima
   e um encaminhamento provisório, sem tratar hipótese como falha confirmada.
2. **Localizar o impacto.** Vincular evidência → premissa invalidada/alterada →
   etapas e dependências afetadas, inclusive consequências posteriores. Separar
   trabalho ainda válido, reutilizável com ajuste, pendente de verificação e
   invalidado. Preservar artefatos e verificações compatíveis; conferir atualidade
   e aderência dos dados antes de reutilizá-los. Não descartar tudo nem manter um
   resultado apenas pelo esforço já investido.
3. **Comparar rotas viáveis.** Examinar recuperação da rota atual, substituição de
   recurso/método e redução de escopo somente quando permitida; omitir opções sem
   aplicação explicando o motivo. Comparar aderência aos requisitos, esforço
   adicional, prazo, risco, reversibilidade e dependências desbloqueadas. Usar
   estimativas com premissas e incerteza, sem pontuações ou precisão artificiais.
   Se nenhuma rota preservar requisito obrigatório, registrar o impedimento e a
   decisão ou condição necessária; não rebaixar o requisito nem declarar entrega
   completa. Suspender somente as partes dependentes, preservando o avanço viável.
4. **Atualizar o necessário.** Escolher a rota com justificativa observável,
   respeitando prioridades vigentes. Manter IDs, resultados e estimativas não
   afetados; alterar estados, sequência, dependências e estimativas apenas onde
   a mudança repercute. Recalcular impactos agregados, como prazo final, quando
   dependerem dessas alterações. Distinguir mudanças aprovadas de propostas que
   dependem de decisão; não inserir redução de escopo não autorizada no plano vigente.
5. **Definir a retomada.** Indicar próxima ação viável, pré-requisitos e resultado
   observável de sucesso, ou condição concreta de desbloqueio. Fixar um gatilho
   pertinente de nova revisão, como falha da alternativa, evidência incompatível
   ou limite informado atingido; evitar ciclos por calendário ou contagem arbitrária.
   Não prometer monitoramento em segundo plano nem criar automações.

No Work, aplicar a documentos, pesquisas, estudos e demais trabalhos acessíveis.
No Codex, vincular mudanças a arquivos, versões, diffs, logs e resultados de testes
pertinentes disponíveis; separar inspeção, simulação, teste proposto e teste
executado. Reaproveitar verificações válidas e propor novas somente para riscos
ou comportamentos afetados. Não alegar acesso, execução ou aprovação não observados.

## Entrega

Apresentar de forma proporcional ao caso:

- **Mudança e motivo:** evidência nova, premissa afetada e objetivo preservado.
- **Diferenças e impacto:** etapa/ID, antes → agora, motivo e efeito em prazo,
  custo, risco ou dependências; indicar também o trabalho preservado. Separar
  estimativas de resultados observados.
- **Plano vigente:** versão ou marco, etapas suficientes para continuar,
  dependências, estados e pendências; distinguir sugestões ainda não autorizadas.
- **Próxima ação e revisão:** pré-requisitos, critério observável de sucesso e
  gatilho para rever. Em impasse, explicitar requisito impedido e decisão necessária.

Entregar no chat por padrão. Atualizar um artefato existente apenas quando houver
esse escopo e capacidade real, conferindo sua versão e a gravação. Sem mudança,
entregar apenas a manutenção justificada e o próximo passo já previsto.

## Verificação e parada

Conferir se cada alteração tem evidência e efeito identificáveis, se requisitos
obrigatórios continuam ativos e se dependências apontam para entradas viáveis.
Checar que trabalho válido foi preservado, partes afetadas foram reavaliadas e
que o plano não depende de acesso ou aprovação inexistente. Explicitar limitações.

Encerrar ao entregar diferenças, impacto, plano vigente e próxima ação com gatilho,
ou manutenção justificada/impedimento específico. Retomar somente por novo pedido
ou etapa/gatilho dentro do workflow autorizado; não iniciar revisão permanente
nem executar novas tarefas fora do escopo.
