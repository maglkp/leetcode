from typing import List, Tuple


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # sort the projects according to their cost (capital), create tuples with capital, profits
        projects = sorted([(c, p) for c, p in zip(capital, profits)], key=lambda x: x[0])

        # create a max heap
        heap = []
        for _ in range(k):
            while projects and projects[0][0] <= w:
                self.add_to_heap(projects.pop(0), heap)
            if not heap:
                break
            w += self.remove_from_heap(heap)[1]

        return w

    def add_to_heap(self, node: Tuple[int, int], heap: List[Tuple[int, int]]):
        heap.append(node)
        ix = len(heap) - 1

        while ix > 0:
            parent_ix = (ix - 1) // 2
            if heap[parent_ix][1] > heap[ix][1]:
                break
            heap[parent_ix], heap[ix] = heap[ix], heap[parent_ix]
            ix = parent_ix

    def remove_from_heap(self, heap: List[Tuple[int, int]]) -> Tuple[int, int]:
        v = heap[0]
        last = heap.pop()
        if len(heap) > 0:
            heap[0] = last
            ix = 0
            while ix < len(heap):
                left = 2 * ix + 1
                right = 2 * ix + 2
                largest = ix

                if left < len(heap) and heap[left][1] > heap[largest][1]:
                    largest = left
                if right < len(heap) and heap[right][1] > heap[largest][1]:
                    largest = right
                if largest != ix:
                    heap[ix], heap[largest] = heap[largest], heap[ix]
                    ix = largest
                else:
                    break

        return v


k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]

s = Solution()
print(s.findMaximizedCapital(k, w, profits, capital))
