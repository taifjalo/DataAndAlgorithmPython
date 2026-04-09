# Explanation of Stack Based Array Implementation in Python:

# Add, Remove, and Retrieve elements from the stack using an array as the underlying data structure. The stack follows the Last In First Out (LIFO) principle, 
# where the last element added is the first one to be removed. The implementation includes functions to check if the stack is empty, 
# push new elements onto the stack, pop elements from the stack, retrieve the top element without removing it, and print the contents of the stack. 
# The main function demonstrates these operations by creating a stack of integers, performing a series of push and pop operations, and printing the final state of the stack.


class Stack:
    def __init__(self, max_size):
        
        self.max_size = max_size
        self.top = -1 # Initialize top index to -1 to indicate an empty stack
        self.items = [None] * max_size

    def is_Empty(self):
        return self.top < 0
    
    def push(self, element):
        if self.top >= self.max_size - 1:
            print("Stack overflow on push")
        else:
            self.top += 1  # Increment top index to point to the new top position
            self.items[self.top] = element

    def pop(self):
        if self.is_Empty():
            print("Stack empty on pop")
        else:
            element = self.items[self.top]  # Get the top element
            self.top -= 1  # Decrement top index
            return element
        
    def get_Top(self):
        if self.is_Empty():
            print("Stack empty on get_Top")
        else:
            stack_top = self.items[self.top]  # Get the top element
            print(stack_top)

    def print_Stack(self):
        print("[ ", end="")
        for i in range(self.top, -1, -1):  # Print from top to bottom
            print(self.items[i], end=" ")
        print("]")
    
# Example usage
if __name__ == "__main__":
    s = Stack(10)  # Create a stack with max size of 10
    s.push(5)
    s.push(15)
    s.push(20)
    s.pop()  # Remove the top element (20)
    s.push(25) # Add a new element (25) to the stack;
    s.get_Top()  # Print the current top element (25)
    s.print_Stack()  # Expected output: [ 25 15 5 ] because 20 was removed and 25 was added on top of the stack