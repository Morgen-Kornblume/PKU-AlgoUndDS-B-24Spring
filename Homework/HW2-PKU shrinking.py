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


PKU = Stack()

def judge3() -> bool:
    if PKU.size() < 3:
        return False
    else:
        if PKU._items[-3] == 'P' and PKU._items[-2] == 'K' and PKU._items[-1] == 'U':
            return True
        else:
            return False

tmp = input()

for x in tmp:
    PKU.push(x)
    if judge3():
        PKU.pop()
        PKU.pop()
        PKU.pop()
for x in PKU._items:
    print(x, end = '')