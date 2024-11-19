import matplotlib.pyplot as plt
import networkx as nx
import random 

# Classe para Nó da Árvore Rubro-Negra
class NodeRB:
    def __init__(self, key):
        self.key = key
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


# Classe para Árvore Rubro-Negra
class RedBlackTree:
    def __init__(self):
        self.NIL = NodeRB(None)
        self.NIL.color = "black"
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = NodeRB(key)
        node.left = self.NIL
        node.right = self.NIL
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.color = "red"
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder(node.right)


# Classe para Nó da Árvore AVL
class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Classe para Árvore AVL
class AVLTree:
    def insert(self, root, key):
        if not root:
            return NodeAVL(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)


# Função para desenhar a árvore binária corretamente sem sobreposição
def draw_binary_tree(tree, is_rb):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.DiGraph()

    # Função recursiva para calcular posições dos nós
    def add_edges(node, x=0, y=0, level=1, pos=None, is_rb=False):
        if node is None or (is_rb and node.key is None):
            return

        if pos is None:
            pos = {}

        # Define posição do nó
        pos[node.key] = (x, y)
        G.add_node(node.key, pos=(x, y), color="red" if is_rb and node.color == "red" else "black")

        # Adiciona arestas para filhos
        if node.left and (not is_rb or node.left.key is not None):
            G.add_edge(node.key, node.left.key)
            add_edges(node.left, x - 1.5 / level, y - 1, level + 1, pos, is_rb)

        if node.right and (not is_rb or node.right.key is not None):
            G.add_edge(node.key, node.right.key)
            add_edges(node.right, x + 1.5 / level, y - 1, level + 1, pos, is_rb)

        return pos

    # Gera posições e cor para os nós
    pos = add_edges(tree.root if is_rb else tree, is_rb=is_rb)
    colors = [G.nodes[node]["color"] for node in G.nodes]

    # Desenha a árvore com as posições ajustadas
    nx.draw(
        G, 
        pos, 
        with_labels=True, 
        node_color=colors, 
        node_size=1000, 
        font_size=10, 
        font_color="white", 
        arrows=True
    )
    plt.show()

# Função principal para selecionar a árvore e gerar números aleatórios
def main():
    while True:
        choice = input("Escolha a árvore (1 - Rubro-Negra, 2 - AVL, 0 - Sair): ")

        if choice == "1":
            tree = RedBlackTree()
            # Gera de 23 a 30 números aleatórios únicos
            values = random.sample(range(1, 100), random.randint(23, 30))
            print(f"Valores inseridos na Árvore Rubro-Negra: {values}")
            for value in values:
                tree.insert(value)
            print("Árvore Rubro-Negra (in-order):")
            tree.inorder()
            print("\nDesenhando a Árvore...")
            draw_binary_tree(tree, is_rb=True)

        elif choice == "2":
            tree = AVLTree()
            root = None
            # Gera de 23 a 30 números aleatórios únicos
            values = random.sample(range(1, 100), random.randint(23, 30))
            print(f"Valores inseridos na Árvore AVL: {values}")
            for value in values:
                root = tree.insert(root, value)
            print("Árvore AVL (in-order):")
            tree.inorder(root)
            print("\nDesenhando a Árvore...")
            draw_binary_tree(root, is_rb=False)

        elif choice == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
