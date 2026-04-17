class StackBasedQueue():

    def __init__(self):
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
    
        values = [str(c) for c in self._InboundStack[::-1]]
        values.extend([str(c) for c in self._OutboundStack])

        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'
    
    
    # _InboundStack = []
    def enqueue(self, data):
        self._InboundStack.append(data)   # _InboundStack = [A, B, C]
        self._size += 1

    # _OutboundStack = []
    def dequeue(self):
        # if _OutboundStack list are empty move the items which  appended to first list. and delete the first one
        if not self._OutboundStack:                                     # if _OutboundStack = []
            while self._InboundStack:                                   # while _OutboundStack = []
                self._OutboundStack.append(self._InboundStack.pop())    # Add _InboundStack = [A, B, C] items to _OutboundStack = []: --> 
                                                                                                               # _OutboundStack = [C, B, A] 
        # if after moving items from _InboundStack, and are both empty return None.
        if not self._OutboundStack:
            return None

        self._size -= 1
        return self._OutboundStack.pop()
    

if __name__ == "__main__":
    queue = StackBasedQueue()
    
    print(queue)            # <StackBasedQueue (0 elements): []>

    queue.enqueue('A')      # _InboundStack = ['A']
    queue.enqueue('B')      # _InboundStack = ['A', 'B']
    queue.enqueue('C')      # _InboundStack = ['A', 'B', 'C']
    print(queue)            # <StackBasedQueue (3 elements): [A, B, C]>

    val = queue.dequeue()   # _OutboundStack = ['C', 'B', 'A'] --> _OutboundStack = ['C', 'B'] and return 'A'
    print(val, queue)

    val = queue.dequeue()   # _OutboundStack = ['C', 'B'] --> _OutboundStack = ['C'] and return 'B' 
    print(val, queue)
