from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, dt):
        no_temporario = Node(dt)
        no_temporario.next_element = self.head_node
        self.head_node = no_temporario
        return self.head_node

    def print_list(self):
        if self.is_empty():
            print("Lista é vazia")
            return False
        temp_node = self.head_node
        while temp_node is not None:
            print(temp_node.data, end=' -> ')
            temp_node = temp_node.next_element
        print("None")
        return True

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head_node = new_node
            return

        temp_node = self.head_node
        while temp_node.next_element is not None:
            temp_node = temp_node.next_element

        temp_node.next_element = new_node
        return

    def delete_at_head(self):
        # first_element pode ser um elemento ou pode ser None
        # Se ele for None eu não faço anda com ele, se ele foi um elemento
        # entçao eu vou precisar desalocar ele no fim que eu fizer o delete.
        first_element = self.get_head()
        if not self.is_empty():
            self.head_node = first_element.next_element
            # Preciso desalocar o nó removido
            first_element.next_element = None

            return

    def delete(self, value):
        if self.is_empty():
            print("Lista vazia")
            return False

        deleted = False

        aux_node = self.head_node
        previous_element = None

        # Verificar se o elemento que eu quero deletar
        # é a cabeça
        if aux_node.data == value:
            self.head_node = aux_node.next_element
            aux_node.next_element = None
            return True

        previous_element = aux_node
        aux_node = aux_node.next_element

        # O primeiro elemento não é o que eu quero deletar, então percorrer a Linkedlist
        # procurando o valor que eu quero deletar.
        while aux_node is not None:
            if aux_node.data == value:
                previous_element.next_element = aux_node.next_element
                aux_node.next_element = None
                deleted = True
                break
            previous_element = aux_node
            aux_node = aux_node.next_element

        return deleted
