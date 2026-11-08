# Anatomia de uma skill

Uma skill tem uma pasta própria e um `SKILL.md`. O frontmatter YAML inclui `name` e `description`; o corpo descreve o procedimento e a saída. O nome deve corresponder à pasta. A descrição serve à seleção: declare objetivo e contexto sem transformar o campo em manual completo.

```yaml
---
name: revisar-relatorio
description: Revise um relatório fornecido quanto a clareza e coerência, preservando suas conclusões.
---
```

No corpo, registre entradas necessárias, limites, passos que realmente mudam a execução, tratamento de lacunas e formato de saída quando relevante. `agents/openai.yaml` pode guardar metadados de interface do ambiente. `references/` contém detalhes consultados sob demanda; `scripts/`, operações determinísticas úteis; `assets/`, arquivos usados na entrega. Não crie essas pastas só para preencher uma estrutura.

Documentação humana e resultados podem ficar fora do pacote, neste repositório. Verifique os requisitos do ambiente de destino: o formato geral não garante que toda ferramenta citada esteja disponível.
