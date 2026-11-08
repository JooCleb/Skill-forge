# Como contribuir

1. Confira o [catálogo](CATALOGO.md), a documentação e o escopo antes de criar uma skill ou alterar uma existente. Não considere a categoria um selo de qualidade.
2. Mantenha cada skill em `skills/<área>/<nome-da-skill>/`, com `SKILL.md` e seus recursos necessários. Preserve o nome no frontmatter e o da pasta. O README e os registros de avaliação para humanos podem ficar fora do pacote da skill, em `docs/` ou `evaluations/`.
3. Para uma skill nova ou mudança de comportamento, defina casos positivos, negativos e de fronteira; registre ambiente, data, resultado e limitações quando os executar. Não marque um caso planejado como executado.
4. Para uma mudança de escopo, fusão, divisão ou descontinuação, comece pelo [modelo de proposta](templates/refactor-proposal.md). Preserve fontes, justificativa e compatibilidade quando pertinente.
5. Execute os comandos do README, regenere `CATALOGO.md` se nome, descrição ou localização mudar e revise o diff. Os avisos do lint são sugestões, não uma avaliação semântica.
6. Descreva o que mudou, por quê, como foi verificado e o que permanece sem validação. Não inclua credenciais, dados pessoais alheios ou resultados fictícios.

Copiar ou editar este repositório não instala nem atualiza automaticamente as skills pessoais em outros ambientes. Siga o mecanismo de instalação vigente do destino.
