---
id: R
tipo: Registro de Riscos
projeto: DevNotes Local
versao: 1.0
status: ativo
fonte: prompts/05_R_Prompt_Refinado_do_Levantamento_e_Análise_de_Requisitos.md
---

# Registro de Riscos — DevNotes Local

## Rastreabilidade

| Work Item | Arquivo |
|---|---|
| Feature | [FEAT-001](../features/FEAT-001-devnotes-local-mvp.md) |
| Req. Funcionais | [RF](../requisitos/RF-requisitos-funcionais.md) |
| Req. Não Funcionais | [RNF](../requisitos/RNF-requisitos-nao-funcionais.md) |

---

## Tabela de Riscos

| ID    | Risco / Ponto de atenção             | Impacto                                                                        | Mitigação sugerida                                                                |
| ----- | ------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| R-001 | Encoding de arquivos legados         | Arquivos PowerBuilder podem não estar em UTF-8 e falhar na leitura.            | Implementar fallback `utf-8`, `latin-1`, `cp1252`.                                |
| R-002 | Busca com SQLite FTS5                | FTS5 exige cuidado na criação, atualização e remoção do índice.                | Testar cadastro, edição, exclusão e busca.                                        |
| R-003 | Preservação de formatação            | Conteúdos técnicos perdem valor se indentação e quebras forem alteradas.       | Exibir sempre com `<pre><code>`.                                                  |
| R-004 | Escopo excessivo                     | O projeto pode crescer demais e perder o caráter didático do MVP.              | Manter fora do MVP autenticação, produção, backup e frontend sofisticado.         |
| R-005 | Upload de arquivos inadequados       | Usuário pode enviar arquivos binários ou extensões indevidas.                  | Validar extensão e tamanho antes de processar.                                    |
| R-006 | Classificação automática incompleta  | Nem toda extensão permite inferir domínio, sistema ou categoria.               | Inferir apenas o que for seguro; permitir ajuste manual.                          |
| R-007 | Highlight.js com linguagem incorreta | Destaque pode ficar ruim se linguagem for mal definida.                        | Permitir linguagem padrão ou genérica.                                            |
| R-008 | Configuração inconsistente           | `config.yaml` pode conter listas incompletas ou mapeamentos inválidos.         | Validar configuração no início da aplicação.                                      |
| R-009 | Exclusão acidental                   | Usuário pode apagar conteúdo importante.                                       | Solicitar confirmação antes da exclusão.                                          |
| R-010 | Testes negligenciados                | MVP didático pode acabar sem testes úteis.                                     | Criar testes para regras principais: upload, extensão, tamanho, encoding e busca. |
| R-011 | Arquivos grandes dentro do limite    | Mesmo abaixo de 12 MB, arquivos podem gerar conteúdo grande para visualização. | Usar visualização simples e considerar rolagem no bloco de conteúdo.              |
| R-012 | Acoplamento entre regras e interface | Regras de validação podem ficar presas nos templates.                          | Concentrar validações no backend.                                                 |
