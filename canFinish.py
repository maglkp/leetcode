from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct the graph as a dictionary adjacency list
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)
            for next_course in adj_list[course]:
                if not dfs(next_course):
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # if not prerequisites:
        #     return True

        # construct the graph as a dictionary adjacency list
        adj_list = defaultdict(list)
        courses_with_prereqs = set()
        all_courses = set()

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            courses_with_prereqs.add(course)
            all_courses.add(course)
            all_courses.add(prereq)

        bfs = deque()
        visited = set()
        # add courses that have no prereqs to the queue
        for course_and_next_course in prerequisites:
            if course_and_next_course[1] not in courses_with_prereqs:
                bfs.append(course_and_next_course[1])
                visited.add(course_and_next_course[1])

        while bfs:
            course = bfs.pop()

            for next_course in adj_list[course]:
                if next_course not in visited:
                    bfs.append(next_course)
                    visited.add(next_course)

        return len(visited) >= numCourses or len(visited) == len(all_courses)


# numCourses = 5
# prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]

s = Solution()
print(s.canFinish(numCourses, prerequisites))
