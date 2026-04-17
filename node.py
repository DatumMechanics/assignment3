''' 
This file contains the definition of a node structure for implementing
singly-linked lists that contain integer values.
'''
from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value: int = value
        self.next: Optional[Node] = next

