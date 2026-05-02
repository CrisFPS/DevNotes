---
id: TASK-024
titulo: Ajustar densidade visual da listagem paginada
feature: FEAT-001
user_story: US-001
status: a_fazer
tipo: melhoria_futura
dependencias: TASK-023
requisito_funcional: RF-023
requisitos_nao_funcionais: RNF-004, RNF-010, RNF-013
---

# TASK-024 — Ajustar densidade visual da listagem paginada

## Descrição

A paginação implementada na TASK-023 resolveu o problema funcional de carregar
muitos registros de uma vez na tela `/content`. No entanto, a listagem ainda
apresenta baixa densidade visual: o espaçamento entre os itens é amplo e pode
exigir rolagem excessiva da tela, especialmente quando a página contém os 20
itens configurados como padrão.

Essa limitação não impede o funcionamento da paginação, mas reduz a ergonomia da
navegação quando há muitos conteúdos cadastrados.

---

## Objetivo

Melhorar a experiência de navegação na listagem paginada, tornando a visualização
mais compacta e eficiente sem alterar o comportamento funcional já validado.

---

## Escopo esperado

- Reduzir margens e espaçamentos verticais entre os itens da listagem.
- Avaliar o tamanho de fontes, metadados e ações para manter legibilidade com
  menor altura por item.
- Preservar a clareza visual da página e os controles de paginação existentes.
- Manter o padrão de 20 itens por página enquanto o layout é compactado.
- Depois do ajuste visual, avaliar como evolução complementar a seleção de
  quantidade de itens por página.

---

## Critérios de aceitação

- A tela `/content` continua exibindo a listagem paginada corretamente.
- A página mantém no máximo 20 itens por página por padrão.
- Os itens ocupam menos altura vertical sem prejudicar a leitura.
- A necessidade de rolagem é reduzida em telas comuns de notebook ou desktop.
- Os links de detalhe, edição e exclusão continuam acessíveis.
- Os controles de paginação continuam visíveis e compreensíveis.
- A tela vazia continua exibindo mensagem adequada.

---

## Evolução complementar

Após compactar o layout, avaliar a inclusão de um controle para seleção de
quantidade de itens por página, com opções como:

- 10 itens por página
- 20 itens por página
- 50 itens por página

Essa seleção deve preservar a simplicidade do MVP e só deve ser implementada se
melhorar a navegação sem aumentar demais a complexidade da interface.

---

## Dependências

TASK-023.

---

## Observações técnicas

- A primeira melhoria recomendada é compactar o layout da listagem, não reduzir
  imediatamente o padrão de 20 itens.
- Reduzir a quantidade padrão para 10 ou 15 itens pode diminuir a rolagem por
  página, mas aumenta a quantidade de páginas e cliques.
- A seleção configurável de quantidade por página deve ser tratada como evolução
  posterior ao ajuste visual.
- A mudança deve se concentrar em `frontend/templates/list.html` e
  `frontend/static/css/style.css`, evitando alterações desnecessárias nas camadas
  de serviço e repositório.
