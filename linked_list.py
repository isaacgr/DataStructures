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

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None
        return

    def delete_pos(self, pos):
        index = 0
        cur_node = self.head
        prev_node = None

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        while cur_node and index < pos:
            prev_node = cur_node
            cur_node = cur_node.next
            index += 1
        if cur_node:
            prev_node.next = cur_node.next
            cur_node = None
            return
        print 'Node not in list'

    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count +=1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
print(ll.len_recursive(ll.head))
ll.print_list()
