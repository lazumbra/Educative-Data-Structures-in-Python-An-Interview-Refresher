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

    def length(self):
        # Crio uma variável temporária na cabeça
        curr = self.get_head()
        length = 0

        # Percorrer a lista
        while curr != None:
            length += 1
            curr = curr.next_element

        return length

    def print_list(self):
        if(self.is_empty()):
            print("Lista é vazia")
            return False
        # Criar uma variável para percorrer a lista
        # Eu podria usar o self.get_head() também
        temp_node = self.head_node
        while temp_node.next_element is not None:
            print(temp_node.data, end=" -> ")
            temp_node = temp_node.next_element
        print(temp_node.data, "-> None")
        return True

    def delete_at_head(self):
        # criar um primeiro elemento para eu poder alocar a cabeça para outro ponto
        first_element = self.get_head()

        # Se o primeiro elemento for None, então não existe nada pra eu fazer
        # Só existe alguma coisa pra eu fazer, caso a cabeça não seja
        # none
        if first_element is not None:
            self.head_node = first_element.next_element
            self.head_node.previous_element = None
            first_element.next_element = None

        return

    def delete(self, dt):
        deleted = False
        # Olhar se a lista é vazia
        if self.is_empty():
            print("Lista é vazia")
            return deleted
        # Olhar se o nó que eu quero deletar é a cabeça
        """
        PROBLEMA: EU acho que deveria ser apenas
        if self.head_node.data == dt
        Verificar se eu consigo deletar na cabeça depois.
        Colocar a litsa 1 -> 2 -> None e tentar deletar
        """
        if self.head_node.data == dt:
            self.delete_at_head()
            deleted = True

        # Caso eu não tenha deletado na cabeça. Então eu vou precisar percorrer
        # a lista. Vou precisar de duas variáveis pra percorrer e poder deletar.
        # perceba que aqui eu estou pegando o segundo elemento depois da cabeça, depois
        # verificar isso.
        # Acho que o previous node poderia ser a cabeça, na minha mente isso faz até
        # mais sentido.
        temp_node = self.head_node.next_element
        previous_node = self.head_node

        # Percorrer a lista
        # usar o while para percorrer uma lista.
        # Aredito que se eu tentar apagar o segundo elemento de uma linkedlist
        # ex: 1 -> 2 -> 3 -> null. Tentar apagar o valor 2
        while temp_node is not None and deleted is False:
            if temp_node.data == dt:
                previous_node.next_element = temp_node.next_element
                deleted = True
                break
            previous_node = temp_node
            temp_node = temp_node.next_element

        if deleted is False:
            print(dt, " is not in List!")
        else:
            print(dt, " is deleted")
        return deleted

    def search(self, dt):
        """
        Essa função retorna None caso não encontre o valor na lista.
        Caso eu encontre o valor na lista retornar o nó
        Caso a lista seja vazia, retornar None e um aviso que a lista é vazia.
        """
        if self.is_empty():
            print("A Lista é vazia")
            return None

        # Quando for criar um temp node, sempre crie ele
        # como a cabeça da lista
        temp_node = self.head_node
        # percorrer a lista. Para percorrer a lista é importante começar
        # a parcorrer usando while
        while temp_node is not None:
            if temp_node.data == dt:
                return temp_node
            temp_node = temp_node.next_element

        # Caso depois de eu percorrer toda a lista eu ainda não tenha encontrado
        # o valor. Então fazer um print dizendo que eu não achei o valor
        print(dt, " não está na lista")
        return None
