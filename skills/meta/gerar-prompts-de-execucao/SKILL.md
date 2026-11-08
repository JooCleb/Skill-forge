---
name: gerar-prompts-de-execucao
description: Use quando o usuário pedir prompts para realizar um trabalho, transformar um objetivo em etapas executáveis, descobrir por onde começar ou ajustar o próximo prompt a um resultado recebido. Aplica-se a sites, código, documentos, pesquisas, design e outras entregas, especialmente quando faltam referências ou materiais. Não usar para trilhas de aprendizagem, simples revisão de um prompt ou execução direta de uma tarefa sem pedido de planejamento por prompts.
---

# Gerador de Prompts de Execução

Transformar o objetivo em um mapa completo e entregar somente o próximo prompt executável. Atualizar o caminho conforme os resultados reais. Priorizar qualidade alta, com orientações curtas e potência proporcional à necessidade.

## Preferências do usuário

- Priorizar ChatGPT Work: projetos para trabalhos maiores, conversa avulsa para menores; adaptar ao Codex quando houver código e repositórios.
- Manter o trabalho no mesmo chat enquanto viável. Recomendar outro somente quando mudar o ambiente, houver excesso de contexto ou uma separação de responsabilidade útil.
- Entregar mapa em Markdown persistido e atualizado; apresentar o próximo prompt pronto para copiar na resposta.
- Quando faltarem referências e o usuário não as tiver, orientar pesquisa e apresentação de opções para ele escolher.
- Recomendar uma escolha técnica com consequências claras; consultar o usuário nas decisões difíceis de reverter que ainda não estejam autorizadas.
- Diante de resultado inadequado, gerar prompt de correção antes das etapas dependentes.
- Distinguir a geração dos prompts da execução: executar o projeto somente se o usuário solicitar essa mudança de papel.

## 1. Esclarecer o objetivo

Aproveitar primeiro as informações e arquivos já disponíveis. Perguntar apenas o que muda o escopo ou o próximo passo: resultado final, público, critérios de qualidade, ambiente, materiais existentes e restrições relevantes. Não aplicar questionário fixo, pedir dados já conhecidos ou solicitar decisões técnicas sem explicá-las.

Definir o que significa terminar: artefato utilizável, comportamento esperado, formato e forma de verificação. Tratar protótipo, versão funcional e entrega final como estados diferentes. Se o pedido for pequeno, permitir uma única etapa; não criar cerimônia nem etapas artificiais.

## 2. Mapear o trabalho

Criar `Mapa_de_Execucao_<Objetivo>.md` com:

- Objetivo, escopo, restrições e critérios finais de sucesso.
- Materiais e referências disponíveis, faltantes e onde obtê-los.
- Decisões confirmadas e hipóteses ainda provisórias.
- Tabela: ID estável, etapa, dependências, entrada necessária, entrega verificável, estado, porte, complexidade, modelo/classe e esforço estimados.
- Etapa atual, impedimentos, critério de aceitação e próximo passo.
- Links ou caminhos efetivamente disponíveis para artefatos e evidências.

Usar estados como planejada, pronta, em andamento, aguardando material, em correção e verificada. Marcar estimativas de modelo e esforço das etapas futuras como provisórias. Adaptar o mapa às dependências, incluindo pesquisa, construção, verificação e entrega quando pertinentes; não impor todas essas fases a todo pedido.

Salvar e atualizar a mesma identidade de arquivo pelo mecanismo disponível, usando a skill de Library quando aplicável. Se não puder salvar, entregar o Markdown e declarar a limitação. Não confundir um arquivo salvo com sua inclusão automática nas fontes de um projeto.

## 3. Resolver o que falta antes de comprometer a qualidade

Classificar cada ausência pelo efeito concreto:

| Ausência | Próximo passo |
|---|---|
| Informação sem a qual a etapa não pode ser correta | Prompt de coleta: perguntas específicas e pausa antes de executar a parte dependente |
| Referência que muda decisivamente a qualidade | Solicitar exemplos, arquivos ou links e explicar o que observar; se o usuário não tiver, pesquisar opções |
| Escolha técnica com consequências importantes | Recomendar uma opção, explicar custos, manutenção e reversibilidade relevantes e consultar quando necessário |
| Preferência secundária com padrão razoável | Declarar a premissa e prosseguir, mantendo-a ajustável |
| Acesso ou ferramenta indispensável indisponível | Indicar a capacidade necessária e alternativa viável; não prometer execução sem acesso |

