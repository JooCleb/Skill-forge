---
name: document-architect
description: >-
  Projete a estrutura de documentos a partir de notas e objetivos no ChatGPT Work
  ou, com material de código, no Codex. Use em pedidos de sumário comentado,
  arquitetura de capítulos ou plano de organização de material extenso antes
  da redação. Não use para reescrita integral imediata, correção gramatical ou
  reorganização curta já delimitada cujo resultado seja o próprio texto revisado.
---

# document-architect

Projetar um documento redigível, com progressão clara e cobertura rastreável das notas. Limitar a entrega à arquitetura; distinguir esse trabalho da reorganização que já entrega texto pronto para estudo.

## Entradas

- Identificar finalidade, público, gênero, extensão aproximada, conteúdo obrigatório e restrições de formato ou ordem.
- Usar as notas e fontes fornecidas ou acessíveis por capacidades autorizadas. Registrar material indisponível sem presumir sua leitura.
- Perguntar apenas pelo que mudar materialmente a estrutura e não puder ser recuperado do contexto. Nos demais pontos, declarar premissas ajustáveis e avançar; não impor questionário.

## Procedimento

1. **Inventariar.** Atribuir identificadores estáveis às unidades de informação, como N01 e N02. Registrar origem recuperável (arquivo e seção, página, bloco ou trecho identificável), conteúdo essencial e função: definição, argumento, evidência, método, resultado, exemplo, ressalva ou referência. Para notas coladas sem localização, usar o identificador e um trecho distintivo; não inventar páginas ou links. Separar conteúdos distintos de uma mesma nota quando tiverem destinos diferentes.
2. **Agrupar.** Escolher progressão conceitual, argumentativa, cronológica ou operacional conforme o objetivo e o público. Preservar modelos obrigatórios. Unir apenas divisões redundantes da estrutura, mantendo todas as informações, nuances, exemplos e origens; notas parecidas não são automaticamente duplicatas. Sinalizar conflitos sem escolher uma versão sem evidência.
3. **Projetar.** Definir títulos informativos e somente os níveis de hierarquia necessários. Para cada seção, indicar a pergunta respondida, sua função no documento, conteúdo previsto e pré-requisitos de leitura, que devem estar apresentados antes. Distinguir esses pré-requisitos de remissões e da ordem de redação: uma síntese pode ser escrita por último e lida primeiro. Se duas seções dependerem uma da outra, antecipar a base comum ou reordenar/dividir o conteúdo até eliminar o ciclo. Evitar repetir explicações em vários capítulos; usar remissões quando necessário.
4. **Acomodar exceções.** Se uma nota relevante não couber, revisar agrupamentos, criar seção ou justificar apêndice com chamada no corpo. Manter evidência ou ressalva essencial junto do argumento correspondente; não usar apêndice como depósito. Preservar notas de pertinência incerta com status explícito e decisão pendente, sem descartá-las silenciosamente.
5. **Mapear e orientar.** Vincular cada unidade inventariada a uma seção ou apêndice; registrar remissões e destinos compartilhados sem perder proveniência. Listar lacunas de informação, evidência ou ligação entre ideias e indicar onde afetam a redação. Distinguir o que já existe do que ainda precisa ser produzido; não preencher lacunas com fatos inventados.

## Entrega

Entregar, na escala adequada ao material:

- **Premissas de projeto:** finalidade, público, extensão e restrições confirmadas ou assumidas.
- **Sumário comentado:** ordem, pergunta, função, conteúdo e dependências de cada seção; sugerir distribuição aproximada da extensão quando houver orçamento útil.
- **Mapa origem–destino:** tabela com `ID | origem e conteúdo essencial | função | destino | status/observação`. Cobrir cada nota; permitir agrupamentos por IDs apenas quando o destino de todas continuar inequívoco. Identificar divisões ou fusões estruturais relevantes.
- **Lacunas e orientação de redação:** indicar prioridades, evidências faltantes, transições e decisões pendentes. Orientar como desenvolver as seções sem redigi-las integralmente.

## Adaptação ao Codex

Quando o documento depender de código, consultar apenas arquivos pertinentes disponíveis, respeitar instruções do projeto e usar caminhos e símbolos reais como origens. Separar comportamento observado, proposto e não verificado. Projetar a documentação sem implementar código, executar testes de software ou alterar arquivos-fonte por implicação.

## Verificação e parada

Conferir o inventário contra o mapa: nenhuma nota pode desaparecer; toda nota relevante deve ter destino efetivo. Verificar conteúdo obrigatório, distinção entre fatos e lacunas, dependências sem circularidade e hierarquia proporcional. Registrar limitações de acesso e decisões que ainda impeçam fechar a arquitetura.

Encerrar após entregar o projeto estrutural e suas pendências. Redigir o documento, pesquisar para suprir lacunas ou modificar o material original somente mediante pedido adicional ou autorização já explícita para essa etapa. Não acionar outras skills como dependência obrigatória.
