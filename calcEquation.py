from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # construct the graph
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0 / values[i]))

        def dfs(node, target, seen):
            if node not in graph:
                return -1
            if node in seen:
                return -1
            seen.add(node)
            if node == target:
                return 1
            for neighbor, val in graph[node]:
                v = dfs(neighbor, target, seen)
                if v != -1:
                    return val * v
            return -1

        def dfs_acc(node, target, seen, acc):
            if node not in graph:
                return -1
            if node == target:
                return acc
            if node in seen:
                return -1
            seen.add(node)
            for neighbor, val in graph[node]:
                v = dfs_acc(neighbor, target, seen, acc * val)
                if v != -1:
                    #return val * dfs(neighbor, target, seen)
                    return v
            return -1

        res = []
        for i in range(len(queries)):
            res.append(dfs(queries[i][0], queries[i][1], set()))
            #res.append(dfs_acc(queries[i][0], queries[i][1], set(), 1.0))
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
s = Solution()
print(s.calcEquation(equations, values, queries))
