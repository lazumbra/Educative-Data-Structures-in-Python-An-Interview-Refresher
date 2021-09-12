from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    """Retornar a cabeça da lista"""

    def get_head(self):
        return self.head_node

    """Verfificar se a lista é vazia"""

    def is_empty(self):
        if(self.head_node is None):
            return True
        else:
            return False

    def insert_at_head(self, valor):
        """
        Inserir um nó na cabeça
        """
        temp_node = Node(valor)
        # Não entendo o motivo de quando eu insiro na cabeça
        # eu preciso apontar pra cabeça
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, valor):
        """Insere um nó no fim da lista.

        Se a lista for fazia, adicionar o elemento na cabeça.

        Se a lista não for vazia, você vai precisar percorrer a lista
        """

        new_node = Node(valor)

        if self.get_head() is None:
            self.head_node = new_node
            return

        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        temp.next_element = new_node
        return

    def print_list(self):
        """Insere um elemento na cabeça.
        O retorno true ou false é só um uma forma de marcar se a lista
        tem elemento ou não. Se não tem elemento a gente não imprime nada
        por isso a gente retorna false. Se consegui imprimir a lista
        completa ou imprimo true só prqa dizer.
        """
        if(self.is_empty()):
            print("Lista é vazia")
            return False

        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element

        print(temp.data, "-> None")
        return True
