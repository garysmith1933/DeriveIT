def reverseList(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

    #Time O(N)
    # Space O(1)