Aplicar esta lógica a qualquer domínio: rubricar requisitos de trabalho acadêmico, obter dados e dicionário de colunas para análises, exemplos de tom para escrita, logs e reprodução para depuração, referências visuais e materiais de marca para design.

A etapa de coleta deve produzir entradas utilizáveis, não apenas dizer “mande mais detalhes”. Especificar o que enviar, em que formato, por que importa e o que fazer se não existir. Solicitar somente o mínimo suficiente. Não pedir senhas, tokens ou segredos no chat; orientar mecanismos seguros do ambiente quando forem necessários.

Para design, investigar referências reais e apresentar opções comparáveis, explicando composição, tipografia, imagens, hierarquia e interações relevantes. Esperar a escolha quando ela mudar a direção da criação. Adaptar os princípios ao projeto, respeitando licenças e identidade própria. Transformar “profissional” e “sem cara de IA” em critérios concretos verificáveis; não prometer excelência apenas com adjetivos no prompt.

Não inventar dados, materiais, resultados, links, consultas ou aprovações. Quando pesquisa não estiver disponível, explicar como fornecer as referências ou obter acesso; oferecer exploração provisória claramente identificada quando fizer sentido.

## 4. Escolher modelo e esforço separadamente

Antes de recomendar nomes e opções atuais, usar orientações oficiais disponíveis e a skill OpenAI Docs para verificar os modelos citados. Respeitar o modelo exato mencionado pelo usuário. Não fixar nesta skill uma tabela de preços, limites ou equivalências entre gerações. Se não houver verificação ou informação da interface, recomendar uma classe de capacidade e sinalizar que o nome precisa ser conferido; pedir a lista disponível somente quando isso alterar a escolha.

Avaliar cada etapa em duas dimensões independentes:

- **Porte:** volume, número de artefatos, extensão do contexto e quantidade de ações. Grande volume repetitivo favorece divisão em lotes, ferramentas e pontos de retomada; não exige sozinho modelo superior ou esforço máximo.
- **Complexidade:** raciocínio, ambiguidade, integração entre sistemas, conflito entre fontes e dificuldade de verificar erros. Elevar capacidade e esforço quando esses fatores o justificarem. Uma tarefa curta pode ser complexa.

Usar a configuração mais econômica que preserve a qualidade exigida. Começar com classe equilibrada e esforço médio para trabalho delimitado; indicar leve para alterações simples e verificáveis; alto para análise difícil, integração ou decisões com várias dependências. Reservar máximo para necessidade concreta, explicando o ganho esperado. Tratar isso como recomendação contextual, não benchmark ou garantia.

Em cada cartão de etapa, incluir: porte, complexidade, modelo ou classe recomendada, esforço e uma frase de justificativa. Dizer explicitamente se há motivo para aumentar o modelo, o esforço, ambos ou nenhum. Se uma etapa mistura coleta simples com raciocínio difícil, dividir ou indicar em que momento mudar a configuração. A recomendação não muda automaticamente o seletor do usuário.

## 5. Entregar o próximo prompt

Apresentar um cartão curto seguido de um único bloco copiável. Usar escrita em português brasileiro e campos preenchidos para o caso concreto:

**Etapa [ID] — [resultado concreto]**
- **Onde enviar:** mesmo chat no Work por padrão; especificar ambiente diferente apenas com motivo.
- **O que anexar/disponibilizar:** arquivos, referências e trecho relevante do mapa realmente necessários, ou “nada adicional”.
- **Porte / complexidade:** classificações e causa principal.
- **Modelo / esforço:** configuração verificada ou classe, com indicação de aumentar ou manter e justificativa breve.
- **O que trazer de volta:** artefato, evidência e decisões necessárias para preparar o próximo prompt.

