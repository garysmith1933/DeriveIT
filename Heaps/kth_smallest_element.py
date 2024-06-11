def kthSmallestElement(arr, k):
    heapq.heapify(arr) # O(N) time

    i = 0

    while i < k:
        num = heapq.heappop(arr) # log n which we do k times
        i += 1

        if i == k:
            return num

    # Time O(n + k log n) 
    # Space O(1)