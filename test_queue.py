def test_queue(queue_class):
    q = queue_class()
    
    # Test is_empty()
    assert q.is_empty() == True, "Test is_empty() failed"
    
    # Test __len__()
    assert len(q) == 0, "Test __len__() failed"
    q.add(10)
    assert len(q) == 1, "Test __len__() after add() failed"
    
    # Test add() and pop()
    q.add(20)
    assert q.pop() == 10, "Test pop() failed"
    assert q.pop() == 20, "Test pop() failed"
    assert q.is_empty() == True, "Test is_empty() after pop() failed"
    
    print(f"All tests passed for {queue_class.__name__}")
