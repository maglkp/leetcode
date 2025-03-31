from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # construct the graph as a dictionary adjacency list
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        visited = set()
        order = []
        order_set = set()

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                if not course in order_set:
                    order.append(course)
                    order_set.add(course)
                return True
            visited.add(course)
            for next_course in adj_list[course]:
                if not dfs(next_course):
                    return False
            visited.remove(course)
            adj_list[course] = []
            if not course in order_set:
                order.append(course)
                order_set.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return list(reversed(order))



numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

#numCourses = 3
#prerequisites = [[1, 0], [1, 2], [0, 1]]

s = Solution()
print(s.findOrder(numCourses, prerequisites))