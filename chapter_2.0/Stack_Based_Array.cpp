// Explanation of Stack Based Array Implementation in C++:

// Add, Remove, and Retrieve elements from the stack using an array as the underlying data structure. The stack follows the Last In First Out (LIFO) principle, 
// where the last element added is the first one to be removed. The implementation includes functions to check if the stack is empty, 
// push new elements onto the stack, pop elements from the stack, retrieve the top element without removing it, and print the contents of the stack. 
// The main function demonstrates these operations by creating a stack of integers, performing a series of push and pop operations, and printing the final state of the stack.

#include<iostream>
using namespace std;

const int MAX_SIZE = 3; 	// Step 1: Maximum size of the stack 3 indexes 0,1,2
template<class t> 			// Template class to allow stack of any data type

class stack {
	int top;
	t items[MAX_SIZE];		// Step 2: Array to hold stack items

public:
	stack() :top(-1) {}		// Step 3: Constructor initializes top to -1 indicating an empty stack

	bool isEmpty()			// Step 4: Function to check if the stack is empty
	{
		return top < 0;
	}

	void push(t Element)	// Step 5: Function to add an element to the top of the stack
	{
		if (top >= MAX_SIZE-1)
		{
			cout << "Stack full on push";
		}
		else
		{
			top++;
			items[top] = Element;
		}
	}

	void pop() 				// Step 6: Function to remove the top element from the stack
	{
		if (isEmpty())
			cout << "stack empty on pop";
		else
			top--;
	}

	void pop(t&Element)
	{
		if (isEmpty())
			cout << "stack empty on pop";
		else {
			Element = items[top];
			top--;
		}
	}

	void getTop(t&stackTop) // Step 7: Function to retrieve the top element of the stack without removing it
	{
		if (isEmpty())
			cout << "stack empty on getTop";
		else {
			stackTop = items[top];
			cout << stackTop << endl;
		}
	}

	void print()			// Step 8: Function to print the contents of the stack from top to bottom
	{	
		cout << "[ ";
		for (int i = top; i >= 0; i--) // Reverse order becuz of the top always points to the last inserted element: Loop to print stack elements starting from the top 
		{
			cout << items[i] << " ";
		}
		cout << "]";
		cout << endl;

	}
};

int main()					// Step 9: Main function to demonstrate the stack operations
{
	stack<int>s;
	s.push(5);
	s.push(15);
	s.push(20);
	s.pop(); // Remove the top element (20)
	s.push(25); // Add a new element (25) to the stack;
	s.print(); // Expected output: [ 25 15 5 ] because 20 was removed and 25 was added on top of the stack
}