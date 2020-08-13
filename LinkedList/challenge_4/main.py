from Node import Node
from Linkedlist import LinkedList


def length(lst):
    count = 0
    if lst.is_empty():
        return count

    current_node = lst.get_head()
    while current_node:
        count += 1
        current_node = current_node.next_element
    return count


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
print(length(lst))
