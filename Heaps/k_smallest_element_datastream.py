class KthSmallestTracker:

    def __init__(self, k):
        self.arr = []
        self.k = k
        
    def add(self, num):
        heap, k = self.arr, self.k

        if len(heap) < k:
            heapq.heappush(heap, -num)
        
        elif num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -num)
   
        
    def getKthSmallest(self): # the heap will always have k elements before it is called. so we can return the first index
        return -self.arr[0]
        
    # Time (add) - O log k (heap contains k numbers, sorted each time)
    # Time (kth smallest) - O(1)
    # Space O(k)