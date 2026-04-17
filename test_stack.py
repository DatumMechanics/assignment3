from stack import Stack

if __name__ == "__main__":
    
    s = Stack()
    assert s.is_empty()

    s.push(10)
    s.push(20)
    s.push(30)
    
    s.print_stack()

    assert not s.is_empty()
    assert s.peek() == 30
    
    assert s.pop() == 30
    s.print_stack()
    assert s.peek() == 20
    
    assert s.pop() == 20
    s.print_stack()
    assert s.pop() == 10
    
    assert s.is_empty()
    
    # Safe on empty
    s.clear()
    print("Quick stack test passed.")
