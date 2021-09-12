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

    """
    Inserir um nó na cabeça
    """

    def insert_at_head(self, valor):
        temp_node = Node(valor)
        # Não entendo o motivo de quando eu insiro na cabeça
        # eu preciso apontar pra cabeça
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node
