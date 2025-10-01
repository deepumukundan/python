class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

node_a = ListNode(5)
node_b = ListNode(10)
node_c = ListNode(15)
head = node_a
node_a.next = node_b
node_b.next = node_c

def sum_of_vals(head):
    sum = 0
    while head:
        sum += head.val
        head = head.next
    return sum

print(sum_of_vals(head))

head = node_a

def sum_of_vals_recursive(node):
    if node == None:
        return 0
    
    return node.val + sum_of_vals_recursive(node.next)

print(sum_of_vals_recursive(head))