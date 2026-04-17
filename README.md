# Assignment 3

This assignment is intended to have you start working with stacks, queues, and linked lists.  
There are several parts to the assignment, each described below.

For this assignment, you are provided with some starter code that defines the structures 
you'll be working with and prototypes the functions you'll be writing.  

*It's important that you don't modify the function names.*  

To help grade your assignment, we will use a set of unit tests that assume these functions
exist and have the same names that are defined in the starter code.  If you change the
prototypes, such as the names of the prototypes, it will cause the unit tests to break, and
your grade for the assignment will likely suffer.  Feel free, however, to write any additional
functions you need to accomplish the tasks described below.

In this assignment, your work will be limited to the files `list_reverse.py`, 
`queue_from_stacks.py`, and `stack_from_queues.py`, where you will implement the functions 
described below. In addition to the descriptions below, there is thorough documentation 
in these files describing how each function should behave. 

## 1. Implement a function to reverse a linked list in place

In `node.py`, a simple structure implementing a node in a singly-linked list is defined.  
For this part of the assignment, you will implement a function called `list_reverse()` that 
takes as an argument a single node structure representing the pointer to the first node of a 
linked list "first", reverses that list, and returns the new pointer to the first node of 
the reversed list.  This function is defined in `list_reverse.py`, and you will implement 
the function logic **Importantly, you must perform the list reversal in place and may 
not allocate any new memory in this function.**

## 2. Implement a queue using two stacks

In the file `stack.py`, a simple stack is implemented using a linked list.
For the second part of this assignment, you will use two instances of this stack code to 
implement a queue.  In other words, you will implement a queue that uses two stacks to 
form the underlying container in which data is stored (instead of, for example, a dynamic 
array or a linked list).  For example, when the user calls `enqueue()` on your 
queue-from-stacks data structure, it will add the newly-enqueued element into one of the 
two stacks, as appropriate, and when the user calls `dequeue()`, your queue-from-stacks will 
remove the appropriate element from one of the two stacks.  To the user of your queue-from-stacks, 
it will behave just like a normal queue.

The interface of your queue-from-stacks is defined in `queue_from_stacks.py`, and you must 
complete each of the functions implementing the queue-from-stacks in `queue_from_stacks.py`.  
Each of the functions in `queue_from_stacks.py` has a function header comment that describes 
more precisely how it should behave.

Importantly, you may only use the functions prototyped in `stack.py` to interface with your 
two stacks, and you may not access the underlying data directly.  Also, make sure your 
queue-from-stacks implementation does not have any memory leaks!

> Hint: think of one stack as an "inbox" and one stack as an "outbox".

## 3. Implement a stack using two queues

In the file `queue.py`, a simple queue data structure is implemented.  
For the third part of this assignment, you will use two instances of this queue data structure 
to implement a stack.  In other words, you will implement a stack that uses two queues to form 
the underlying container in which data is stored (instead of, for example, a dynamic array or a 
linked list).  For example, when the user calls `push()` on your stack-from-queues data structure, 
it will add the newly-pushed element into one of the two queues, as appropriate, and when the 
user calls `pop()`, your stack-from-queues will remove the appropriate element from one of the 
two queues.  To the user of your stack-from-queues, it will behave just like a normal stack.

The interface of your stack-from-queues is defined in `stack_from_queues.py`, and you must complete 
each of the functions implementing the stack-from-queues in `stack_from_queues.py`.  Each of the 
functions in `stack_from_queues.py` has a function header comment that describes more precisely how 
it should behave.

Importantly, you may only use the functions prototyped in `queue.py` to interface with your two queues, 
and you may not access the underlying data directly.  Also, make sure your stack-from-queues 
implementation does not have any memory leaks!

> Hint: there are two possible implementations of the stack-from-queues, one with an expensive pop 
operation and an efficient push operation, and one with an expensive push operation and an efficient 
pop operation.  Whichever of these you choose to implement, the key is knowing where in your two 
queues the most recently pushed element is.  This is always the next element to be popped from the stack.

## Testing your work

In addition to the starter code provided, you are also provided with some application code in `main.py`
and some other functions like `test_import.py` that could form the basis of other tests you would do. 
to help verify that your functions are behaving the way you want them to.  In particular, the code in 
`main.py` calls the functions you'll implement in this assignment, passing them appropriate arguments, 
and then prints the results.  

You can see some example output from a correct solution to the assignment in the file `example_output.txt`.

## Submission

As always, we'll be using Gradescope. Further instructions will be posted on the Canvas assignment page.
The upload should contian `list_reverse.py`, `queue_from_stacks.py`, and `stack_from_queues.py` when grading
your work.  Changes to other files will be ignored.


## Grading criteria

To grade your work, the TAs will use the tests in `main.py` Your programs should
run on `flip.engr.oregonstate.edu`, so make sure you have tested your work there before you 
make your final submission, since a program that compiles and runs in one environment may not compile 
and run in another.  **Assignments that do not compile on flip will receive a grade of 0.**  If you do 
not have an ENGR account, you can create one at https://teach.engr.oregonstate.edu/.

The assignment is worth 100 total points, broken down as follows:

* 20 points: `list_reverse()` works as described above
* 30 points: all functions in your queue-from-stacks implementation correctly implement a queue
* 30 points: all functions in your stack-from-queues implementation correctly implement a stack
* 20 points for assignment 3 demo

The autograder will only produce 80 points

Note that we will only consider changes to `list_reverse.py`, `queue_from_stacks.py`, and 
`stack_from_queues.py` when grading your work.  Changes to other files will be ignored.
