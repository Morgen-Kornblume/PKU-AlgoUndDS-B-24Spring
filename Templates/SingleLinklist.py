# 标准模板，链表类
class SingleLinklist:
    '''
    这个类是一个单链表的标准模板
    '''
    class Node:
        '''
        链表节点，包含数据和指向下一个节点的指针
        '''
        def __init__(self, data, next=None):
            '''
            初始化节点
            '''
            self.data = data
            self.next = next
    
    def __init__(self):
        '''
        初始化链表
        '''
        self.head = None
        self.tail = None
        self.size = 0
    
    def print_all(self):
        '''
        打印链表中的所有元素的数据（从头到尾）
        '''
        p = self.head
        while p is not None:
            print(p.data, end=' ')
            p = p.next
        print()
    
    def insert_head(self, data):
        '''
        在链表头部插入一个节点，其数据为 data
        '''
        if self.head is None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.head = self.Node(data, self.head)
        self.size += 1
    
    def insert_tail(self, data):
        '''
        在链表尾部插入一个节点，其数据为 data
        '''
        if self.tail is None:
            self.tail = self.Node(data)
            self.head = self.tail
        else:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        self.size += 1
    
    def insert_after(self, p, data):
        '''
        在指定节点 p 后插入一个节点，其数据为 data
        '''
        if p is None:
            return
        if p is self.tail:
            self.insert_tail(data)
        else:
            new_node = self.Node(data, p.next)
            p.next = new_node
            self.size += 1
    
    def remove_head(self):
        '''
        删除链表头部的节点
        '''
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
    
    def remove_tail(self):
        '''
        删除链表尾部的节点
        '''
        if self.tail is None:
            return
        if self.head is self.tail: # 只有一个节点
            self.head = None
            self.tail = None
            self.size -= 1
            return
        p = self.head
        while p.next is not self.tail:
            p = p.next
        p.next = None
        self.tail = p
        self.size -= 1

    def remove_after(self, p):
        '''
        删除指定节点 p 后的节点
        '''
        if p is None or p.next is None:
            return
        if p.next is self.tail:
            self.remove_tail()
        else:
            p.next = p.next.next
            self.size -= 1

    def size(self) -> int:
        '''
        返回链表的长度(int)
        '''
        return self.size
    
    def clear(self):
        '''
        清空链表
        '''
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        '''
        判断链表是否为空
        '''
        return self.size == 0

    # 实现 __iter__ 和 __next__ 方法，使得链表对象可以被迭代
    def __iter__(self):
        self._iter = self.head
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration
        else:
            data = self._iter.data
            self._iter = self._iter.next
            return data