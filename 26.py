#WAP IN PYTHON TO PRINT A LINKED LIST ON PYTHON :

# Node class

class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head to None

    # Method to insert a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        if not current:
            print("The linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the linked list

# Driver code
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

print("The Linked List is:")
linked_list.print_list()
