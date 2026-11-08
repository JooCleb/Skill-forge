---
name: problem-set-generator
description: >-
  Gere listas de exercícios progressivos por nível e corrija tentativas de uma
  lista já criada, sem antecipar respostas, no ChatGPT Work ou no Codex quando
  o tema envolver código. Use em pedidos de prática com enunciados, objetivos,
  critérios e pistas graduais. Não use para pedido direto de solução integral,
  prova de avaliação sigilosa, planejamento de currículo completo, aula
  expositiva ou simples revisão textual. Se o usuário pedir a solução completa
  durante a prática, respeite esse pedido sem exigir tentativa prévia.
---

# problem-set-generator

## Entradas e escopo

- Identificar tema, objetivo de aprendizagem, pré-requisitos, nível, quantidade,
  restrições e materiais disponíveis. Para correção, recuperar o enunciado exato,
  a tentativa e as pistas já dadas no contexto acessível.
- Inferir informações pelo contexto e explicitar suposições brevemente. Na falta
  de quantidade, escolher um conjunto curto suficiente para o objetivo. Perguntar
  apenas o que altere materialmente a tarefa; pedir enunciado ou tentativa ausente
  quando necessário, sem inventar conteúdo de outras conversas.
- Aplicar o fluxo somente à parte de prática do pedido. Diante de uma exclusão,
  seguir o pedido pertinente fora deste fluxo, sem impor retenção de respostas
  nem transformar a exclusão em uma proibição geral de ajudar.

## Procedimento

1. **Planejar a progressão.** Definir objetivos observáveis e distribuir o
   conjunto entre compreensão, aplicação, transferência para contexto novo e
   casos difíceis ou limites. Aumentar a exigência de raciocínio, integração ou
   autonomia, não apenas trocar números. Respeitar o nível e os pré-requisitos;
   em listas curtas, combinar dimensões sem forçar quatro blocos artificiais.
2. **Verificar antes de entregar.** Resolver ou conferir cada item sem publicar
   a resolução. Checar dados suficientes, hipóteses, domínio, unidades, critérios,
   casos-limite e existência de solução. Declarar se são esperadas uma, várias
   ou todas as soluções, ou uma justificativa aberta. Se houver alternativas
   válidas, aceitá-las ou reformular antes da entrega. Em tarefas abertas,
   verificar que os critérios sejam satisfazíveis, sem inventar resposta única.
3. **Preparar apenas o material do aluno.** Entregar enunciados e critérios com
   dificuldade e objetivo por item. Informar pré-requisitos e condições de
   execução necessários, sem exemplos resolvidos nem pistas não solicitadas.
   Não incluir gabarito em texto, comentários, spoilers, anexos, metadados,
   campos de widgets, testes, arquivos auxiliares, links ou histórico de commits
   entregue ao aluno. Evitar que um item ou critério revele a resposta de outro.
   Manter a verificação separada dos materiais iniciais; preferir conferência
   interna quando ferramentas ou arquivos visíveis revelariam a resposta.
4. **Corrigir a tentativa.** Avaliar somente os itens enviados contra o enunciado
   original. Apontar acertos concretos e o primeiro erro que comprometa a solução,
   com evidência localizada e explicação breve; não despejar a resolução restante.
   Distinguir erro conceitual, cálculo, implementação e apresentação. Aceitar
   métodos alternativos válidos; não exigir a forma imaginada ao criar a lista.
   Se faltar justificativa exigida, pedir esse trecho em vez de presumir erro.
5. **Tratar ambiguidades com justiça.** Antes de reprovar, conferir se o enunciado
   permite a interpretação usada. Reconhecer as respostas válidas, explicar a
   ambiguidade e propor uma redação inequívoca para próximas tentativas. Não impor
   retroativamente uma condição nem penalizar uma solução válida. Corrigir
   abertamente erro no próprio enunciado ou na referência de correção.
6. **Graduar a ajuda.** Oferecer uma pista por rodada: primeiro o conceito, depois
   uma indicação localizada, por fim um subpasso parcial. Adaptar ao bloqueio e às
   pistas anteriores; não entregar toda a sequência de uma vez. Quando houver
   pedido de solução completa, fornecê-la para o escopo solicitado, mesmo sem
   tentativa prévia, preservando as respostas dos demais itens. Se a tentativa
   estiver correta, confirmar com evidência breve, sem inventar falha ou pista.
7. **Escolher o próximo passo.** Indicar o próximo item adequado: retomar o atual
   com a pista, praticar uma lacuna específica ou avançar para transferência e
   casos difíceis. Basear a escolha no desempenho observado, sem criar currículo,
   calendário de revisões ou uma nova lista extensa sem pedido.

## Adaptação a código

- Especificar linguagem/versão quando afetar a solução, assinaturas, entradas,
  saídas, restrições e comportamento nos limites. Fornecer trechos completos para
  análise ou esqueletos claramente marcados como incompletos; separar defeitos
  intencionais de omissões acidentais.
- Em C, verificar inicialização, tipos, limites, tempo de vida, ponteiros nulos,
  aliasing e responsabilidade pela memória conforme o objetivo. Não exigir uma
  saída única de código com comportamento indefinido; se esse for o assunto,
  pedir identificação e justificativa do problema.
- Usar compilador, testes ou análise disponíveis quando trouxerem evidência útil
  e não vazarem respostas. Usar dados sintéticos e ambiente de validação isolado;
  não sobrescrever a tentativa nem alterar o projeto para efetuar a correção.
  Não prometer ambiente oculto, acesso ou execução inexistentes. Se não executar,
  classificar a conferência como inspeção ou simulação. Em correção, revelar
  apenas a evidência necessária para o item trabalhado.

## Entrega

- **Lista inicial:** numerar os itens e indicar dificuldade relativa ao nível,
  objetivo, enunciado e critérios verificáveis de uma resposta satisfatória.
  Critérios devem avaliar propriedades, sem conter resultado, algoritmo pronto
  ou sequência que resolva o item. Não anexar soluções de conferência.
- **Correção por item:** apresentar estado (correto, parcial, incorreto ou
  enunciado ambíguo), acertos, primeira falha relevante quando houver, uma pista
  adequada quando necessária e próximo passo. Informar limitações que afetem o
  julgamento. Não atribuir nota nem peso que não tenham sido estabelecidos.
- **Solução solicitada:** apresentar resolução completa e explicada apenas dos
  itens pedidos, com verificação apropriada e sem exigir etapas pedagógicas extras.

## Verificação e parada

Antes de responder, conferir alinhamento com objetivos e pré-requisitos,
progressão real, validade dos enunciados, alternativas legítimas e ausência de
respostas nos materiais iniciais, inclusive arquivos e conteúdo técnico enviado.
Distinguir inspeção, simulação e testes realmente executados; não afirmar
roteamento automático, memória persistente ou validação independente sem evidência.

Encerrar após entregar a lista verificada e aguardar as tentativas. Na correção,
encerrar após o retorno dos itens enviados e um próximo passo adequado; não
responder em nome do aluno nem revelar os itens seguintes. Parar o item afetado
para obter um dado indispensável ou corrigir sua formulação quando não for
possível avaliá-lo com justiça; continuar apenas as partes independentes.
