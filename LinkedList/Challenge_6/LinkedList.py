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
