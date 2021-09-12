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

    def delete_at_head(self):
        """Deletar um nó na cabeça"""

        primeiro_elemento = self.get_head()

        if (primeiro_elemento is not None):
            self.head_node = primeiro_elemento.next_element
            primeiro_elemento.next_element = None
        return

    def delete(self, valor):
        """
        Deletar um elemento da lista a partir do valor.
        então eu vou encontrar na lista um elemento que tenha o mesmo
        valor passado na função e então eu deleto esse nó da lista.
        """
        deleted = False

        if self.is_empty():
            print("Lista vazia")
            return deleted

        current_node = self.get_head()
        previous_node = None

        if current_node.data is valor:
            self.delete_at_head()
            deleted = True
            return deleted

        # Percorrer a lista
        while current_node.next_element is not None:
            if valor is current_node.data:
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted
