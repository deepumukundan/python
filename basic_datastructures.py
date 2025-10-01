#-------------------------------------------------
class ListNode:
    """A singly linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
head = l1
l1.next = l2
l2.next = l3

#-------------------------------------------------
class DoublyListNode:
    """A doubly linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

l1 = DoublyListNode(1)
l2 = DoublyListNode(2)
l3 = DoublyListNode(3)
head = l1
l1.next = l2
l2.prev = l1
l2.next = l3
l3.prev = l2

#-------------------------------------------------
class TreeNode:
    """A Binary Tree"""
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

values = []
def dfsInOrder(node):
        if not node:
            return
        left = dfsInOrder(node.left)
        values.append(node.val) # This is in-order. If this line was before left, its pre-order and after right is post-order
        right = dfsInOrder(node.right)

        return values

root = TreeNode(9)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
dfsInOrder(root)
print(values)

#-------------------------------------------------