class Node:                      #  كل عنصر في الستاك عبارة عن نود   
    def __init__(self, data=None, next=None): 
        self.data = data         #  data  → القيمة
        self.next = next         #  next  → يشير للعنصر اللي بعده


    #       [1]      → [5] → [9] → [3] → None شكل النكد لست
    #  [head or top] → [5] → [9] → [3] → None         
class Stack:                             
    def __init__(self):         # تخيلها مثل كومة كتب 📚, تضيف من الأعلى , تشيل من الأعلى
        self.top = None         # top →  رأس الستاك يشير لأعلى عنصر في الستاك - دائماً يكون العنصر الأخير اللي تم إضافته
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = Node(value)
        # If list is empty just point the header to the new node
        if not self.top:
            self.top = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self.top
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    


if __name__ == "__main__":
    stack = Stack()
    print("Testing push: ")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(2)

    print(stack.top.data)  # Output: 2
    print(stack.top.next.data)  # Output: 30
    print(stack.top.next.next.data)  # Output: 20
    print(stack.top.next.next.next.data)  # Output: 10
    print(stack.top.next.next.next.next)  # Output: None


    print("\nTesting pop: ")
    print(stack.pop())  # Output: 2
    print(stack.pop())  # Output: 30
    print(stack.top.data)  # Output: 20



    print("\nTesting peek: ")
    print(stack.peek())  # Output: 20


    print("\nTesting is_empty: ")
    print(stack.is_empty())  # Output: False
    stack.pop()
    stack.pop()
    print(stack.is_empty())  # Output: True


    print("\nTesting append: ")    
    stack.append(5)
    stack.append(15)
    stack.append(25)
    
    print(stack.top.data)  # Output: 5
    print(stack.top.next.data)  # Output: 15
    print(stack.top.next.next.data)  # Output: 25
    print(stack.top.next.next.next)  # Output: None