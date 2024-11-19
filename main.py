import matplotlib.pyplot as plt
import networkx as nx
import random 
from colorama import Fore, Back, Style, init

# Inicializa a colorama para funcionar no Windows
init(autoreset=True)

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

    def remove(self, key):
        node = self.search(self.root, key)
        if node == self.NIL:
            print(f"Nó {key} não encontrado.")
            return
        
        if node.left != self.NIL and node.right != self.NIL:
            successor = self.minimum(node.right)
            node.key = successor.key
            node = successor
        
        # Agora o nó a ser removido tem no máximo um filho
        child = node.left if node.left != self.NIL else node.right
        self.transplant(node, child)
        
        if node.color == "black":
            self.remove_fixup(child)
    
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def remove_fixup(self, node):
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                
                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = "black"

    def search(self, node, key):
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

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

    def remove(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            # Caso 1: Nó tem um único filho ou nenhum
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            # Caso 2: Nó tem dois filhos
            temp = self.get_minimum(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)

        # Atualiza a altura do nó atual
        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Reequilíbrio
        balance = self.get_balance(root)

        # Caso de desbalanceamento
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_minimum(self, root):
        while root.left:
            root = root.left
        return root

# Função para desenhar a árvore binária corretamente sem sobreposição
def draw_binary_tree(tree, is_rb):

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
def print_welcome():
    print(Fore.YELLOW + Style.BRIGHT + "\n" + "="*40)
    print(Fore.GREEN + Style.BRIGHT + "Bem-vindo ao Gerenciador de Árvores Binárias!")
    print("="*40 + "\n")

def print_menu():
    print(Fore.CYAN + Style.BRIGHT + "\nEscolha a Árvore ou opção desejada:")
    print(Fore.MAGENTA + "1 - Árvore Rubro-Negra")
    print(Fore.MAGENTA + "2 - Árvore AVL")
    print(Fore.RED + "0 - Sair")

def print_action_menu():
    print(Fore.CYAN + "\nEscolha uma ação desejada:")
    print(Fore.GREEN + "1 - Inserir um nó")
    print(Fore.GREEN + "2 - Remover um nó")
    print(Fore.GREEN + "3 - Exibir a árvore (in-order)")
    print(Fore.GREEN + "4 - Desenhar a árvore")
    print(Fore.YELLOW + "0 - Voltar ao menu principal")

def main():
    while True:
        print_welcome()
        print_menu()
        
        choice = input(Fore.YELLOW + "Digite sua opção: ")

        if choice == "1":
            tree = RedBlackTree()
            values = random.sample(range(1, 100), random.randint(23, 30))
            print(f"\nValores inseridos na Árvore Rubro-Negra: {values}")
            for value in values:
                tree.insert(value)

            while True:
                print_action_menu()

                action = input(Fore.YELLOW + "Digite a ação desejada: ")

                if action == "1":
                    value = int(input(Fore.GREEN + "Informe o valor a ser inserido: "))
                    tree.insert(value)
                    print(Fore.GREEN + f"Nó {value} inserido com sucesso!")

                elif action == "2":
                    value = int(input(Fore.RED + "Informe o valor a ser removido: "))
                    tree.remove(value)
                    print(Fore.RED + f"Nó {value} removido com sucesso!")

                elif action == "3":
                    print("\nÁrvore Rubro-Negra (in-order):")
                    tree.inorder()
                    print()

                elif action == "4":
                    print("Desenhando a Árvore Rubro-Negra...")
                    draw_binary_tree(tree, is_rb=True)

                elif action == "0":
                    break
                else:
                    print(Fore.RED + "Opção inválida. Tente novamente.")

        elif choice == "2":
            tree = AVLTree()
            root = None
            values = random.sample(range(1, 100), random.randint(23, 30))
            print(f"\nValores inseridos na Árvore AVL: {values}")
            for value in values:
                root = tree.insert(root, value)

            while True:
                print_action_menu()

                action = input(Fore.YELLOW + "Digite a ação desejada: ")

                if action == "1":
                    value = int(input(Fore.GREEN + "Informe o valor a ser inserido: "))
                    root = tree.insert(root, value)
                    print(Fore.GREEN + f"Nó {value} inserido com sucesso!")

                elif action == "2":
                    value = int(input(Fore.RED + "Informe o valor a ser removido: "))
                    root = tree.remove(root, value)
                    print(Fore.RED + f"Nó {value} removido com sucesso!")

                elif action == "3":
                    print("\nÁrvore AVL (in-order):")
                    tree.inorder(root)
                    print()

                elif action == "4":
                    print("Desenhando a Árvore AVL...")
                    draw_binary_tree(root, is_rb=False)

                elif action == "0":
                    break
                else:
                    print(Fore.RED + "Opção inválida. Tente novamente.")

        elif choice == "0":
            print(Fore.YELLOW + "Encerrando o programa.")
            break

        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

main()