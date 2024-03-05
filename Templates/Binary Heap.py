class BinaryHeap:
    '''
    二叉堆模板，默认为大根堆
    '''
    def __init__(self):
        self.dat = [0]
        self.size = 1
    
    def upload(self, nowa):
        '''
        向上调整节点（大根堆）
        '''
        x = nowa
        while(x > 1 and self.dat[x].data > self.dat[x // 2].data):
            self.dat[x], self.dat[x // 2] = self.dat[x // 2], self.dat[x]
            x = x // 2

    def insert(self, data):
        '''
        插入一个新的点，数据为 data（data必须可以比较）
        '''
        self.size += 1
        self.dat.append(data)
        self.upload(self.size)

    def download(self):
        '''
        删除堆顶后向下调整
        '''
        nowa = 1
        while(nowa * 2 <= self.size):
            tmp = nowa * 2
            if(tmp + 1 <= self.size and self.dat[tmp + 1] > self.dat[tmp]):
                t += 1
            if(self.dat[tmp] < self.dat[nowa]):
                break
            self.dat[tmp], self.dat[nowa] = self.dat[nowa], self.dat[tmp]
            nowa = tmp

    def pop(self):
        '''
        弹出堆顶元素
        '''
        if(self.size > 0):
            self.dat[1], self.dat[self.size] = self.dat[self.size], self.dat[1]
            self.dat.pop()
            self.size -= 1
            self.download()


