class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        value_to_new_node = dict()

        def dfs(node):
            if not node:
                return None
            if node.val in value_to_new_node:
                return value_to_new_node[node.val]

            new_node = Node(node.val)
            value_to_new_node[node.val] = new_node

            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            return new_node

        return dfs(node)


    # adjacency list approach
    def cloneGraph1(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        # construct the adjacency list
        adj_list = {}

        def dfs_construct_adjlist(node):
            if not node:
                return

            if node.val not in adj_list:
                adj_list[node.val] = [n.val for n in node.neighbors]

                for neighbor in node.neighbors:
                    dfs_construct_adjlist(neighbor)

        dfs_construct_adjlist(node)

        # clone the graph
        root = Node(node.val)

        def dfs_clone(cloned_node):
            if not cloned_node or cloned_node.val not in adj_list:
                return

            ns = adj_list.pop(cloned_node.val)
            for neighbor in ns:
                n = Node(neighbor)
                cloned_node.neighbors.append(n)
                dfs_clone(n)

        dfs_clone(root)

        return root


adj_init = {1: [2, 4],
     2: [1, 3],
     3: [2, 4],
     4: [1, 3]     }
root = Node(1)

def dfs_clone_init(cloned_node):
    if not cloned_node or cloned_node.val not in adj_init:
        return

    ns = adj_init.pop(cloned_node.val)
    for neighbor in ns:
        n = Node(neighbor)
        cloned_node.neighbors.append(n)
        dfs_clone_init(n)


dfs_clone_init(root)
#print(root)

s = Solution()
c = s.cloneGraph(root)
print(c)
