from collections import defaultdict
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_unique_heap = []
        inserted = defaultdict(int)
        for num in nums:
            if num not in inserted:
                self.add_to_heap(num, max_unique_heap)
            inserted[num] += 1

        k_acc = 0
        for _ in range(k):
            v = self.remove_from_heap(max_unique_heap)
            k_acc += inserted[v]
            if k_acc >= k:
                return v

        raise "should always be enough to remove k values, they should have count of 1+"

    def add_to_heap(self, node: int, heap: List[int]):
        heap.append(node)
        ix = len(heap) - 1

        while ix > 0:
            parent_ix = (ix - 1) // 2
            if heap[parent_ix] > heap[ix]:
                break
            heap[parent_ix], heap[ix] = heap[ix], heap[parent_ix]
            ix = parent_ix

    def remove_from_heap(self, heap: List[int]) -> int:
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


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
nums = [1]
k = 1
print(Solution().findKthLargest(nums, k))