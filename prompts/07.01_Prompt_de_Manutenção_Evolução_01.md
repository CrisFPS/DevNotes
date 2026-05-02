## 7. Prompt de Manutenção/Evolução

Atue como desenvolvedor responsável pela manutenção e evolução do projeto **DevNotes Local**.

Preciso criar uma massa de dados de teste para avaliar melhor a exibição das anotações na tela e apoiar a definição futura da paginação.

Crie um script para inserir **200 anotações técnicas aleatórias** na base de dados da aplicação.

As anotações devem conter dados variados e realistas, simulando conteúdos como:

- snippets de código;
- comandos SQL;
- anotações técnicas;
- pequenas regras de negócio;
- observações sobre sistemas legados;
- scripts simples;
- exemplos de uso de ferramentas;
- categorias, tags, linguagem, sistema e domínio variados.

O script deve:

1. respeitar a estrutura atual do banco de dados;
2. gerar dados suficientemente diferentes entre si;
3. preencher os campos obrigatórios corretamente;
4. evitar registros duplicados óbvios;
5. ser seguro para execução em ambiente local de desenvolvimento;
6. permitir fácil reexecução, se possível, sem causar inconsistências relevantes;
7. executar a inserção na base de dados local.

Após a execução, informe:

- quantos registros foram inseridos;
- se houve algum erro;
- quais tipos de dados foram gerados;
- qualquer observação importante para que eu consiga avaliar a tela de listagem e pensar na futura paginação.

