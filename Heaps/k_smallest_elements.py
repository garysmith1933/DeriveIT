def kSmallestElements(arr, k):
    res = []
    heapq.heapify(arr)

    while len(res) != k:
        res.append(heapq.heappop(arr))
    
    return res