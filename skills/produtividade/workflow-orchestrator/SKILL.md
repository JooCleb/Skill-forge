---
name: workflow-orchestrator
description: >-
  Coordene a execução de um objetivo composto no ChatGPT Work, adaptando ao Codex
  quando houver código, com etapas dependentes de pesquisa, análise, produção e
  validação. Use em pedidos para realizar esse trabalho até a entrega, acompanhando
  estado, dependências e critérios de passagem. Não use para tarefa simples, como
  corrigir uma frase, planejamento sem execução, mera seleção ou composição de
  skills, nem coordenação exclusivamente de agentes.
---

# workflow-orchestrator

Coordenar a execução até uma entrega verificável, com o menor processo suficiente.
Tratar pesquisa, análise, produção e validação como capacidades a selecionar conforme
o objetivo, não como quatro fases obrigatórias. Não criar dependências de outras skills.

## Entradas

- Recuperar objetivo, entrega esperada, fontes e artefatos acessíveis, requisitos,
  critérios de conclusão, restrições e autorização presentes na conversa.
- Confirmar capacidades e permissões reais do ambiente. Não presumir plugins,
  agentes, memória persistente, pesquisa disponível ou acesso entre chats.
- Perguntar apenas pelo que muda materialmente a execução; adotar padrões razoáveis
  e explícitos no restante. Enquanto faltar uma entrada, avançar no trabalho independente.

## Procedimento

1. **Fixar o resultado.** Definir entrega, escopo e critérios observáveis de conclusão
   antes de executar. Preservar requisitos vigentes; não acrescentar exigências de
   qualidade sem relação com o pedido. Se o pedido não se enquadrar na descrição,
   atender diretamente ou limitar-se ao planejamento/seleção solicitados.
2. **Selecionar o necessário.** Escolher somente capacidades que acrescentam valor.
   Usar skills pertinentes apenas quando disponíveis e adequadas; consultar suas
   instruções ao usá-las. Não iniciar uma cadeia de meta-skills ou instalar integrações
   para preencher o plano. Executar diretamente o que não exige especialização adicional.
3. **Montar um plano curto.** Dividir em etapas com identificador, entrada, saída,
   responsável, dependências e critério de passagem. Usar o próprio assistente como
   responsável padrão; não inventar participantes. Identificar quais saídas são
   indispensáveis a cada etapa, sem bloquear tudo por uma entrada não relacionada.
4. **Executar e atualizar o estado.** Iniciar etapas cujas entradas necessárias estejam
   disponíveis e verificadas. Registrar o resultado real e sua evidência ao terminar
   cada uma. Executar sequencialmente por padrão. Delegar apenas quando houver
   capacidade disponível, permissão aplicável e ganho concreto; fornecer escopo,
   entradas, saída e critério ao delegado, evitar escritas concorrentes e conferir
   a entrega recebida antes de integrá-la. Sem delegação, seguir com o próprio assistente.
5. **Controlar passagens.** Usar os estados `pendente`, `em execução`, `em verificação`,
   `concluída`, `bloqueada` e, se necessário, `cancelada`. Liberar a etapa dependente
   somente quando as saídas de que ela precisa satisfizerem seus critérios. Marcar
   uma etapa como concluída somente após verificar sua saída; declaração de sucesso
   de ferramenta, agente ou skill, isoladamente, não substitui evidência.
6. **Conter falhas e replanejar.** Registrar falha observada, evidência, saídas afetadas
   e condição de retomada. Bloquear somente etapas que dependem dessas saídas e seus
   descendentes; continuar as independentes. Usar alternativa autorizada se preservar
   os critérios; limitar retentativas a tentativas justificadas por fatos novos.
   Não inventar pesquisa, dados ou testes para preencher lacunas. Revisar plano e
   critérios somente por mudança legítima, explicitando motivo e impacto; não relaxar
   critérios para declarar sucesso. Se uma saída mudar, invalidar apenas verificações
   e etapas afetadas, preservando trabalho ainda válido.
7. **Conferir a entrega real.** Relacionar cada critério à evidência da versão final.
   Para arquivos, reabrir o arquivo efetivamente produzido, inspecionar conteúdo e
   formato pertinentes e confirmar disponibilidade pelo mecanismo de entrega suportado;
   criar um arquivo ou mencionar um caminho não comprova sua validação. Para código,
   ler instruções do repositório, preservar alterações existentes, revisar o diff e
   executar os checks relevantes disponíveis. Registrar comandos, resultados e limites;
   não afirmar testes não executados. Se só houver inspeção ou simulação, declarar
   esse alcance. Não concluir enquanto algum critério obrigatório estiver sem evidência.

## Entrega e estado

Apresentar o resultado junto de um registro enxuto, sem reproduzir logs extensos:

| Etapa | Entrada → saída | Responsável | Depende de | Critério de passagem | Estado e evidência |
| --- | --- | --- | --- | --- | --- |
| Identificador e ação real | Insumo e artefato real | Executor confirmado | Identificadores ou nenhuma | Condição observável | Estado, referência da evidência e bloqueio, se houver |

Incluir artefatos acessíveis, critérios atendidos e pendências materiais. Referenciar
fontes, trechos, resultados observados ou testes pertinentes; distinguir fato de inferência.
Manter o estado na conversa; persistir um registro somente se houver mecanismo e
autorização adequados. Não prometer continuidade automática ou transferência entre chats.

## Verificação e parada

- Conferir que dependências, evidências e artefatos correspondem à versão atual e ao
  escopo autorizado; reutilizar evidência válida sem repetir trabalho desnecessário.
- Encerrar com conclusão somente quando todos os critérios obrigatórios estiverem
  satisfeitos. Não abrir novas etapas por rotina depois disso.
- Se não restar ação independente viável, encerrar a tentativa com estado parcial ou
  bloqueado, resultado disponível, causa e entrada/ação necessária para retomar.
  Não declarar conclusão integral nem permanecer em ciclo de tentativas.
- Solicitar aprovação apenas para ações que realmente a exigem pelas permissões
  vigentes; critérios de passagem técnicos não criam aprovações humanas adicionais.
