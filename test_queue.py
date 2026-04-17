from queue import Queue

if __name__ == "__main__":
    q = Queue()
    assert q.is_empty()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    assert not q.is_empty()
    assert q.front() == 10
    
    assert q.dequeue() == 10
    assert q.front() == 20
    
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    
    assert q.is_empty()
    
    # Clear is safe on an already-empty queue.
    q.clear()
    print('Passed all tests')
