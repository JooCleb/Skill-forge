---
name: test-designer
description: >-
  Use quando houver pedido de plano de testes ou de implementação de testes
  para requisitos, código ou processos fornecidos no ChatGPT Work ou no Codex.
  Não use para mudança trivial sem justificativa de novos testes, como trocar
  a cor de um título, nem para simples execução de uma suíte já existente.
---

# test-designer

Derivar testes de comportamentos esperados, riscos e invariantes. Selecionar o menor conjunto que detecte falhas relevantes; quantidade de testes e cobertura de linhas não comprovam correção.

## Entradas e escopo

- Identificar o pedido: planejar testes ou também implementá-los. Recuperar requisitos, contratos, exemplos aprovados, código e testes disponíveis, fronteiras do sistema e restrições de ambiente. Registrar origem e versão quando relevantes.
- No Work, trabalhar com materiais e ferramentas acessíveis, inclusive processos sem código. No Codex, ler instruções do repositório e convenções de teste. Não presumir arquivos, execução, acessos, dependências ou permissões.
- Pedir somente informações que mudem os casos ou seus resultados esperados; avançar nas partes independentes. Para alteração trivial ou mera execução de suíte, dispensar novo desenho e seguir o pedido com verificação proporcional.

## Procedimento

1. **Mapear o contrato.** Identificar entradas, estados, operações, saídas, efeitos, invariantes e fronteiras com dependências. Atribuir IDs aos requisitos e relacionar riscos concretos: o que poderia falhar, em qual condição e com que consequência. Não transformar detalhes internos em requisitos.
2. **Definir o oráculo antes das asserções.** Registrar como decidir o resultado: regra aprovada, exemplo de aceite, propriedade justificada ou modelo independente. Vincular cada asserção à regra que a sustenta, inclusive para saídas secundárias; nome de parâmetro e assinatura não definem sua semântica. Explicitar tolerâncias e erros esperados quando previstos. Sem regra suficiente, marcar “oráculo pendente”, formular a pergunta decisiva e suspender apenas a conclusão afetada. Código atual e testes legados mostram expectativas existentes; não os promover a especificação correta. Se caracterização for solicitada, identificá-la como registro do comportamento atual, separado da validação de correção.
3. **Escolher testes pelo risco.** Usar unitários para regras isoladas, integração para contratos entre componentes reais e ponta a ponta para fluxos críticos que exijam o sistema completo. Classificar pelo limite exercitado: simular uma dependência para isolar a unidade não transforma o teste em integração. Regressão é a finalidade de impedir o retorno de uma falha e pode ocorrer nesses níveis. Em processos sem software, selecionar ensaios manuais de aceitação. Reutilizar cobertura válida; justificar combinações, sem impor todos os tipos nem uma nova infraestrutura.
4. **Derivar casos pertinentes.** Selecionar representantes de classes de equivalência, limites internos e externos, vazio e elemento único, entradas inválidas, erros, sequências e transições de estado. Considerar falhas de dependências e recuperação quando fizerem parte do risco. Em uma lista em C, incluir falha controlada de alocação e invariantes após operações sucessivas; definir preservação de estado e retornos conforme o contrato, sem inventá-los.
5. **Tornar cada caso discriminante.** Especificar precondições, dados, ações, resultado esperado, oráculo e limpeza. Nomear o defeito que o caso detectaria. Verificar comportamento e invariantes contratados, evitando reproduzir o algoritmo ou conferir apenas chamadas de mocks. Controlar fixtures, relógio, aleatoriedade e recursos quando necessário; isolar dependências nas fronteiras sem substituir a própria unidade testada.
6. **Implementar somente o solicitado.** Em pedido de plano, entregar o desenho. Quando implementação estiver incluída, seguir ferramentas e convenções existentes e preservar alterações do usuário. Não modificar o produto para fazer testes passarem nem instalar infraestrutura sem necessidade e autorização. Usar dados fictícios e ambiente controlado; não acionar serviços reais como consequência do desenho.
7. **Executar e registrar com precisão.** Quando execução estiver no escopo e disponível, conferir comandos e efeitos, executar os testes pertinentes e registrar ambiente, comando, resultado e retorno. Separar defeito demonstrado, problema do teste e impedimento de infraestrutura. Se houver apenas leitura ou simulação, declarar esse método e “não executado”; apresentar saídas deduzidas como deduções, sem dizer que a suíte passou. Repetir somente verificações afetadas por mudanças ou lacunas materiais.

## Entrega

Apresentar a matriz proporcional ao pedido, preenchida com casos reais:

`ID/requisito e origem | Risco | Caso: precondições, entrada e ação | Resultado esperado e oráculo | Nível ou método | Situação e evidência`

Acrescentar testes implementados e sua localização quando houver, comandos e resultados efetivamente observados, lacunas de cobertura e oráculos pendentes. Distinguir planejado, implementado e executado; classificar a execução como passou, falhou, bloqueada ou não executada. Identificar inspeção e simulação separadamente. Não declarar todos os requisitos cobertos por uma amostra aprovada.

Exemplo de chamada: “Use @test-designer para planejar testes desta API conforme o contrato anexado; priorize os riscos e não implemente nesta etapa.”

## Verificação e parada

- Conferir rastreabilidade, oráculos anteriores às asserções, limites pertinentes, independência das fixtures e correspondência entre alegações de execução e evidências. Remover duplicações e casos sem falha relevante que possam detectar.
- Encerrar ao entregar a matriz e os testes no escopo pedido, com execução real ou limitação identificada. Sem oráculo essencial, concluir parcialmente e indicar a decisão necessária. Não ampliar para correções, auditoria geral, novos tipos de teste ou outras skills por padrão.
