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

    def insert_at_tail(self, value):
        # crio um novo nó
        new_node = Node(value)

        # Olhar se a lista for vazia. Se a lista for vazia inserir o elemento
        # Como sendo a cabeça
        if self.head_node is None:
            self.head_node = new_node
            return

        # Se a lista não for vazia eu vou percorrer a lista e parar no último elemento
        # Perceba que eu paro no último elemento e não no None
        # Para percorrer a lista eu vou criar uma variável temporária.
        """
        A variável temporária vai servir como o apontador para eu ter acesso ao próximo elemento.
        Ela também vai ser para eu fazer a troca de nó
        """
        # Criando a variável temporária
        temp_node = self.get_head()

        while temp_node.next_element is not None:
            temp_node = temp_node.next_element

        # Agora que eu cheguei no último elemento é hora de adicionar
        # o meu elmento objetivo.
        temp_node.next_element = new_node
        return
