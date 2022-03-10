from collections.abc import Sequence

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

class Heap():
    class Heap():
        def __init__(self):
            self.heap = [None]
            self.size = 0

        def __len__(self):
            return self.size
        
        def __iter__(self):
            return self

        def __next__(self):
            if self.size <= 0:
                raise StopIteration
            return self.pop()

        def is_empty(self):
            return self.size <= 0

    class MaxHeap(Heap):
        def push(self, value):
            self.heap.append(value)
            self.size += 1
            i = self.size
            while i != 1 and value > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
                i //= 2
        
        def pop(self):
            if self.is_empty():
                raise IndexError()
            tmp = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.size -= 1

            parent = 1
            child = 2

            while child <= self.size:

                if child+1 < self.size and self.heap[child] < self.heap[child+1]: #check parent node have enough child node(2 nodes), and find which child node is bigger(guarantee parent node is bigger than child nodes when swap)
                    child += 1
                
                if self.heap[child] > self.heap[parent]:
                    self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                else:
                    break

                parent = child
                child *= 2

            return tmp

    class MinHeap(Heap):
        def push(self, value):
            self.heap.append(value)
            self.size += 1
            i = self.size
            while i != 1 and value < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
                i //= 2

        def pop(self):
            if self.is_empty():
                raise IndexError()
            tmp = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.size -= 1

            parent = 1
            child = 2

            while child < self.size:

                if child+1 < self.size and self.heap[child] > self.heap[child+1]:
                    child += 1
                
                if self.heap[child] < self.heap[parent]:
                    self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                else:
                    break

                parent = child
                child *= 2

            return tmp
