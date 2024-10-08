from typing import List, Set, Dict
import random


class RandomizedSet:

    def __init__(self):
        self.indexes: Dict = dict()
        self.values: List = list()

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False

        self.values.append(val)
        self.indexes[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False

        removed_ix = self.indexes[val]
        self.indexes.pop(val)
        if len(self.values) > 1:
            last_ix = len(self.values) - 1
            if removed_ix < last_ix:
                # move back last value to the removed value position
                last_value = self.values[last_ix]
                self.values[removed_ix] = last_value  # !!!

                # update map with new last-element index that was moved back
                self.indexes[last_value] = removed_ix

        # remove last value which can now be in 2 places (if len>1)
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


s = RandomizedSet()
print(s.insert(1))
print(s.insert(7))
print(s.remove(1))

print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())
