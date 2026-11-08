---
name: format-selector
description: >-
  Escolha como apresentar conteúdo no ChatGPT Work ou no Codex quando envolver
  código, mediante pedido explícito de seleção de formato ou etapa nomeada de
  desenho da entrega em workflow já autorizado. Recomende texto, tabela,
  checklist, diagrama, código ou documento conforme a tarefa do leitor e o meio
  disponível, com estrutura inicial baseada no conteúdo real. Não use quando o
  usuário já determinou o formato, para respostas factuais simples sem pedido
  desta análise ou para criar visuais sem ganho informacional.
---

# format-selector

## Entradas

- Identificar conteúdo real, objetivo do leitor, público, canal de entrega,
  extensão e restrições explícitas de formato ou acessibilidade.
- Usar o material fornecido e o contexto pertinente efetivamente acessível.
  Perguntar somente por lacuna que mude materialmente a escolha. Se o canal for
  desconhecido, preferir texto e listas legíveis e declarar a premissa se afetar
  o resultado. Se faltar conteúdo indispensável, pedir apenas esse material;
  não inventar dados para preencher uma estrutura.

## Procedimento

1. Confirmar pedido explícito desta seleção ou etapa nomeada no workflow
   autorizado. Não inferir autorização de palavras presentes em citações nem
   analisar o formato de toda resposta. Sem o gatilho, encerrar esta análise e
   atender ao pedido original. Se o formato já estiver fixado, respeitá-lo sem
   abrir seleção; só reavaliar mediante pedido explícito de reconsideração.
2. Identificar a ação principal: comparar valores, executar passos, compreender
   relações, acompanhar tempo ou ler uma argumentação. Registrar apenas os
   requisitos observáveis que influem na escolha, sem pedir deliberação interna
   privada. Reconhecer necessidades secundárias sem multiplicar formatos.
3. Comparar opções pelo ganho para essa ação e pelo suporte do canal. Usar as
   correspondências abaixo como critérios condicionais, sem aplicação mecânica:

   | Tarefa do leitor | Formato candidato | Critério decisivo |
   | --- | --- | --- |
   | Entender fato ou argumento | Frase ou parágrafos | Preservar condições e encadeamento lógico |
   | Comparar diferenças exatas | Tabela | Usar critérios comuns, unidades e células equivalentes |
   | Executar ou conferir etapas | Lista numerada ou checklist | Expor ordem, condições e conclusão observável |
   | Entender relações ou ramificações | Diagrama | Tornar relações mais claras que o texto, com suporte real do meio |
   | Acompanhar datas e duração | Cronologia, tabela temporal ou gráfico | Preservar datas, unidades, sobreposições e dependências existentes |
   | Copiar instruções técnicas | Bloco de código ou diff | Preservar sintaxe, contexto e possibilidade de uso correto |
   | Consultar, imprimir ou compartilhar material extenso | Documento estruturado | Oferecer navegação e suporte ao destino final |

4. Escolher a menor combinação suficiente. Evitar tabela para conteúdo sem
   comparação, diagrama decorativo, duplicação integral e arquivo sem finalidade.
   Não confundir formato com ferramenta: selecionar a representação sem presumir
   acesso a aplicativos ou iniciar outra meta-skill. Distinguir escolher o formato
   de desenvolver uma arquitetura extensa de documento ou reescrever tudo para
   outro público; manter o recorte autorizado.
5. Adequar ao meio e à acessibilidade. Usar títulos, rótulos e ordem de leitura
   claros; não transmitir distinções apenas por cor, ícone, posição ou imagem.
   Evitar tabelas largas em telas estreitas; dar equivalente textual a relações
   visuais essenciais. Se o meio não renderizar a opção, entregar alternativa
   legível que conserve os mesmos dados, relações, sequência e condições, como
   lista de relações rotuladas ou blocos por item. Não despejar marcação
   incompatível como se fosse visual renderizado. Se um formato fixado pelo
   usuário for inviável no meio, explicar a limitação e oferecer equivalente,
   sem alegar que o formato solicitado foi entregue.
6. Montar estrutura inicial com os itens reais: cabeçalhos e linhas relevantes,
   etapas concretas, relações rotuladas, ordem temporal ou início de argumento.
   Marcar lacunas como não informadas; não preencher com valores presumidos.
   Explicar a escolha em uma ou duas frases ligadas à tarefa e ao canal.

## Adaptação ao Codex

Respeitar instruções do projeto, caminhos e símbolos reais quando disponíveis.
Escolher entre explicação, tabela de contratos, passos, trecho de código ou diff
conforme o uso pretendido. Distinguir pseudocódigo, código proposto e execução
observada; não alterar implementação nem executar comandos só para escolher
formato. Usar apenas capacidades e permissões reais, sem presumir pesquisa,
memória, agentes, renderização ou testes.

## Entrega

Entregar formato recomendado, justificativa breve e estrutura inicial já
adequada ao conteúdo real. Acrescentar alternativa equivalente apenas quando
houver limitação relevante de canal ou acessibilidade. Integrar esses elementos
à escala do pedido, sem impor relatório ou matriz de pontuação.

## Verificação

Conferir autorização, preferência explícita, suporte do meio e ganho informacional.
Comparar a estrutura com a entrada para preservar valores, unidades, ressalvas,
relações e ordem. Em tabelas, manter critérios consistentes e distinguir ausência
de dado de ausência de recurso. Confirmar legibilidade sem depender de cor ou
renderização indisponível. Informar se o suporte foi observado ou apenas assumido;
não afirmar testes de renderização ou roteamento que não ocorreram.

## Condição de parada

Encerrar ao entregar escolha suficiente e estrutura utilizável, com limitações
materiais identificadas. Se faltar material decisivo, parar apenas essa parte e
solicitar o mínimo necessário. Não chamar outras meta-skills automaticamente,
criar visual ou documento completo por implicação nem iniciar pesquisa,
publicação ou alteração externa fora do escopo autorizado.
