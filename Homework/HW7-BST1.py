class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(nowa , data):
    if(nowa.data == data):
        return
    if(data < nowa.data):
        if(nowa.left == None):
            nowa.left = Node(data)
        else:
            insert(nowa.left, data)
    else:
        if(nowa.right == None):
            nowa.right = Node(data)
        else:
            insert(nowa.right, data)

def traverse(rt):
    #创建一个QUEUE来实现BFS
    queue = []
    queue.append(rt)
    while len(queue) > 0:
        #pop出第一个元素
        node = queue.pop(0)
        print(node.data, end = ' ')
        #如果左子树不为空，就加入到QUEUE中
        if node.left != None:
            queue.append(node.left)
        #如果右子树不为空，就加入到QUEUE中
        if node.right != None:
            queue.append(node.right)

#读取输入
seq = list(map(int, input().split()))

root = Node(seq[0])

for i in seq[1:]:
    insert(root, i)

traverse(root)