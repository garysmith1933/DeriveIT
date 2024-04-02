def delete(head, i):
    current = head

    if i == 0:
        return current.next 

    for _ in range(i-1):
        current = current.next
    
    current.next = current.next.next 
    return head

    # Time O(N)
    # Space O(1)