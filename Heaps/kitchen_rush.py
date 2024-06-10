import heapq
class KitchenOrders:

    def __init__(self):
        self.orders = []
        
    def add(self, number):
        heapq.heappush(self.orders, number)
        
    def getLowest(self):
        return self.orders[0]
        
    def removeLowest(self):
        heapq.heappop(self.orders)

    # get time O(1)
    # add time O(log n)
    # remove time O(log n)
    # space O(N)