## 8. Prompt de Manutencao/Evolucao

Atue como desenvolvedor responsavel pela manutencao e evolucao do projeto **DevNotes Local**.

Preciso implementar **paginacao na tela de listagem de conteudos cadastrados**, acessada em:

```text
http://localhost:8000/content
```

Atualmente a tela pode carregar muitos registros de uma vez, principalmente apos a criacao de massas de teste. A manutencao deve melhorar a experiencia de navegacao, preparar o sistema para maior volume de anotacoes e manter a listagem simples de usar.

### Objetivo

Implementar paginacao funcional na listagem de conteudos cadastrados, respeitando a arquitetura atual do projeto e mantendo compatibilidade com os dados ja existentes.

### Escopo esperado

A solucao deve contemplar:

- ajuste na consulta de listagem para buscar apenas os registros da pagina atual;
- definicao de quantidade padrao de itens por pagina;
- suporte a parametro de pagina via query string, por exemplo:

```text
/content?page=1
/content?page=2
```

- calculo do total de registros cadastrados;
- calculo do total de paginas;
- exibicao dos controles de navegacao na tela;
- indicacao visual da pagina atual;
- links para pagina anterior e proxima;
- comportamento adequado quando nao houver registros;
- comportamento adequado quando a pagina solicitada for invalida, menor que 1 ou maior que o total de paginas;
- preservacao da ordenacao atual da listagem, se ja existir;
- manutencao da compatibilidade com os templates e rotas existentes.

### Regras de implementacao

1. Analise primeiro a estrutura atual do projeto, especialmente:
   - rotas de conteudo;
   - repositorios;
   - servicos;
   - modelos SQLAlchemy;
   - template da listagem;
   - testes existentes.

2. Implemente a paginacao seguindo os padroes ja usados no projeto.

3. Evite refatoracoes grandes ou mudancas fora do escopo.

4. A quantidade padrao por pagina deve ser simples de alterar futuramente.

5. Sugestao inicial: usar **20 itens por pagina**, salvo se a estrutura atual indicar outro valor mais adequado.

6. A tela deve continuar acessivel pela rota:

```text
/content
```

7. Ao acessar `/content` sem parametro, a aplicacao deve exibir a primeira pagina.

8. A paginacao deve funcionar com registros criados manualmente e tambem com a massa de teste de 200 anotacoes.

9. Os controles da tela devem ser claros e discretos, sem transformar a listagem em uma nova pagina visualmente diferente.

10. Evite quebrar funcionalidades existentes, como:
    - visualizacao de detalhes;
    - edicao;
    - exclusao;
    - busca ou filtros, caso compartilhem componentes ou rotas.

### Comportamentos esperados

Ao concluir a implementacao:

- acessar `/content` deve listar somente os primeiros registros da pagina atual;
- acessar `/content?page=2` deve exibir a segunda pagina;
- a tela deve mostrar em qual pagina o usuario esta;
- deve ser possivel ir para a pagina anterior, quando existir;
- deve ser possivel ir para a proxima pagina, quando existir;
- se houver 202 registros e o tamanho da pagina for 20, o sistema deve calcular 11 paginas;
- paginas invalidas devem ser tratadas sem erro inesperado;
- a listagem deve continuar ordenada de forma consistente.

### Testes e validacao

Inclua ou ajuste testes automatizados quando fizer sentido, cobrindo pelo menos:

- listagem da primeira pagina;
- listagem de uma pagina intermediaria;
- pagina solicitada menor que 1;
- pagina acima do total disponivel;
- calculo correto do total de paginas;
- preservacao da quantidade maxima de itens por pagina.

Tambem valide manualmente com a massa de dados local:

```powershell
.\venv\Scripts\python.exe scripts\seed_random_notes.py
```

Depois acesse:

```text
http://localhost:8000/content
http://localhost:8000/content?page=2
```

### Resultado esperado da entrega

Ao finalizar, informe:

- quais arquivos foram alterados;
- como a paginacao foi implementada;
- qual quantidade de itens por pagina foi definida;
- como executar os testes;
- se houve algum erro ou limitacao encontrada;
- observacoes importantes para evolucoes futuras, como:
  - selecao de quantidade por pagina;
  - paginacao combinada com filtros;
  - paginacao combinada com busca textual;
  - melhoria visual dos controles de navegacao.

