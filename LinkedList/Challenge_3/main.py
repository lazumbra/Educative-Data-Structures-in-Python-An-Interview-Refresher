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

def delete_at_tail(lst):

    current_node = lst.get_head()

    previ_node = None

    if current_node == None:
        return

    while current_node.next_element is not None:
        previ_node = current_node
        current_node = current_node.next_element
    
    previ_node.next_element = current_node.next_element
    current_node.next_element = None
    


    



lst = LinkedList()



lst.print_list()

delete_at_tail(lst)

#delete_at_head(lst)
#delete_at_head(lst)

lst.print_list()
