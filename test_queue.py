def test_queue(queue_class):
    q = queue_class()
    
    # Test is_empty()
    assert q.is_empty() == True, "Test is_empty() failed"
    
    # Additional tests to be added here

    print(f"All tests passed for {queue_class.__name__}")
