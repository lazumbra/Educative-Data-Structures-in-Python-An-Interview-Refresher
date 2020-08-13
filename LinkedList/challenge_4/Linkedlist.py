from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if (self.head_node is None):
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        # Olhar se a lista é vazia
        # Se a lista for vazia: Adicionar o nó na cabeça
        if self.get_head is None:
            self.head_node = new_node
            return
        # Se a lista não é vazia então percorrer a lista
        # Para percorrer a lista eu preciso de um nó temporário
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        temp.next_element = new_node
        return

    def print_list(self):
        # Verificar se a lista é vazia
        if(self.is_empty()):
            print('List is Empty')
            return False
        # Cria uma variável temporária pra percorrer a lista
        # A variável temporária precisa começar na cabeça
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Pra deletar na cabeça vc precisa criar um axu
        # que faça referencia pra cabeça
        first_element = self.get_head()
        # Você olha se a cabeça está vazia, se tiver vazia retorne nada e
        # saia da função.
        # Se o primeiro elemento não é vazia troque as referencias
        # cabeça aponta para o elemento depois do primeiro
        # tira a referencia do primeiro elemento
        # primeiro elemento aponta pra None
        if(self.head_node is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if(self.is_empty()):
            print("List is empty")
            return deleted

        # Criar as variáveis auxiliar pra me ajudar com a
        # passagem na lista
        previous_node = None
        current_node = self.head_node

        # Olhar se o primeiro elemento a ser deletado é a cabeça
        if current_node.data is value:
            self.delete_at_head()
            deleted = True
            return deleted

        # Percorrer a lista
        while current_node:
            if current_node.data is value:
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted

    def search(self, dt):
        if self.is_empty():
            print('List is Empty')
            return None

        # Criar a minha variável temporária na cabeça e percorrer a lista
        temp_node = self.head_node

        while temp_node:
            if(temp_node.data is dt):
                return temp_node
            temp_node = temp_node.next_element

        print(dt, " is not in List")
        return None
