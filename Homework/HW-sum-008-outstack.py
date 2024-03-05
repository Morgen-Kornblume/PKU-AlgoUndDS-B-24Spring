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
        self._items.pop()
    def peek(self):
        return self._items[-1]
    def size(self):
        return len(self._items)
    
ori = input()


while True:
    try:
        tmp = input()
        #print('here')
        ptr = 0
        stk = Stack()
        for x in ori:
            #print(x)
            stk.push(x)
            while(stk.is_empty() == False and ptr < len(tmp) and stk.peek() == tmp[ptr] ):
                stk.pop()
                ptr += 1
        if(stk.is_empty()):
            print('YES')
        else:
            print('NO')
    except:
        break