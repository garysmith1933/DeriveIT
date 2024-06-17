class MedianTracker:
    
    def __init__(self): # initialize the object
        self.heap = []
        
    def add(self, num): # add `num` to the numbers we've seen
        self.heap.append(num)
        
    def getMedian(self): # return median number we've seen so far
        heap = self.heap
        self.heap.sort()

        if len(heap) % 2 == 0: # even
            highmid = len(heap) // 2
            lowmid = highmid - 1

            mid = (heap[highmid] + heap[lowmid]) / 2
            return mid
        
        else: # odd
            mid = len(heap) // 2
            return heap[mid]