O bloco copiável deve conter, nessa ordem:
1. Objetivo desta etapa e contexto confirmado suficiente.
2. Entradas disponíveis e dependências; quando faltarem, as perguntas ou pesquisa necessárias antes da execução dependente.
3. Ações concretas, escolhas relevantes e limites de escopo.
4. Entregável solicitado e critérios de aceitação observáveis.
5. Verificação apropriada e evidências a relatar, distinguindo execução de mera sugestão.
6. Condição de parada e retorno: concluir esta etapa, relatar pendências e aguardar o próximo prompt, sem executar etapas ainda não liberadas.

Escrever o prompt inteiro, pronto para uso. Não deixar placeholders evitáveis, mencionar arquivos inexistentes nem depender de outra skill estar instalada no chat de destino. Usar skills e plugins adequados se disponíveis; especificar a capacidade necessária e alternativa quando não estiverem disponíveis. Não escolher ferramentas só porque existem.

Incluir instruções de execução, não apenas “aja como especialista” ou “faça o melhor possível”. Pesquisa deve produzir fontes verificadas; código deve produzir arquivos e evidências de funcionamento; design deve produzir prévia inspecionável; documentos devem satisfazer critérios de conteúdo e apresentação. Respeitar o pedido e os limites do ambiente para publicação, gastos, dados e outras ações externas; não interpretar a existência de um prompt como nova autorização irrestrita.

## 6. Receber resultados e adaptar

Quando o usuário trouxer uma saída, consultar o mapa atual e inspecionar o artefato disponível. Comparar com os critérios da etapa. Não aceitar “pronto” como prova de que testes ou verificações foram feitos; pedir somente a evidência faltante que importe.

- **Resultado suficiente:** registrar o que foi verificado, atualizar o mapa e preparar o próximo prompt com as decisões reais.
- **Resultado incompleto ou inadequado:** registrar a lacuna e criar um prompt de correção específico, preservando o que já funciona. Descrever o problema observável, a mudança necessária, a verificação e o retorno esperado. Aguardar a correção antes de avançar nas etapas dependentes.
- **Limitação de ferramenta ou informação:** resolver a entrada ou capacidade faltante; não tentar compensar apenas aumentando o esforço.
- **Objetivo alterado:** revisar somente etapas afetadas, registrar novas dependências e manter IDs estáveis.

Concluir quando os critérios finais estiverem atendidos. Não criar ciclos infinitos de refinamento nem melhorias fora do escopo. Relatar limitações reais que restarem.

## 7. Continuidade e comandos

Reconhecer pedidos naturais: “próximo prompt”, “aqui está o resultado”, “corrija esta etapa”, “atualize o mapa”, “retomar em outro chat”. Recuperar estado disponível antes de perguntar novamente.

Para trocar de chat, preparar um bloco compacto com objetivo, decisões confirmadas, estado atual, impedimentos, artefatos e próximo passo. Dizer exatamente o que copiar ou anexar. Não presumir memória entre chats, acesso ao repositório ou sincronização de arquivos. Manter o mapa consolidado, evitando acumular transcrições completas.

## Exemplo de aplicação

Pedido: prompts para um portfólio com agenda, sem referências visuais.

Mapear descoberta dos serviços → referências e direção visual → conteúdo e regras de reserva → implementação → verificação → entrega. Emitir primeiro o prompt de descoberta no mesmo chat. Separar a escolha entre solicitar horário e reservar automaticamente, pois muda a implementação. Após obter o contexto do serviço, emitir prompt para pesquisar e apresentar referências reais comparáveis antes de criar o layout. Recomendar potência por dificuldade, não colocar todas as etapas no modelo mais forte. Se a agenda aceita reservas em horário ocupado, emitir correção do conflito e verificação antes de preparar a publicação.

## Conferência antes de entregar

Confirmar que o mapa alcança o objetivo, o próximo prompt é executável, as dependências estão explícitas, as referências necessárias têm caminho de obtenção, modelo e esforço têm justificativa própria e o usuário sabe o que trazer de volta. Preservar o papel de gerar prompts e manter a nova skill separada do gerador de trilhas de estudo.
