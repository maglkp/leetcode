from typing import Optional


class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key: int = key
        self.value: int = value

        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}
        self.leastRecentlyUsed: Optional[Node] = None
        self.mostRecentlyUsed: Optional[Node] = None

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        entry = self.cache[key]
        v = entry.value

        if entry != self.mostRecentlyUsed:
        # or
        # if entry.prev is not None:
            #if entry is not self.leastRecentlyUsed:
            # or
            if entry.next is not None:
                # it was in the middle
                entry.prev.next = entry.next
                entry.next.prev = entry.prev
                self.mostRecentlyUsed.prev = entry
                entry.next = self.mostRecentlyUsed
                self.mostRecentlyUsed = entry
            else:
                # it was the least recently used
                entry.prev.next = None
                self.leastRecentlyUsed = entry.prev
                entry.prev = None
                entry.next = self.mostRecentlyUsed
                self.mostRecentlyUsed.prev = entry
                self.mostRecentlyUsed = entry

        return v

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            entry = self.cache[key]
            entry.value = value
            if entry != self.mostRecentlyUsed:
                # or
                # if entry.prev is not None:
                if entry is not self.leastRecentlyUsed:
                    # is in the middle
                    # or
                    # if entry.next is not None:
                    entry.prev.next = entry.next
                    entry.next.prev = entry.prev
                    self.mostRecentlyUsed.prev = entry
                    entry.next = self.mostRecentlyUsed
                    self.mostRecentlyUsed = entry
                else:
                    # is the least recently used
                    self.leastRecentlyUsed = entry.prev
                    self.leastRecentlyUsed.next = None
                    entry.prev = None
                    entry.next = self.mostRecentlyUsed
                    self.mostRecentlyUsed.prev = entry
                    self.mostRecentlyUsed = entry
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.leastRecentlyUsed.key]

                if self.leastRecentlyUsed != self.mostRecentlyUsed:
                    one_but_least = self.leastRecentlyUsed.prev
                    one_but_least.next = None
                    self.leastRecentlyUsed = one_but_least
                else:
                    self.mostRecentlyUsed = None
                    self.leastRecentlyUsed = None

            entry = Node(key, value)
            self.cache[key] = entry
            if not self.mostRecentlyUsed:
                self.mostRecentlyUsed = entry
                self.leastRecentlyUsed = entry
            else:
                entry.next = self.mostRecentlyUsed
                self.mostRecentlyUsed.prev = entry
                self.mostRecentlyUsed = entry

capacity = 2
obj = LRUCache(capacity)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))



# obj.put(2, 1)
# obj.put(1, 1)
# obj.put(2, 3)
# obj.put(4, 1)
#
# print(obj.get(1))
# print(obj.get(2))


#["LRUCache","get","get","put","get","put","put","put","put","get","put"]
#[[1],[6],[8],[12,1],[2],[15,11],[5,2],[1,15],[4,2],[4],[15,15]]

capacity = 1
obj = LRUCache(capacity)
print(obj.get(6))
print(obj.get(8))
print(obj.put(12, 1))
print(obj.get(2))
print(obj.put(15, 11))
print(obj.put(5, 2))
print(obj.put(1, 15))
print(obj.put(4, 2))
print(obj.get(4))
print(obj.put(15, 15))