---
name: gerar-trilhas-de-estudo
description: Crie trilhas de estudo do básico ao avançado com prompts completos e numerados para executar em chats separados e instruções gerais de tutoria para o campo de instruções de um projeto. Use quando o usuário pedir uma sequência de prompts para aprender um assunto, uma formação completa com especializações, instruções de tutor para um projeto de estudos ou a ampliação de uma trilha existente. Não acione apenas para executar uma aula de uma sequência já pronta, responder uma dúvida ou criar um cronograma.
---

# Gerador de Trilhas de Estudo

## Resultado e preferências

Produzir, por padrão, dois arquivos Markdown em português brasileiro:

1. `Prompts_<Tema>_do_Basico_ao_Avancado.md`: escopo, mapa, sequência integral de prompts prontos para copiar, especializações e referências.
2. `Instrucoes_Gerais_Projeto_<Tema>.md`: somente o texto pronto para colar no campo de instruções do projeto, adaptado ao tema.

Gerar os prompts, não executar as aulas nem responder seus exercícios durante o planejamento. Respeitar alterações explícitas solicitadas pelo usuário. Aplicar os seguintes padrões pessoais, sem perguntar novamente:

- Construir um núcleo completo e aprofundado, seguido de trilhas de especialização.
- Incluir diagnóstico inicial; preservar os fundamentos e indicar o que pode ser revisado ou pulado conforme evidências de domínio.
- Adaptar a condução: aula inteira para temas menores; blocos interativos para temas densos.
- Esperar respostas aos exercícios; diante de erro, explicar a dificuldade, dar uma pista e permitir nova tentativa antes da resolução.
- Ajustar a quantidade de exercícios à complexidade e aos objetivos, sem quantidade fixa.
- Fazer revisões somente quando o aluno solicitar ou demonstrar dificuldade. Não programar revisões periódicas, cumulativas, espaçadas nem quizzes de recapitulação obrigatórios.
- Perguntar apenas informações que alterem significativamente o planejamento.
- Priorizar qualidade das referências, aceitando outros idiomas e materiais pagos; indicar alternativas gratuitas quando possível.

## 1. Delimitar sem burocracia

Consultar primeiro o pedido, os materiais fornecidos e o contexto relevante disponível. Não presumir nível, desempenho, acesso a ferramentas ou objetivos não estabelecidos.

Se faltar algo decisivo, perguntar de forma breve sobre o objetivo, a abrangência ambígua ou os conhecimentos prévios. Não impor questionário fixo nem perguntar disponibilidade semanal se não houver pedido de cronograma. Se houver informação suficiente, declarar as premissas e produzir a trilha.

Tratar “completo” como cobertura explícita e verificável do escopo, nunca como promessa de esgotar um campo ou garantir domínio. Distinguir núcleo, aprofundamentos, especializações e assuntos fora do recorte. Não reduzir a formação a preparação para prova ou mercado sem solicitação.

Ao receber ementa ou trilha existente, ler seu conteúdo real e mapear requisitos. Ao ampliar uma sequência, preservar IDs estáveis e indicar adições e dependências; não renumerar silenciosamente nem perder tópicos anteriores.

## 2. Fundamentar o currículo

Pesquisar fontes confiáveis antes de fechar o mapa. Combinar referências estruturantes reconhecidas com fontes primárias atuais quando o tema exigir. Preferir documentação oficial e especificações em tecnologia; livros acadêmicos e literatura científica em ciências; obras fundamentais e interpretações acadêmicas pertinentes em humanidades.

- Consultar fontes suficientes para detectar lacunas de cobertura, dependências e limitações; não impor número ornamental de referências.
- Conferir links, títulos, autores e edições ou versões quando forem citados. Não inventar capítulos, páginas, DOI, acesso integral ou consulta a um livro que apenas foi localizado.
- Separar referências efetivamente consultadas no planejamento de leituras complementares identificadas. Não apresentar recomendações bibliográficas como conteúdo lido.
- Priorizar autoridade e adequação didática. Aceitar materiais em outros idiomas e pagos sem tornar sua compra condição para acompanhar a formação.
- Usar links Markdown e dados bibliográficos portáveis nos arquivos, sem depender de identificadores internos de citações do chat.
- Se não for possível pesquisar, explicitar a limitação e distinguir propostas de fontes verificadas; não simular pesquisa.
- Instruir o futuro tutor a verificar fontes e informações instáveis durante a aula, sem fingir acesso à pesquisa feita em outro chat.

## 3. Construir a arquitetura pedagógica

Mapear dependências antes de distribuir conteúdos. Ajustar o tamanho da trilha ao assunto, sem teto arbitrário de prompts e sem inflar a sequência com variações redundantes.

Organizar:

1. **Diagnóstico inicial:** avaliar pré-requisitos e raciocínio com tarefas representativas, sem gabarito antecipado. Usar o resultado para sugerir percurso, não para excluir fundamentos do arquivo.
2. **Fundamentos:** linguagem, conceitos, modelos e pré-requisitos necessários.
3. **Desenvolvimento:** mecanismos, técnicas, aplicações e relações entre tópicos.
4. **Núcleo avançado:** problemas complexos, condições, limites, decisões e integração de conhecimentos.
5. **Especializações:** ramos relevantes com objetivos, pré-requisitos e prompts efetivamente escritos, não apenas nomes ou sugestões vagas.

