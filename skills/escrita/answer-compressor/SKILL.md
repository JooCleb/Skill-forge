---
name: answer-compressor
description: >-
  Condense uma resposta no ChatGPT Work, inclusive explicações de código no Codex,
  preservando fatos, condições, ressalvas e intenção. Use somente mediante pedido
  explícito de encurtar ou condensar uma resposta mantendo o essencial, ou etapa
  nomeada dessa condensação em workflow já autorizado. Não use para aprofundar,
  revisar estilo sem pedido de redução, compactar estado operacional para retomada,
  alterar conteúdo ou posicionamento, nem refatorar ou minificar código.
---

# answer-compressor

## Entradas

- Identifique a resposta original, o público, a finalidade, o formato e o limite solicitado (palavras, caracteres, proporção ou extensão aproximada).
- Use o contexto disponível; na falta de indicação, preserve público, idioma, tom e formato do original e reduza o excesso sem impor uma porcentagem. Pergunte somente por informação ausente que mude materialmente a entrega; se faltar o original, solicite-o antes de reescrever.
- Confira se o pedido autoriza condensar a resposta. Um pedido genérico de revisão ou uma preferência habitual por brevidade não basta. Se o pedido estiver fora do escopo, não aplique esta skill nem chame outra meta-skill automaticamente.
- Se esta skill for explicitamente invocada para uma finalidade excluída, informe brevemente a incompatibilidade e encerre sem realizar a transformação. Sua mera disponibilidade não impede atender normalmente a pedidos de outro tipo.

## Procedimento

1. Separe a mensagem central, os fatos e as relações indispensáveis de repetições, introduções vazias e exemplos dispensáveis. Considere indispensável toda informação cuja retirada altere a interpretação, a decisão ou a ação do leitor.
2. Preserve números, unidades, datas, nomes, negações, exceções, condições de aplicação, atribuições, referências necessárias e graus de incerteza. Preserve também intenção, posicionamento e ênfases relevantes; não transforme possibilidade em garantia, associação em causa ou resultado restrito em regra geral.
3. Reescreva com frases diretas e agrupe ideias relacionadas. Remova exemplos somente quando não carregarem informação exclusiva necessária. Não acrescente fatos nem corrija silenciosamente o conteúdo do original.
4. Confira o tamanho na unidade pedida. Para redução proporcional, compare com o original usando a mesma unidade; trate “metade” sem unidade como aproximadamente metade das palavras. Não invente contagens exatas sem conferi-las.
5. Se o limite não comportar o essencial, entregue a menor síntese fiel que conseguir e indique brevemente que ela excede o limite para preservar as condições relevantes. Não apague ressalvas para caber, não afirme cumprimento falso nem torne a conclusão absoluta.

## Adaptação ao Codex

Ao condensar uma explicação técnica ou relato de implementação, preserve identificadores, comandos, versões, pré-condições, efeitos, riscos e distinção entre testes executados e sugeridos. Mantenha trechos de código necessários íntegros; a redução da explicação não autoriza editar arquivos, refatorar, executar comandos do projeto ou declarar validações não observadas.

## Entrega

Entregue o texto condensado no formato solicitado, pronto para uso, sem preâmbulo ou relatório de cortes. Registre somente perdas inevitáveis relevantes e restrições de tamanho não atendidas, em nota breve separada. Não enumere a remoção de redundâncias ou exemplos dispensáveis.

## Verificação

Compare o texto reduzido ao original: confirme fatos e números, alcance de negações, vínculo das condições com cada afirmação, exceções, incertezas e intenção. Confira também legibilidade, formato e tamanho. Corrija divergências antes de entregar. Baseie a verificação em trechos e diferenças observáveis; não solicite deliberação interna privada, pesquisa externa ou outras meta-skills.

## Condição de parada

Encerre quando a versão estiver fiel e no formato e tamanho pedidos, ou quando a limitação inevitável estiver indicada. Não mantenha ciclos de encurtamento sem ganho claro nem transforme a condensação em rotina para respostas futuras.
