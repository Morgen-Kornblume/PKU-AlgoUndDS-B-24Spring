

class Node:
    def __init__(self, value, char=None):
        self.char = char
        self.value = value
        self.left = None
        self.right = None

    def __lt__(self, other):
        if(self.value == other.value):
            return self.char < other.char
        return self.value < other.value

def swap(a , b):
    return b, a

def merge(node1, node2):
    root = Node(node1.value + node2.value, min(node1.char, node2.char))
    if node1 > node2:
        node1, node2 = swap(node1, node2)
    root.left = node1
    root.right = node2
    return root

map = {}
def traverse(node, str):
    global map
    if node.left == None and node.right == None:
        map[node.char] = str
        return
    if node.left != None:
        traverse(node.left, str + "0")
    if node.right != None:
        traverse(node.right, str + "1")
    return

def calc(node, rem):
    if(node.left == None and node.right == None):
        print(node.char, end="")
        return rem
    if rem[0] == "0":
        return calc(node.left, rem[1:])
    else:
        return calc(node.right, rem[1:])

n = int(input())
nodes = []

for i in range(n):
    char, value = input().split()
    value = int(value)
    nodes.append(Node(value, char))


while len(nodes) > 1:
    nodes.sort()
    node1 = nodes.pop(0)
    node2 = nodes.pop(0)
    nodes.append(merge(node1, node2))

traverse(nodes[0], "")



#print(map)

while True:
    try:
        str = input()
        #print(str)
        if(str[0]=='0' or str[0]=='1'):
            while len(str) > 0:
                str = calc(nodes[0], str)
            print("")
        else:
            for ch in str:
                #print(ch)
                print(map[ch], end="")
            print("")
    except:
        break