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
    
    # Test peek()
    q.add(30)
    assert q.peek() == 30, "Test peek() failed"
    
    # Test __contains__()
    assert 30 in q, "Test __contains__() failed"
    assert 40 not in q, "Test __contains__() failed"
    
    # Test __eq__()
    q2 = queue_class()
    q2.add(30)
    assert q == q2, "Test __eq__() failed"
    q2.add(40)
    assert q != q2, "Test __eq__() failed"
    
    # Test clear()
    q.clear()
    assert q.is_empty() == True, "Test clear() failed"
    
    # Test __str__()
    q.add(50)
    assert str(q) == "[50]", "Test __str__() failed"
    
    print(f"All tests passed for {queue_class.__name__}")

   