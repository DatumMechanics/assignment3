"""
Stack implemented using two queues.

This module assumes a Queue class with: enqueue(int), dequeue()->int, front()->int, is_empty()->bool, clear()->None.
"""

from __future__ import annotations
from queue import Queue

class StackFromQueues:
    """
    A LIFO stack implemented using two FIFO queues.
    
    At any time, **exactly one** of q1 or q2 holds all the elements; the other is empty.
    Push appends to the non-empty queue.
    Top/Pop shift elements to expose/remove the most-recently-pushed value.
    """

    def __init__(self) -> None:
        # initialize/create the stack from queues
        self.q1 = Queue()
        self.q2 = Queue()

    def is_empty(self) -> bool:
        """
        Empty and returns True iff both queues are empty.
        """
        pass

    def push(self, value: int) -> None:
        """
        Enqueue into whichever queue is currently non-empty.
        """
        pass

    def _active_and_passive(self):
        """
        Helper: return (start, final) 
        'start' is the currently non-empty queue; 'final' is the empty queue.
        """
        pass

    def top(self) -> int:
        """
        Return the top value *without removing* it.

        Raises:
            AssertionError if the stack is empty.
        """
        pass

    def pop(self) -> int:
        """
        Remove and return the top value.

        Raises:
            AssertionError if the stack is empty.
        """
        pass

    def clear(self) -> None:
        """
        Python's GC handles memory; we call clear() to break links and empty both queues.
        """
        pass

    
