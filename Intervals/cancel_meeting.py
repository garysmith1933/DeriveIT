def cancelMeetings(head, meeting): # [0, 1] [1. 3]   [ 2, 3]
    current = head
    prev = None

    while current:
        if current.val[1] > meeting[0]: break # not overlapping
        prev = current
        current = current.next
            
        
    while current:
        if current.val[0] >= meeting[1]: break
        current = current.next
    

    if not prev:
        return current
    

    prev.next = current

    return head

    # Time O(N)
    # Space O(N)