from typing import List
from collections import deque

class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def is_diff_1(gene1, gene2):
            diffs = 0
            for i in range(8):
                if gene1[i] != gene2[i]:
                    diffs += 1
            return diffs == 1

        banksy = set(bank)
        q = deque()
        visited = set()

        q.append((startGene, 0))
        while q:
            current_gene, step = q.popleft()
            if current_gene == endGene:
                return step
            visited.add(current_gene)
            for next_gene in banksy:
                if is_diff_1(next_gene, current_gene) and next_gene not in visited:
                    q.append((next_gene, step + 1))

        return -1

    def minMutation_dfs(self, startGene: str, endGene: str, bank: List[str]) -> int:
        banksy = set(bank)

        def is_diff_1(gene1, gene2):
            diffs = 0
            for i in range(8):
                if gene1[i] != gene2[i]:
                    diffs += 1
            return diffs == 1

        visited = set()
        def dfs(current_gene):
            if current_gene == endGene:
                return 0

            if current_gene in visited:
                return -1

            visited.add(current_gene)
            children = []
            # get all possible next genes that differ by 1 from current_gene
            for next_gene in banksy:
                if is_diff_1(next_gene, current_gene):
                    banksy.remove(next_gene)
                    val = dfs(next_gene)
                    banksy.add(next_gene)
                    if val != -1:
                        children.append(val + 1)
            visited.remove(current_gene)
            if len(children) > 0:
                return min(children)

            return -1


        return dfs(startGene)


    def minMutation_primitive(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)
        diffs = []
        for i in range(8):
            if startGene[i] != endGene[i]:
                diffs.append(i)

        def dfs(diffs, current_gene):
            if len(diffs) == 0:
                return True
            for i in range(len(diffs)):
                # check if after swapping the diffs[i] current gene is in bank
                new_current_gene = current_gene[:diffs[i]] + endGene[diffs[i]] + current_gene[diffs[i] + 1:]
                if new_current_gene in bank:
                    new_diffs = diffs[:i] + diffs[i + 1:]
                    if dfs(new_diffs, new_current_gene):
                        return True
            return False

        return len(diffs) if dfs(diffs, startGene) else -1


startGene = "AACCGGTT"
endGene =   "AAACGGTA"

bank =     ["AACCGATT",
            "AACCGATA",
            "AAACGATA",
            "AAACGGTA"]

bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]
startGene = "AAAACCCC"
endGene =   "CCCCCCCC"

s = Solution()
print(s.minMutation(startGene, endGene, bank))
