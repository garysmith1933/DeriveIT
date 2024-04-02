def deleteNthToLastNode(head, i):
    dummy = ListNode()
    dummy.next = head 

    def delNth(head, i):
        L, R = head, head

        for _ in range(i+1):
            R = R.next

        while R:
            R = R.next
            L = L.next
        
        L.next = L.next.next
        return head
    
    delNth(dummy, i)
    return dummy.next

    #Time O(N)
    #Space O(1)