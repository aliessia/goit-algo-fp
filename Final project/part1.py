class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        self.head = reverse_list(self.head)

    def sort(self):
        self.head = merge_sort(self.head)

    def merge_with(self, other):
        self.head = sorted_merge(self.head, other.head)


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort(head):
    if not head or not head.next:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    
    sorted_list = sorted_merge(left, right)
    
    return sorted_list

def get_middle(head):
    if not head:
        return head
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def sorted_merge(a, b):
    if not a:
        return b
    if not b:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    
    return result


llist1 = LinkedList()
llist1.append(3)
llist1.append(1)
llist1.append(2)

llist2 = LinkedList()
llist2.append(6)
llist2.append(4)
llist2.append(5)

print("Перший список:")
llist1.print_list()
print("Другий список:")
llist2.print_list()

llist1.reverse()
print("Перший список після реверсування:")
llist1.print_list()

llist1.sort()
print("Перший список після сортування:")
llist1.print_list()

llist1.merge_with(llist2)
print("Об'єднаний список:")
llist1.print_list()
