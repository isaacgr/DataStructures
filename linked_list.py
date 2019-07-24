class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print current_node.data
            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data, node):
        if not node:
            print "Node not in list"
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node


ll = LinkedList()
ll.append("A")
ll.append("B")
ll.prepend("C")
ll.insert("E", ll.head.next)
ll.print_list()
