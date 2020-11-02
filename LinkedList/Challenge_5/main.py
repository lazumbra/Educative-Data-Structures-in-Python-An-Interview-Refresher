from Node import Node
from LinkedList import LinkedList


def reverse(lst):
    # Que implementação louca. Eu não entendi. Vou fazer o seguinte.
    # Implementar essa solução sugerida, ver se eu entendo no código e depois
    # implementar a minha própria solução
    previous = None
    current = lst.get_head()
    next = None

    while current:
        next = current.next_element
        print("muda:", current.data)
        current.next_element = previous
        print("prevideous:", current.next_element)
        previous = current
        current = next

        lst.head_node = previous
    return lst


lst = LinkedList()
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)


lst.print_list()
lst.delete(2)
# reverse(lst)
lst.print_list()
