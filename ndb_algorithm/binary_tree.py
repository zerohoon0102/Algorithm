class Node:
    def __init__(self, value):
        self.value = value
    left_node = None
    right_node = None

def preorder(root):
    print(root.value, end=' ')
    if root.left_node != None:
        preorder(root.left_node)
    if root.right_node != None:
        preorder(root.right_node)
        
def inorder(root):
    if root.left_node != None:
        inorder(root.left_node)
    print(root.value, end=' ')
    if root.right_node != None:
        inorder(root.right_node)

def postorder(root):
    if root.left_node != None:
        postorder(root.left_node)
    if root.right_node != None:
        postorder(root.right_node)
    print(root.value, end=' ')
