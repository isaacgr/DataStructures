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

    def swap_nodes(self, k1, k2):
        # check if keys are same
        if k1 == k2:
            return
        # start at the head
        prev_1 = None
        curr_1 = self.head
        # go through list until we hit k1
        while curr_1 and curr_1.data != k1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        # go through list until we hit k2
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != k2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        # if k1 or k2 didnt exist in list
        if not curr_1 or not curr_2:
            return
        # curr_1 is our key, and prev_1 is the one before it
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2 # assume head if no previous

        # curr_2 is our key, and prev_2 is the one before it
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1 # assume head if no previous

        curr_1.next, curr_2.next = curr_2.next, curr_1.next # swap

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.swap_nodes('A', 'C')
ll.print_list()
