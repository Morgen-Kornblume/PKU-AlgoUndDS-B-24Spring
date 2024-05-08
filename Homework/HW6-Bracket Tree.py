class Node:
    def __init__(self, value):
        self.value = value
        self.son = []

class Tree:
    def __init__(self):
        self.root = Node(None)
tree = Tree()


def build_tree(node, st: str):
    node.value = st[0]
    st=st[1:]
    if((len(st)>=1) and st[0]=='('):
        st=st[1:]
        while(True):
            node.son.append(Node(None))
            st = build_tree(node.son[-1],st)
            if(st[0]==','):
                st=st[1:]
            else:
                st=st[1:]
                break
    return st

def traverse1(node):
    if node.value is not None:
        print(node.value, end = "")
    for son in node.son:
        traverse1(son)

def traverse2(node):
    for son in node.son:
        traverse2(son)
    if node.value is not None:
        print(node.value, end = "")

tree_str = input()

build_tree(tree.root, tree_str)

traverse1(tree.root)
print()
traverse2(tree.root)
# A(B(E),C(F,G),D(H(I)))