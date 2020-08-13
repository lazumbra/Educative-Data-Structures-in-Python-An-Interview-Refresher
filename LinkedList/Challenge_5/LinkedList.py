from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node == None):
            return True
        else:
            return False

    def insert_at_head(self, dt):
        # Para inserir eu preciso de uma variável temporal
