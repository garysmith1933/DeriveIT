def listLength(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

# Time O(N)
# Space O(1)