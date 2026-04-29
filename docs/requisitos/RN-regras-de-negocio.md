---
id: RN
tipo: Regras de Negócio
projeto: DevNotes Local
versao: 1.0
status: aprovado
fonte: prompts/05_R_Prompt_Refinado_do_Levantamento_e_Análise_de_Requisitos.md
---

# Regras de Negócio — DevNotes Local

## Rastreabilidade

| Work Item | Arquivo |
|---|---|
| Feature | [FEAT-001](../features/FEAT-001-devnotes-local-mvp.md) |
| User Story | [US-001](../us/US-001-gerenciar-conteudos-tecnicos-locais.md) |
| Req. Funcionais | [RF](./RF-requisitos-funcionais.md) |

---

## Tabela de Regras de Negócio

| ID     | Regra                                    | Descrição                                                                                                                       |
| ------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| RN-001 | Upload único por operação                | O sistema deve permitir o envio de apenas um arquivo por vez no MVP.                                                            |
| RN-002 | Limite máximo de upload                  | O arquivo enviado não pode ultrapassar 12 MB.                                                                                   |
| RN-003 | Extensões permitidas                     | Somente arquivos com extensões configuradas como permitidas poderão ser enviados.                                               |
| RN-004 | Lista inicial de extensões               | O MVP deve aceitar `.py`, `.java`, `.sql`, `.md`, `.txt`, `.srw`, `.sru`, `.srd`, `.srm`, `.srf`, `.sra` e `.srs`.              |
| RN-005 | PowerBuilder como linguagem única        | Arquivos PowerBuilder devem ser classificados com linguagem `PowerBuilder`, independentemente da extensão específica.           |
| RN-006 | Tipo de objeto PowerBuilder por extensão | O tipo do objeto PowerBuilder deve ser identificado automaticamente pela extensão do arquivo.                                   |
| RN-007 | Mapeamento `.srw`                        | Arquivos `.srw` devem ser classificados como `PowerBuilder Window`.                                                             |
| RN-008 | Mapeamento `.sru`                        | Arquivos `.sru` devem ser classificados como `PowerBuilder User Object`.                                                        |
| RN-009 | Mapeamento `.srd`                        | Arquivos `.srd` devem ser classificados como `PowerBuilder DataWindow`.                                                         |
| RN-010 | Mapeamento `.srm`                        | Arquivos `.srm` devem ser classificados como `PowerBuilder Menu`.                                                               |
| RN-011 | Mapeamento `.srf`                        | Arquivos `.srf` devem ser classificados como `PowerBuilder Function`.                                                           |
| RN-012 | Mapeamento `.sra`                        | Arquivos `.sra` devem ser classificados como `PowerBuilder Application`.                                                        |
| RN-013 | Mapeamento `.srs`                        | Arquivos `.srs` devem ser classificados como `PowerBuilder Structure`.                                                          |
| RN-014 | Fallback de encoding                     | Ao ler arquivos enviados, o sistema deve tentar `utf-8`; se falhar, tentar `latin-1`; se falhar, tentar `cp1252`.               |
| RN-015 | Conteúdo pesquisável                     | Todo conteúdo cadastrado manualmente ou extraído de arquivo deve ser registrado no SQLite e indexado para busca textual.        |
| RN-016 | Marcação de regra de negócio             | Um conteúdo pode ser marcado como regra de negócio, permitindo filtro e identificação diferenciada.                             |
| RN-017 | Regras de negócio exigem classificação   | Conteúdos marcados como regra de negócio devem permitir associação a sistema e domínio.                                         |
| RN-018 | Configuração centralizada                | Sistemas, domínios, linguagens, extensões aceitas, tipos de objeto e tags pré-cadastradas devem ser definidos no `config.yaml`. |
| RN-019 | Busca textual com filtros                | A busca deve permitir texto livre e filtros complementares por metadados.                                                       |
| RN-020 | Visualização formatada                   | Conteúdos técnicos devem ser exibidos usando estrutura HTML que preserve formatação, especialmente `<pre><code>`.               |
