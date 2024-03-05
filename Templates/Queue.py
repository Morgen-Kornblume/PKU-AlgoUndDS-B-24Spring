class Queue:
    def __init__(self):
        self.dat = []
        self.head = 0
    
    def is_empty(self):
        return self.head < len(self.dat)

    def push(self, data):
        self.dat.append(data)
    
    def pop(self):
        if(self.is_empty() == False):
            self.head += 1

    def head(self):
        return self.dat[self.head]