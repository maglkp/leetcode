from typing import List


class MedianFinder:

    def __init__(self):
        # left side heap
        self.max_heap = []
        # right side heap
        self.min_heap = []

    def addNum(self, num: int) -> None:

        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            # add to the left side
            self.add_to_max_heap(num)
            return

        median = self.findMedian()
        if len(self.max_heap) == len(self.min_heap):
            if num < median:
                # add to the left side
                self.add_to_max_heap(num)
            else:
                # add to the right side
                self.add_to_min_heap(num)
        # we have more values on the right side
        elif len(self.min_heap) > len(self.max_heap):
            if num <= median:
                # add to the left side
                self.add_to_max_heap(num)
            else:
                # number should go to the right side but it already has more than the left side
                # pop one element from the right side and add it to the left side
                to_transfer = self.remove_from_min_heap()
                self.add_to_max_heap(to_transfer)

                # add to the left side
                self.add_to_min_heap(num)
        # we have more values on the left side
        else:
            if num >= median:
                # add to the left side
                self.add_to_min_heap(num)
            else:
                # number should go to the left side but it already has more than the right side
                # pop one element from the left side and add it to the right side
                to_transfer = self.remove_from_max_heap()
                self.add_to_min_heap(to_transfer)

                # add to the left side
                self.add_to_max_heap(num)

    def add_to_max_heap(self, node: int):
        heap = self.max_heap
        heap.append(node)
        ix = len(heap) - 1

        while ix > 0:
            parent_ix = (ix - 1) // 2
            if heap[parent_ix] > heap[ix]:
                break
            heap[parent_ix], heap[ix] = heap[ix], heap[parent_ix]
            ix = parent_ix

    def add_to_min_heap(self, node: int):
        heap = self.min_heap
        heap.append(node)
        ix = len(heap) - 1

        while ix > 0:
            parent_ix = (ix - 1) // 2
            if heap[parent_ix] < heap[ix]:
                break
            heap[parent_ix], heap[ix] = heap[ix], heap[parent_ix]
            ix = parent_ix

    def remove_from_min_heap(self) -> int:
        heap = self.min_heap
        v = heap[0]
        last = heap.pop()
        if len(heap) > 0:
            heap[0] = last
            ix = 0
            while ix < len(heap):
                left = 2 * ix + 1
                right = 2 * ix + 2
                smallest = ix

                if left < len(heap) and heap[left] < heap[smallest]:
                    smallest = left
                if right < len(heap) and heap[right] < heap[smallest]:
                    smallest = right
                if smallest != ix:
                    heap[ix], heap[smallest] = heap[smallest], heap[ix]
                    ix = smallest
                else:
                    break

        return v

    def remove_from_max_heap(self) -> int:
        heap = self.max_heap
        v = heap[0]
        last = heap.pop()
        if len(heap) > 0:
            heap[0] = last
            ix = 0
            while ix < len(heap):
                left = 2 * ix + 1
                right = 2 * ix + 2
                largest = ix

                if left < len(heap) and heap[left] > heap[largest]:
                    largest = left
                if right < len(heap) and heap[right] > heap[largest]:
                    largest = right
                if largest != ix:
                    heap[ix], heap[largest] = heap[largest], heap[ix]
                    ix = largest
                else:
                    break
        return v

    def findMedian(self) -> float:

        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2


# mf = MedianFinder()
# mf.addNum(1)
# mf.addNum(2)
# print(mf.findMedian())
# mf.addNum(3)
# print(mf.findMedian())

# mf = MedianFinder()
# mf.addNum(-1)
# print(mf.findMedian())
# mf.addNum(-2)
# print(mf.findMedian())
# mf.addNum(-3)
# print(mf.findMedian())
# mf.addNum(-4)
# print(mf.findMedian())
# mf.addNum(-5)
# print(mf.findMedian())


mf = MedianFinder()
mf.addNum(1)
print(mf.findMedian())

mf.addNum(2)
print(mf.findMedian())

mf.addNum(3)
print(mf.findMedian())

mf.addNum(4)
print(mf.findMedian())

mf.addNum(5)
print(mf.findMedian())

mf.addNum(6)
print(mf.findMedian())
