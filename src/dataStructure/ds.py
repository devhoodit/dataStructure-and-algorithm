class Stack():
    def __init__(self, length):
        self.stack = []
        self.max_length = length

    def __len__(self):
        return len(self.stack)

    def is_full(self):
        return len(self.stack) >= self.max_length
    
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        if self.is_full():
            raise IndexError("stack overflow")
        else:
            self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack underflow")
        else:
            return self.stack.pop()

class  ArrayStack():
    def __init__(self, length):
        self.stack = [None for _ in range(length)]
        self.max_length = length
        self.cur_pos = 0

    def __len__(self):
        return self.cur_pos

    def is_full(self):
        return self.cur_pos >= self.max_length

    def is_empty(self):
        return self.cur_pos == 0

    def push(self, data):
        if self.is_full():
            raise IndexError("stack overflow")
        else:
            self.stack[self.cur_pos] = data
            self.cur_pos += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack underflow")
        else:
            self.cur_pos -= 1
            tmp = self.stack[self.cur_pos]
            self.stack[self.cur_pos] = None
            return tmp
            