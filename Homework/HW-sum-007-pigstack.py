class Stack:
    '''
    List based implementation of Stack（列表模拟栈）
    '''
    def __init__(self):
        self._items = []
    def is_empty(self):
        return not bool(self._items)
    def push(self, item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def size(self):
        return len(self._items)
    
pigstack = Stack()
minstack = Stack()
minn = 1048576
while True:
    try:
        s = input().split()
        if s[0] == 'push':
            x = int(s[1])
            pigstack.push(x)
            if minstack.is_empty() or x <= minstack.peek():
                minstack.push(x)
                minn = x
        elif s[0] == 'pop':
            if pigstack.is_empty() == False:
                if pigstack.peek() == minstack.peek():
                    if(minstack.peek()==minn):
                        minstack.pop()
                        if(minstack.is_empty() == False):
                            minn = minstack.peek()
                    else:
                        minstack.pop()
                pigstack.pop()
        elif s[0] == 'min':
            if(minstack.is_empty() == False):
                print(minstack.peek())
    except:
        break