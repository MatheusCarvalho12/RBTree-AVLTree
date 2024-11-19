
---

# Gerenciador de Árvores Binárias

Este projeto implementa e gerencia duas estruturas de árvore binária: a Árvore Rubro-Negra (Red-Black Tree) e a Árvore AVL. O programa permite realizar operações de inserção, remoção, e visualização (em ordem) dos nós dessas árvores, além de oferecer uma visualização gráfica das mesmas. Ambas as árvores são balanceadas automaticamente, mantendo suas respectivas propriedades de balanceamento.

## Conceitos

- **Árvore Rubro-Negra (Red-Black Tree)**:
  - É uma árvore binária de busca balanceada com propriedades de cores (vermelho e preto) que garantem um balanceamento adequado.
  - As principais propriedades incluem: o nó raiz é sempre preto, as folhas são pretas, um nó vermelho nunca pode ter um filho vermelho, e todos os caminhos de qualquer nó até suas folhas descendentes contêm o mesmo número de nós pretos.
  - As operações de inserção e remoção são acompanhadas de correções automáticas para manter o balanceamento.

- **Árvore AVL**:
  - Uma árvore binária de busca balanceada onde, para cada nó, a diferença de altura entre a subárvore esquerda e a subárvore direita não pode ser maior do que 1 (fator de balanceamento de -1, 0 ou +1).
  - A cada operação de inserção ou remoção, a árvore pode passar por rotações para restaurar o balanceamento.

## Funcionalidades

- **Árvore Rubro-Negra**:
  - **Balanceamento automático** após inserções e remoções para garantir que as propriedades de cores e balanceamento da árvore sejam mantidas.
  - **Operações**:
    - Inserção de nós.
    - Remoção de nós.
    - Exibição da árvore (in-order).
    - Desenho da árvore graficamente.

- **Árvore AVL**:
  - **Balanceamento automático** após inserções e remoções para garantir que a diferença de altura entre subárvores adjacentes nunca ultrapasse 1.
  - **Operações**:
    - Inserção de nós.
    - Remoção de nós.
    - Exibição da árvore (in-order).
    - Desenho da árvore graficamente.

## Requisitos

- **Python 3.x**
- **Bibliotecas**:
  - `matplotlib`: Para exibição gráfica da árvore.
  - `networkx`: Para construção e exibição da estrutura da árvore.
  - `colorama`: Para colorir a saída no terminal.

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```bash
pip install matplotlib networkx colorama
```

## Como Usar

Ao executar o código, o usuário é apresentado com um menu interativo onde pode escolher qual árvore (Rubro-Negra ou AVL) deseja manipular. A seguir, o usuário pode inserir, remover ou visualizar nós dessas árvores, bem como desenhá-las graficamente.

### Passos:

1. **Escolher o tipo de árvore**:
   - Digite `1` para a Árvore Rubro-Negra.
   - Digite `2` para a Árvore AVL.
   - Digite `0` para sair.

2. **Escolher uma ação para a árvore selecionada**:
   - Inserir um nó.
   - Remover um nó.
   - Exibir a árvore (em ordem).
   - Desenhar a árvore graficamente.

## Estrutura do Código

### 1. **Classe `NodeRB`** (Árvore Rubro-Negra)

A classe `NodeRB` representa um nó da Árvore Rubro-Negra. Cada nó possui:
- `key`: O valor armazenado no nó.
- `color`: A cor do nó, que pode ser `red` (vermelho) ou `black` (preto).
- `left` e `right`: Referências para os filhos esquerdo e direito.
- `parent`: Referência para o nó pai.

### 2. **Classe `RedBlackTree`** (Árvore Rubro-Negra)

A classe `RedBlackTree` implementa a Árvore Rubro-Negra e contém os seguintes métodos:

