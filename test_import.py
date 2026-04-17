
# verify_node_import.py
import inspect
import node

print("Loaded node from:", node.__file__)

from node import Node

# Show the source code of the Node class to confirm it defines `self.next`
try:
    print("\nNode class source:\n")
    print(inspect.getsource(Node))
except OSError:
    print("\nCould not retrieve Node source; it may be a built-in or compiled module.")
    print
                        
