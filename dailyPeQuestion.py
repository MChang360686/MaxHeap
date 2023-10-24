import heapq
# We could code a heap from scratch
# but to make things easier we will use
# the heapq module


# class implementation
class maxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def parent(self, i):
        pass

    def leftChild():
        pass

    def rightChild():
        pass

    def swap(self, a, b):
        # switch A and B
        self[a], self[b] = self[b], self[a]

    def insert():
        pass

    def maxHeapify():
        pass

    def getMax():
        pass

def findKthLargest(nums, k):
    # Convert the given array into a max heap
    # heapq is minheap, so we need to reverse
    # this by using negative numbers
    maxHeap = [-num for num in nums]
    heapq.heapify(maxHeap)

    # Perform k-1 extract-max operations
    # because we want the kth largest num
    for _ in range(k-1):
        heapq.heappop(maxHeap)

    # kth largest element is root heap
    return -maxHeap[0]

if __name__ == '__main__':

    list = [1, 3, 5, 10, 7, 9]

    print(findKthLargest(list, 3))
