#Prueba Técnica - Backend Developer - Datamart
#Aspirante: Santiago Esteawens Torres Zapata

# 3.Escribe una clase llamada BinaryTree que implemente un árbol binario de búsqueda. 
# La clase debe tener métodos para insertar, buscar, debe ser capaz de imprimir el árbol 
# en orden ascendente.

# Definición de clase Nodo como elemento del árbol binario
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Definición de clase para las operaciónes de árbol binario de búsqueda
class BinaryTree:
    def __init__(self):
        self.root = None

    # Métodos para insertar un elemento
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Métodos para encontrar un elemento
    def find(self, key):
        if self.root is None:
            return False
        else:
            return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                return False
            else:
                return self._find_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                return False
            else:
                return self._find_recursive(node.right, key)
        else:
            return True

    # Métodos para imprimir el árbol
    def print_tree(self):
        if self.root is not None:
            self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is not None:
            self._print_tree_recursive(node.left)
            print(node.val)
            self._print_tree_recursive(node.right)

# Inicialización del objeto clase y adición de elementos
binary_tree = BinaryTree()
binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(70)
binary_tree.insert(60)
binary_tree.insert(80)
binary_tree.insert(10)
binary_tree.insert(90)

print('Problema 3.')
print(f'Busca el elemento 20 en el árbol, resultado: {binary_tree.find(20)}')
print(f'Busca el elemento 25 en el árbol, resultado: {binary_tree.find(25)}')
print('Imprime en orden ascendente el árbol:')
binary_tree.print_tree()

# 3. Analice la complejidad computacional de cada operación implementada en su solución al problema 3.

# **Se asumen que las operaciones de comparación, asignación y acceso a los nodos del árbol se realizan 
#   en tiempo constante, es decir, O(1)

# Métodos de inserción: 'insert' y '_insert_recursive'
# La complejidad de tiempo de estas funciones es O(log n) en promedio, ya que solo necesita atravesar muchos nodos
# de forma logarítmica para encontrar la ubicación correcta para insertar la nueva clave.
# En el peor de los casos, cuando el árbol se convierte en una lista enlazada, la complejidad de tiempo
# pasa a O(n), donde n es el número de nodos en el árbol, en este caso el algoritmo necesita atravesar linealmente muchos nodos
# La complegidad de espacio es O(1) debido a la pila de llamadas de la recursión, en el caso promedio.
# Sin embargo, en el peor de los casos, la complejidad del espacio puede ser O(n) si el árbol está completamente 
# desequilibrado y degenera en una lista enlazada. Esto se debe a que el algoritmo necesita realizar un seguimiento 
# de todos los nodos de la lista.

# Métodos de busqueda: 'find' y '_find_recursive'
# Al igual que con la inserción, la complejidad de tiempo de estas funciones es O(log n), y en el peor de los casos es O(n).
# Esto se debe a que el algoritmo necesita atravesar el árbol de forma similar a la operación de inserción, 
# y se aplica el mismo análisis de complejidad temporal.
# La complejidad de espacio también es O(1) debido a la pila de llamadas de la recursión.

# Métodos para imprimir: 'print_tree' y '_print_tree_recursive'
# Estas funciones realizan un recorrido en orden del árbol, que tiene una complejidad de tiempo de O(n),
# esto se debe a que el algoritmo necesita visitar todos los nodos del árbol para poder imprimirlos, 
# y el número de nodos es linealmente proporcional al tamaño del árbol.
# La complejidad de espacio es O(1) puesto que el algoritmo necesita realizar un seguimiento de todos 
# los nodos de la lista para poder imprimirlos en orden.