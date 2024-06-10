import heapq

def mergeSortedArrays(arrs):
    k = len(arrs)

# heap = (val, arridx, idx)
    heap = [(arrs[arrIdx][0], arrIdx, 0) for arrIdx in range(k)]
    heapq.heapify(heap)
    print(heap)


    res = []

    while heap:
        val, arrIdx, idx = heapq.heappop(heap) # taking the lowest number and it to the solution
        res.append(val)


        if idx + 1 < len(arrs[arrIdx]): # if the array has another value, add to heap
            heapq.heappush(heap, (arrs[arrIdx][idx + 1], arrIdx, idx + 1))

    return res

    # Time O(n log k)
    # Space O(N)