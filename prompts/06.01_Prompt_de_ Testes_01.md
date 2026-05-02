## 6. Prompt de Testes

Atue como especialista em testes de software, pytest, FastAPI, SQLite, SQLAlchemy e validação de MVPs locais.

Quero criar a estratégia e a implementação inicial dos testes do projeto DevNotes Local.

Contexto:
O DevNotes Local é uma aplicação web local, simples e didática, criada com Python 3.11, FastAPI, SQLite, SQLAlchemy, SQLite FTS5, Jinja2, HTML/CSS simples, Highlight.js e pytest.

O sistema permite cadastrar, editar, excluir, pesquisar e visualizar conteúdos técnicos, além de fazer upload simples de arquivos para armazenamento local e indexação textual.

Funcionalidades principais do MVP:
- cadastro manual de conteúdo técnico;
- edição de conteúdo;
- exclusão de conteúdo;
- pesquisa textual;
- filtros por categoria, linguagem, tags, tipo, sistema, domínio e regra de negócio;
- upload simples de um arquivo por vez;
- validação de extensão;
- validação de tamanho máximo de 12 MB;
- leitura de arquivo com tentativa de utf-8 e fallback para latin-1 e cp1252;
- classificação automática de linguagem e tipo de objeto pela extensão;
- salvamento de arquivo em uploads/;
- gravação de metadados e conteúdo textual no SQLite;
- indexação com SQLite FTS5;
- visualização preservando formatação com <pre><code>;
- uso de Highlight.js na tela de detalhe.

Extensões aceitas:
- .py
- .java
- .sql
- .md
- .txt
- .srw
- .sru
- .srd
- .srm
- .srf
- .sra
- .srs

Mapeamento PowerBuilder:
- .srw -> PowerBuilder Window
- .sru -> PowerBuilder User Object
- .srd -> PowerBuilder DataWindow
- .srm -> PowerBuilder Menu
- .srf -> PowerBuilder Function
- .sra -> PowerBuilder Application
- .srs -> PowerBuilder Structure

Escopo fora dos testes neste momento:
- autenticação;
- múltiplos usuários;
- permissões;
- APIs externas;
- testes de carga;
- testes complexos de interface;
- testes em produção;
- testes com infraestrutura em nuvem.

Sua tarefa:
Crie uma estratégia de testes profissional e adequada para um MVP local.

A resposta deve conter:

1. Objetivo dos testes
   - explique o que os testes devem garantir neste MVP.

2. Pirâmide de testes simplificada
   - testes unitários;
   - testes de integração;
   - testes básicos de rotas FastAPI;
   - testes básicos de renderização quando aplicável.

3. Plano de testes por funcionalidade
   Inclua testes para:
   - cadastro de conteúdo;
   - edição;
   - exclusão;
   - pesquisa;
   - filtros;
   - upload;
   - validação de extensão;
   - limite de 12 MB;
   - leitura com fallback de encoding;
   - classificação automática por extensão;
   - classificação de arquivos PowerBuilder;
   - gravação no SQLite;
   - indexação com SQLite FTS5;
   - visualização com preservação de formatação;
   - renderização básica dos templates.

4. Casos de teste detalhados
   Para cada caso, informe:
   - identificador;
   - objetivo;
   - pré-condição;
   - entrada;
   - resultado esperado;
   - tipo de teste: unitário, integração ou rota.

5. Organização sugerida da pasta tests/
   Proponha uma estrutura, por exemplo:
   - tests/test_content_service.py
   - tests/test_upload_service.py
   - tests/test_encoding_service.py
   - tests/test_extension_classifier.py
   - tests/test_search_fts.py
   - tests/test_routes.py

6. Fixtures recomendadas
   Sugira fixtures para:
   - banco SQLite temporário;
   - cliente de teste FastAPI;
   - arquivo .txt;
   - arquivo .sql;
   - arquivo .srw;
   - arquivo com encoding latin-1;
   - arquivo com extensão inválida;
   - arquivo acima do limite permitido.

7. Implementação dos testes
   Gere exemplos de testes com pytest.
   Sempre que necessário, explique os ajustes que talvez precisem ser feitos de acordo com a estrutura real do projeto.

8. Testes mínimos obrigatórios para considerar o MVP aceitável
   Liste um conjunto mínimo de testes que precisam passar.

9. Como executar os testes
   Informe o comando para rodar pytest.
   Informe como interpretar o resultado.

10. Recomendações de manutenção dos testes
   Explique como evoluir os testes conforme novas funcionalidades forem adicionadas.

Regras:
- Use Markdown.
- Use tabelas quando ajudar.
- Priorize testes úteis para o MVP.
- Não proponha ferramentas complexas demais.
- Não proponha Selenium, Playwright ou testes E2E completos neste momento, a menos que cite apenas como evolução futura.
- Mantenha os testes compatíveis com projeto local e pequeno.
- Não altere o escopo funcional do MVP.