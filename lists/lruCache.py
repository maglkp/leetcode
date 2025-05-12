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
                entry.prev.next = entry.next
                entry.next.prev = entry.prev
                self.mostRecentlyUsed.prev = entry
                entry.next = self.mostRecentlyUsed
                self.mostRecentlyUsed = entry
            else:
                entry.prev.next = None
                entry.prev = None
                entry.next = self.mostRecentlyUsed
                self.mostRecentlyUsed.prev = entry
                self.mostRecentlyUsed = entry

        return v

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            entry = self.cache[key]
            if entry != self.mostRecentlyUsed:
                # or
                # if entry.prev is not None:
                if entry is not self.leastRecentlyUsed:
                    # or
                    # if entry.next is not None:
                    entry.prev.next = entry.next
                    entry.next.prev = entry.prev
                    self.mostRecentlyUsed.prev = entry
                    entry.next = self.mostRecentlyUsed
                    self.mostRecentlyUsed = entry
                else:
                    entry.prev.next = None
                    entry.prev = None
                    entry.next = self.mostRecentlyUsed
                    self.mostRecentlyUsed.prev = entry
                    self.mostRecentlyUsed = entry
            entry.value = value
        else:
            if len(self.cache) == self.capacity:
                one_but_least = self.leastRecentlyUsed.prev
                if one_but_least:
                   one_but_least.next = None
                del self.cache[self.leastRecentlyUsed.key]
                self.leastRecentlyUsed = one_but_least

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
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
#print(obj.get(1))
#print(obj.get(3))
#print(obj.get(4))



