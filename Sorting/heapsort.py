def heapSort(arr):
    heapq.heapify(arr)
    res = []

    while arr:
        num = heapq.heappop(arr)
        res.append(num)
    
    return res

    # Time O(n log n)
    # Space O(1)