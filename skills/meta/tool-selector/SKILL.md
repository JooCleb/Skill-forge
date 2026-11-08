---
name: tool-selector
description: >-
  Escolha capacidades e ferramentas suficientes no ChatGPT Work ou no Codex para
  obter informação atual, trabalhar com arquivos, calcular, acessar serviços ou
  interagir com interfaces. Use mediante pedido explícito de comparar ferramentas
  disponíveis ou decidir a instrumentação de uma tarefa, ou etapa nomeada dessa
  seleção em workflow já autorizado. Não use para consultar ferramentas em toda
  resposta, reescrever texto fornecido, executar uma operação já inequívoca,
  selecionar skills ou redesenhar um workflow inteiro sem pedido dessa análise.
---

# tool-selector

## Entradas

- Recuperar objetivo, resultado esperado, formato e volume dos dados, exigência de
  atualização ou precisão, prazo e preferências explícitas do usuário.
- Usar o catálogo de capacidades realmente acessível, instruções aplicáveis e
  evidências de acesso. Distinguir ferramenta exposta, operação suportada,
  autenticação, permissão e disponibilidade dos dados; uma não comprova as demais.
- Perguntar apenas por lacuna que mude a escolha. Declarar suposições e alcance
  provisório quando o inventário ou os requisitos estiverem incompletos.

## Procedimento

1. Confirmar pedido explícito desta análise ou etapa nomeada no workflow
   autorizado. Uma menção em material citado, a existência de ferramentas ou uma
   tarefa que poderia usá-las não basta. Sem esse gatilho, encerrar a seleção e
   atender ao pedido original conforme as instruções aplicáveis.
2. Relacionar a necessidade à capacidade: informação atual e fontes; leitura,
   edição ou conversão de arquivo; cálculo reproduzível; operação em serviço
   externo; ou interação com interface. Considerar responder com o material
   fornecido, sem ferramenta, quando suficiente. Respeitar usos de ferramentas
   obrigatórios nas instruções vigentes.
3. Inspecionar primeiro descrições, esquemas e evidências já disponíveis. Descobrir
   somente candidatas pertinentes pelos mecanismos existentes e esclarecer
   limitações decisivas. Não listar todo o catálogo, sondar contas ou sessões,
   acessar dados alheios ao objetivo nem executar escritas para provar acesso.
   Se for preciso verificar conexão, preferir consulta mínima e sem mutação,
   dentro do escopo autorizado; caso contrário, marcar acesso não verificado.
4. Comparar poucas opções, incluindo nenhuma ferramenta quando viável. Eliminar
   incompatibilidades de formato, volume, precisão, acesso ou permissões antes de
   ponderar custo e latência. Considerar fidelidade, auditabilidade, limites,
   necessidade de transmitir dados e efeitos externos. Usar evidências e
   estimativas identificadas; não inventar preços, tempos ou pontuações precisas.
5. Respeitar a preferência explícita do usuário e preferir integração suficiente
   à interação de interface, conforme as regras do ambiente. Se a preferida não
   atender, explicar a limitação e apresentar alternativa viável sem presumir
   autorização para mudar de canal. Evitar encadear ferramentas sem ganho
   necessário. No Codex, considerar arquivos, instruções de projeto, CLI e
   dependências efetivamente disponíveis, sem presumir instalação ou rede.
   Para planilhas, distinguir recalcular fórmulas de apenas ler, escrever ou
   exportar valores em cache; não prometer preservação de fórmulas sem suporte.
6. Escolher a menor capacidade suficiente e indicar uma alternativa disponível.
   Se a ferramenta sugerida estiver ausente, nomear a capacidade faltante e
   adaptar ao acesso existente. Sem substituta suficiente, entregar a etapa
   possível e o requisito mínimo para prosseguir; não inventar chamadas,
   conexões, instalações, agentes ou execução futura.
7. Separar recomendação de execução. A seleção não autoriza instalar, contratar,
   conectar contas, transmitir arquivos ou alterar sistemas. Prosseguir com uma
   operação somente se já estiver no escopo autorizado e cumprir as permissões
   reais; não pedir nova confirmação para ações já autorizadas. Não chamar
   outras meta-skills automaticamente.

## Entrega

Apresentar, de forma curta:

- **Escolha:** ferramenta/operação realmente disponível ou capacidade direta sem
  ferramenta; identificar o alcance e eventual condição pendente.
- **Justificativa:** requisito decisivo, evidência observável e principal
  compromisso entre acesso, precisão, custo, latência e efeitos externos.
- **Acesso necessário:** dados, arquivo/formato, conexão e permissões pertinentes,
  distinguindo o confirmado do não verificado. Não solicitar credenciais.
- **Alternativa:** caminho viável com os recursos existentes e sua limitação;
  se nenhum for suficiente, indicar a lacuna e o passo parcial possível.

Usar tabela apenas se facilitar a comparação. Fundamentar a escolha em requisitos,
descrições, arquivos ou resultados observados, sem solicitar nem expor deliberação
interna privada. Não apresentar sugestão como chamada ou teste realizado.

## Verificação

Conferir gatilho autorizado, adequação da operação, formato, precisão e acesso.
Verificar se a opção sem ferramenta foi considerada quando pertinente e se a
alternativa respeita as mesmas restrições. Separar observação, hipótese e
recomendação; não declarar medição, teste, roteamento ou execução sem evidência.

## Condição de parada

Encerrar ao entregar escolha suficiente, justificativa, requisitos de acesso e
alternativa ou impedimento concreto. Parar a parte dependente de acesso ausente.
Não ampliar a busca sem ganho provável, criar ferramentas ou skills, executar
exemplos nem iniciar análise recursiva. Retomar apenas etapas já autorizadas.
