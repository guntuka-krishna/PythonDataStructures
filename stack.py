'''
STACK: Stack is an abstract data type with a bounded(predefined) capacity.
       It is a simple data structure that allows adding and removing elements
       in a particular order. Every time an element is added, it goes on the top of the stack,
       the only element that can be removed is the element that was at the top of the stack, just like a pile of objects.

Features of Stack Data Structure:

1) Stack is an ordered list of similar data type.
2) Stack is a LIFO structure. (Last in First out).
3) push() function is used to insert new elements into the Stack and pop() function is used to delete
   an element from the stack. Both insertion and deletion are allowed at only one end of Stack called Top.
4) Stack is said to be in Overflow state when it is completely full and is said to be in Underflow state if it is completely empty.

'''

#stack class
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def view(self):
        for val in self.stack:
            print(val, end=" ")
        print()


