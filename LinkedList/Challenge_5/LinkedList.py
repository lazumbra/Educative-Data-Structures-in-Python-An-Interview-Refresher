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
        # porque eu preciso dessa variável temp?
        # Eu conseguiria adicionar código sem essa variável?
        temp_node = Node(dt)
        # Porque eu tenho de chamar o self para chamar uma função aqui dentro?
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node
        # Se a lista não estiver vazia.
        temp_node.next_element = self.head_node
        # Eu preciso mesmo de alocar o previous elemento para temp_node?
        # Fazer um teste do que aconteceria se eu não fizesse essa alocação.
        self.head_node.previous_element = temp_node
        self.head_node = temp_node
        return self.head_node
