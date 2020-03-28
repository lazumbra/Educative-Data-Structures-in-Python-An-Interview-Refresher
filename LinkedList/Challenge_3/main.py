from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    
    if lst.is_empty():
        return False
    
    current_node = lst.get_head()
    
    if current_node.data == value:
        lst.delete_at_head()
        return True
    
    #Percorrer a lista 

    prevNode = None

    while current_node.data != value and current_node.next_element != None:
        prevNode = current_node
        current_node = current_node.next_element

    if current_node.data == value:
        prevNode.next_element = current_node.next_element
        current_node.next_element = None
        return True
    
    
    
    return False
    



lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)


lst.print_list()

delete(lst, 4)

#delete_at_head(lst)
#delete_at_head(lst)

lst.print_list()
