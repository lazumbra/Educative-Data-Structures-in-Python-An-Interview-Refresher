from LinkedList import LinkedList
from Node import Node


def delete(lst, value):
    deleted = False
    if lst.is_empty():
        print("List is Empty")
        return deleted

    current_node = lst.get_head()

    if current_node.data is value:
        # Point head to the next element of the first element
        lst.headNode = current_node.next_element
        # Point the next element of the first element to None
        current_node.next_element.previous_element = None
        deleted = True  # Both links have been changed.
        print(str(current_node.data) + " Deleted!")
        return deleted

    # Traversing/Searching for node to Delete
    while current_node:
        if value is current_node.data:
            if current_node.next_element:
                # Link the next node and the previous node to each other
                prev_node = current_node.previous_element
                next_node = current_node.next_element
                prev_node.next_element = next_node
                next_node.previous_element = prev_node
                # previous node pointer was maintained in Singly Linked List

            else:
                current_node.previous_element.next_element = None
            deleted = True
            break
        # previousNode = tempNode was used in Singly Linked List
        current_node = current_node.next_element

    if deleted is False:
        print(str(value) + " is not in the List!")
    else:
        print(str(value) + " Deleted!")
    return deleted


lst = LinkedList()
for i in range(11):
    lst.insert_at_head(i)

lst.print_list()
delete(lst, 5)

lst.print_list()
delete(lst, 0)

lst.print_list()
