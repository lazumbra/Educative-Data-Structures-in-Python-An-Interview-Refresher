from LinkedList import LinkedList

minha_lista = LinkedList()

minha_lista.insert_at_tail(1)
minha_lista.insert_at_tail(2)
minha_lista.insert_at_tail(3)
minha_lista.insert_at_tail(1)


minha_lista.print_list()
print(minha_lista.detect_loop())

# minha_lista.delete_at_head()

# print(minha_lista.delete(9))

# minha_lista.print_list()

# print(minha_lista.length())
