""" 
This module contains the definition of a Stack class implementing a simple stack (LIFO) 
using a singly-linked list of Node objects. 
"""

from __future__ import annotations 
from typing import Optional
from node import Node 
import inspect

class Stack:

    """ 
    A LIFO stack implemented via a singly-linked list. Maintains a pointer to the top 
    node. 
    """ 

    def __init__(self) -> None:
        # start with an empty stack. 
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        """ 
        Returns True if the stack has no elements. 
        """ 
        return self.top is None

    def push(self, value: int) -> None:
        """
        Pushes a value onto the top of the stack. 
        """ 

        # Instantiate a Node. 
        new_node = Node(value, next=self.top) 
        self.top = new_node

    def peek(self) -> int:
        """ 
        Returns value without removing the element. 
        
        Raises:
            AssertionError if the stack is empty.
        """ 
        if self.top is not None:
            return self.top.value
        else:
            return None

    def pop(self) -> int:
        """ 
        Removes and returns the value from the top of the stack. 

        Raises:
            AssertionError if the stack is empty.
        """ 

        assert self.top is not None, "pop() called on empty stack" 

        popped_top = self.top 
        value = popped_top.value 
        self.top = popped_top.next 

        # Help garbage collection by breaking the link. 
        popped_top.next = None 
        return value

    def clear(self) -> None:
        """ 
        Iteratively pops all elements to break links. 
        (Python's garbage collector manages memory automatically.) 
        """
        while not self.is_empty():
            self.pop()

    def print_stack(self) -> None:
        
        print('current stack:')
        print('   top')
        curr = self.top
        while curr is not None:
            print(f'  {curr.value}')
            curr = curr.next
        print('   bottom')
        print() # print a new line
