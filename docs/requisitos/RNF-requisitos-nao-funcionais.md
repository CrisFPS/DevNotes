---
id: RNF
tipo: Requisitos Não Funcionais
projeto: DevNotes Local
versao: 1.0
status: aprovado
fonte: prompts/05_R_Prompt_Refinado_do_Levantamento_e_Análise_de_Requisitos.md
---

# Requisitos Não Funcionais — DevNotes Local

## Rastreabilidade

| Work Item | Arquivo |
|---|---|
| Feature | [FEAT-001](../features/FEAT-001-devnotes-local-mvp.md) |
| Req. Funcionais | [RF](./RF-requisitos-funcionais.md) |
| Regras de Negócio | [RN](./RN-regras-de-negocio.md) |

---

## Tabela de Requisitos Não Funcionais

| ID      | Requisito                            | Descrição                                                                                            | Prioridade  | Observações                                                            |
| ------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------- |
| RNF-001 | Simplicidade                         | A aplicação deve ser simples, objetiva e adequada ao escopo de estudo.                               | Obrigatória | Evitar complexidade desnecessária.                                     |
| RNF-002 | Uso local                            | O sistema deve funcionar localmente, sem necessidade de publicação em servidor externo.              | Obrigatória | Deve rodar na máquina do usuário.                                      |
| RNF-003 | Baixa complexidade arquitetural      | O MVP não deve usar microsserviços, mensageria, cloud ou arquitetura distribuída.                    | Obrigatória | Manter foco didático.                                                  |
| RNF-004 | Desempenho adequado                  | A busca e a navegação devem ter desempenho aceitável para uma base local pequena ou média.           | Obrigatória | Não há exigência de alta escala.                                       |
| RNF-005 | Preservação de formatação            | O conteúdo visualizado deve preservar quebras de linha, indentação e espaçamento.                    | Obrigatória | Essencial para código, SQL e scripts.                                  |
| RNF-006 | Compatibilidade com arquivos legados | O sistema deve lidar de forma simples com arquivos textuais legados, especialmente PowerBuilder.     | Obrigatória | Considerar encoding.                                                   |
| RNF-007 | Tratamento de encoding               | O sistema deve tentar ler arquivos em `utf-8`, depois `latin-1` e depois `cp1252`.                   | Obrigatória | Reduz falhas em arquivos antigos.                                      |
| RNF-008 | Organização do projeto               | A estrutura de pastas deve ser clara e coerente com o objetivo didático.                             | Obrigatória | `backend/`, `frontend/`, `uploads/`, `prompts/`, `docs/`, `tests/`.   |
| RNF-009 | Testabilidade                        | O sistema deve permitir testes automatizados com pytest.                                             | Obrigatória | Testar regras principais do MVP.                                       |
| RNF-010 | Manutenibilidade                     | O código futuro deve ser organizado para facilitar evolução e leitura.                               | Obrigatória | Mesmo sendo MVP, evitar bagunça estrutural.                            |
| RNF-011 | Configurabilidade                    | Listas de linguagens, sistemas, domínios, extensões e tags devem ser centralizadas em `config.yaml`. | Obrigatória | Evita valores fixos espalhados.                                        |
| RNF-012 | Segurança local básica               | O sistema deve validar extensão e tamanho de arquivo antes de processar uploads.                     | Obrigatória | Mesmo local, precisa de validações mínimas.                            |
| RNF-013 | Interface simples                    | A interface deve ser funcional, leve e compreensível, sem sofisticação visual excessiva.             | Obrigatória | HTML e CSS simples.                                                    |
| RNF-014 | Clareza didática                     | O projeto deve manter artefatos de prompts e documentação para apoiar aprendizado de SDLC com IA.   | Obrigatória | Pastas `prompts/` e `docs/`.                                           |
| RNF-015 | Rastreabilidade básica               | O sistema deve manter metadados suficientes para localizar origem e classificação do conteúdo.       | Desejável   | Especialmente em uploads.                                              |
| RNF-016 | Robustez em erros comuns             | O sistema deve tratar erros simples de upload, leitura e validação sem quebrar a aplicação.          | Desejável   | Pode exibir mensagens amigáveis.                                       |