- **`insert(key)`**: Insere um nó na árvore. Após a inserção, a árvore pode passar por correções de balanceamento (função `insert_fixup`) para manter as propriedades da árvore Rubro-Negra.
- **`remove(key)`**: Remove um nó da árvore. Se o nó a ser removido tem dois filhos, o sucessor do nó é encontrado e suas chaves são trocadas. A remoção é seguida por correções de balanceamento (função `remove_fixup`).
- **`search(node, key)`**: Busca um nó com chave `key`.
- **`left_rotate(x)`** e **`right_rotate(x)`**: Realizam rotações à esquerda e à direita, respectivamente, para garantir o balanceamento da árvore durante as operações de inserção e remoção.
- **`inorder(node)`**: Exibe os nós da árvore em ordem crescente (in-order traversal).
- **`insert_fixup(node)`**: Ajusta a árvore após a inserção de um nó para garantir que as propriedades de balanceamento e cor sejam mantidas.
- **`remove_fixup(node)`**: Ajusta a árvore após a remoção de um nó para restaurar as propriedades de balanceamento.

### 3. **Classe `NodeAVL`** (Árvore AVL)

A classe `NodeAVL` representa um nó da Árvore AVL e possui:
- `key`: O valor armazenado no nó.
- `left` e `right`: Referências para os filhos esquerdo e direito.
- `height`: A altura do nó, usada para calcular o fator de balanceamento.

### 4. **Classe `AVLTree`** (Árvore AVL)

A classe `AVLTree` implementa a Árvore AVL e contém os seguintes métodos:

- **`insert(root, key)`**: Insere um nó na árvore. Após a inserção, o balanceamento da árvore é recalculado e, se necessário, a árvore é reequilibrada usando rotações.
- **`left_rotate(z)`** e **`right_rotate(z)`**: Realizam rotações à esquerda e à direita para balancear a árvore após uma inserção ou remoção.
- **`get_height(root)`**: Retorna a altura de um nó.
- **`get_balance(root)`**: Calcula o fator de balanceamento de um nó (a diferença de altura entre os filhos esquerdo e direito).
- **`remove(root, key)`**: Remove um nó da árvore, realizando as rotações necessárias para restaurar o balanceamento.
- **`inorder(root)`**: Exibe os nós da árvore em ordem crescente (in-order traversal).

### 5. **Função `draw_binary_tree(tree, is_rb)`**

Esta função desenha a árvore binária graficamente. Ela utiliza a biblioteca `networkx` para construir a estrutura da árvore e `matplotlib` para exibi-la. A função ajusta as posições dos nós para evitar sobreposição e usa cores para distinguir a Árvore Rubro-Negra (vermelho e preto) da Árvore AVL (sem cores).

### 6. **Funções de Interface com o Usuário**

- **`print_welcome()`**: Exibe uma mensagem de boas-vindas.
- **`print_menu()`**: Exibe o menu principal com as opções de árvore.
- **`print_action_menu()`**: Exibe o menu de ações disponíveis para a árvore selecionada.

### 7. **Função `main()`**

A função principal (`main`) é o ponto de entrada do programa, que oferece um menu interativo para o usuário escolher qual árvore manipular e quais operações realizar.

## Exemplos de Uso

### Exemplo de Inserção na Árvore Rubro-Negra:

1. Escolha a Árvore Rubro-Negra.
2. Insira os valores desejados.
3. Veja a árvore após a inserção com a função `inorder` ou visualize-a graficamente.

### Exemplo de Remoção na Árvore AVL:

1. Escolha a Árvore AVL.
2. Remova um nó da árvore.
3. Veja a árvore após a remoção com a função `inorder` ou visualize-a graficamente.

## Conclusão

Este projeto oferece uma implementação das árvores binárias Rubro-Negra e AVL, com suporte a inserção, remoção, visualização e desenho gráfico das árvores. Ele exemplifica o funcionamento dessas estruturas balanceadas e as correções automáticas necessárias para manter a eficiência de operações como busca, inserção e remoção.

--- 

