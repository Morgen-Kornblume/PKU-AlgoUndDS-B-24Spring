# Build a binary tree from sequence of left-first and right-first traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build(mseq, pseq):
    global tree
    if len(mseq) == 0:
        return None
    root = Node(pseq[-1])
    
    if len(mseq) == 1:
        return root
    root_index = mseq.index(pseq[-1])
    root.left=build(mseq[:root_index], pseq[:root_index])
    root.right=build(mseq[root_index+1:], pseq[root_index:-1])
    return root

def traverse(node):
    
    print(node.value, end="")
    if node.left != None:
        traverse(node.left)
    if node.right != None:
        traverse(node.right)
    return

mseq = input()#middle-first
pseq = input()#post-first

traverse(build(mseq, pseq))