Apresentar tabela de módulos e prompts com ID, título, objetivos observáveis, nível, dependências e classificação (núcleo/especialização). Numerar os prompts de forma inequívoca, inclusive em ramificações. Indicar rotas possíveis sem impor que todas as especializações sejam cursadas em série.

Distribuir conceitos, ideias, importância, uso, aplicabilidade, exemplos, exercícios, erros comuns e limites ao longo do currículo. Adaptar a distribuição ao domínio; não repetir mecanicamente todos os itens em cada aula.

Incluir práticas, análises de casos ou projetos integradores quando acrescentarem competências específicas ao tema. Não disfarçar revisão periódica como projeto obrigatório; não impor software, laboratórios pagos ou aplicações artificiais. Explicitar requisitos materiais e alternativas viáveis.

## 4. Escrever cada prompt por inteiro

Ler `references/modelos.md` antes de redigir os entregáveis. Preencher os modelos com conteúdo específico: não entregar placeholders, somente títulos de aulas ou comandos genéricos como “explique tudo sobre X”.

Cada prompt deve conter:

- ID, assunto e posição na trilha;
- contexto mínimo e pré-requisitos explícitos, sem pressupor memória de chats anteriores;
- objetivos verificáveis e escopo concreto, incluindo subtemas e limites;
- orientação de profundidade e pontos de raciocínio que precisam ser desenvolvidos;
- exemplos e aplicações relevantes àquela aula;
- atividades apropriadas aos objetivos, com dificuldade progressiva e volume adaptável;
- modo de interação e regra de não revelar respostas antes da tentativa;
- orientação sobre fontes adequadas ao tópico e atualização quando necessária.

Concentrar regras gerais nas instruções do projeto, mas repetir em cada prompt as salvaguardas essenciais de contexto, ritmo e exercícios. O prompt deve funcionar em um novo chat sem depender da disponibilidade de outras skills.

Para assuntos densos, solicitar panorama breve e execução apenas do primeiro bloco, com pausa em um ponto pedagogicamente útil. Não mandar entregar toda a aula e esperar entre blocos ao mesmo tempo. Para temas menores, permitir explicação completa seguida de exercícios e pausa.

Não considerar a aula anterior concluída apenas por estar numerada antes. Quando necessário, pedir um breve registro de continuidade fornecido pelo aluno; não alegar acesso garantido aos demais chats. Se o usuário pedir “faça o prompt N”, orientar a localizar o prompt no arquivo disponível; se não estiver acessível, pedir o trecho em vez de inventar seu conteúdo.

## 5. Redigir as instruções gerais do tutor

Adaptar o modelo em `references/modelos.md` ao assunto, incorporando os princípios de Escrita Aprofundada e Didática sem depender da invocação dessa skill. Manter as instruções compactas o suficiente para serem utilizáveis no campo do projeto. Se houver limite de caracteres informado, cumpri-lo e conferir a contagem; não afirmar um limite da plataforma sem verificar.

Preservar sobretudo:

- rigor, clareza, mecanismos, condições e limites, evitando superficialidade e repetição;
- exemplos resolvidos distintos dos exercícios que o aluno deve tentar;
- avaliação tanto da conclusão quanto da justificativa, sem concordância automática;
- pistas graduais e nova tentativa após erro; solução completa quando solicitada, quando o aluno desistir ou depois de tentativa adicional acompanhada de feedback, sem prolongar artificialmente a interação;
- proteção das questões ainda não respondidas: corrigir apenas as tentadas, sem publicar o gabarito restante;
- revisão somente sob demanda ou dificuldade observada;
- autonomia do aluno para pedir explicação direta, solução ou avanço;
- ausência de promessa de memória entre chats ou de domínio sem evidências.

## 6. Auditar e entregar

Antes de salvar, conferir:

- Todos os tópicos centrais mapeados estão cobertos, com dependências anteriores ou declaradas?
- As especializações têm prompts completos e um percurso inteligível?
- Os IDs são únicos, sem referências quebradas, conteúdo truncado ou placeholders?
- Os prompts são específicos, executáveis em chats separados e coerentes com as instruções gerais?
- O diagnóstico e os exercícios preservam a espera, as pistas e as respostas ainda não tentadas?
- A regra pessoal de não programar revisões foi preservada em ambos os arquivos?
- As fontes são identificáveis, honestamente descritas e relevantes?
- A extensão reflete necessidade pedagógica, não número arbitrário de aulas?

Salvar os dois arquivos usando o mecanismo de persistência de artefatos disponível, seguindo a skill de Library quando aplicável. Trabalhar em etapas internamente se a trilha for extensa, mas finalizar os arquivos completos sem substituir o restante por “continue” ou “adicione mais tópicos”. Se houver impedimento real, delimitar o que falta e não chamar o material parcial de completo.

Responder brevemente com os arquivos, o escopo e a ordem de uso: colar as instruções gerais no projeto, disponibilizar a sequência ao projeto e executar um prompt por chat, começando pelo diagnóstico. Não iniciar a aula sem pedido.
