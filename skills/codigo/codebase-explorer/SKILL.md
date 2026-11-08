---
name: codebase-explorer
description: >-
  Produza um mapa verificável de um repositório desconhecido no ChatGPT Work
  ou no Codex quando houver código. Use em pedidos de compreender arquitetura,
  entradas, módulos, dependências, integrações e fluxos de funcionamento de
  um repositório ou subsistema amplo. Não use para explicar uma linha ou função
  isolada, corrigir um erro pontual, refatorar sem exploração ampla ou realizar
  auditoria especializada de segurança ou de qualidade.
---

# codebase-explorer

Mapeie o que as fontes permitem demonstrar, sem modificar o projeto.

## Entradas

- Identifique a origem acessível: pasta local, repositório conectado ou arquivos fornecidos; registre raiz, revisão/branch quando disponíveis e limites de acesso.
- Use o foco informado. Na falta dele, escolha de um a três fluxos representativos a partir das entradas reais. Em monorepos, delimite os pacotes analisados.
- Peça somente acesso ou esclarecimento que mude materialmente a análise. Sem código acessível, informe o impedimento e solicite a fonte; não invente um mapa.

## Procedimento

1. **Estabeleça contexto.** Leia instruções aplicáveis, como `AGENTS.md`, documentação de entrada, manifestos, arquivos de versões fixadas, tarefas e configurações de CI. Resolva divergências entre documentação e implementação pelas evidências, sem ocultá-las. Com checkout e terminal, registre o estado inicial sem alterar branch ou arquivos.
2. **Localize a estrutura.** Faça buscas direcionadas por entradas, módulos, testes, configurações e integrações. Com terminal, prefira `rg --files` e `rg -n`; em conectores, use busca e leitura disponíveis. Não pressuponha terminal, rede, credenciais ou agentes. Evite varrer dependências vendorizadas, saídas de compilação e arquivos gerados; inspecione-os quando sustentarem uma relação relevante. Examine configurações de exemplo sem expor valores secretos.
3. **Comprove responsabilidades.** Relacione pastas/pacotes a símbolos, registros de rotas, comandos, consumidores, imports e configurações efetivamente lidos. Separe dependências internas, externas e de desenvolvimento; diferencie declaração em manifesto, uso encontrado e disponibilidade no ambiente.
4. **Rastreie fluxos.** Siga uma entrada até armazenamento, integração externa ou saída, incluindo o retorno quando relevante. Confira cada ligação por chamada, registro, injeção, evento ou configuração: entrada → validação/autorização → regra → acesso a dados/integração → saída, somente onde essas etapas existirem. Cite caminhos e símbolos reais; confira esquema/consulta quando houver banco. Marque saltos não resolvidos e ligações inferidas; não preencha lacunas por convenções do framework. Localize testes ligados ao fluxo sem tratar sua existência como execução.
5. **Classifique com evidências.** Indique código ativo por ligações às entradas/configurações, gerado por marcador ou gerador identificado, legado por evidência de substituição/descontinuação e não confirmado quando faltar suporte. Esses estados podem se sobrepor: código gerado pode estar ativo. Nome de pasta, idade ou ausência de referências em uma busca não provam desuso. Ativo por leitura não significa executado.
6. **Verifique apenas o necessário.** Antes de executar, leia o comando, seus scripts/hooks e dependências imediatas para avaliar efeitos. Execute somente verificações pertinentes, disponíveis, isoladas e sem alteração do projeto ou de sistemas externos; mantenha saídas temporárias fora do projeto. Não instale dependências, gere artefatos no checkout, rode migrações, faça deploy ou inicie serviços externos para completar o mapa. Se não puder garantir uma verificação segura, registre-a como não executada e prossiga por leitura. Diante de serviço indisponível, preserve o mapa possível e delimite o que não foi verificado em execução; não simule sucesso.

## Entrega

Adapte a extensão ao escopo; inclua:

- **Escopo e mapa:** origem/revisão e tabela de pasta ou módulo, responsabilidade, evidência e estado.
- **Fluxos principais:** percurso com caminhos e símbolos por ligação, armazenamento/saída e lacunas. Use diagrama somente se esclarecer relações; mantenha evidências próximas ao texto ou diagrama.
- **Dependências e integrações:** finalidade, ponto de uso e configuração pertinente, sem segredos.
- **Comandos de desenvolvimento:** comando exato, diretório, finalidade, fonte e pré-requisitos conhecidos. Distinga “confirmado na configuração/documentação; não executado” de “executado”, com resultado observado. Não invente comandos usuais da stack.
- **Pontos de atenção:** divergências, dependências bloqueantes e incertezas com evidência e impacto no entendimento. Não transforme a exploração em refatoração ou auditoria não solicitada.

Para cada afirmação material, associe caminho real e símbolo/seção; acrescente linha ou permalink da revisão somente quando observado. Diferencie **observado no código/configuração**, **inferido por leitura** e **verificado em execução**; uma verificação parcial não comprova o fluxo completo.

## Verificação

Antes de entregar, confira caminhos, símbolos e ligações contra as fontes lidas. Revise se os fluxos alcançam uma saída ou um limite explícito, se os comandos têm fonte e estado, e se as classificações estão sustentadas. Registre verificações realmente realizadas, resultados e limitações. Havendo checkout, compare o estado final ao inicial; preserve alterações preexistentes e não use limpeza ou restauração para ocultar diferenças. Não afirme integridade verificada se não a conferiu.

## Condição de parada

Encerre quando o escopo escolhido tiver responsabilidades, fluxos, dependências e comandos sustentados, com lacunas explícitas. Pare também diante de acesso insuficiente ou bloqueio que impeça aprofundamento seguro, entregando o mapa parcial e a informação mínima necessária para prosseguir. Não explore indefinidamente, altere o projeto ou resolva os pontos de atenção por iniciativa desta skill.
