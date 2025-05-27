from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        layers = divmod(len(matrix), 2)[0]
        for layer in range(layers):
            layer_width = len(matrix) - 2 * layer
            for k in range(layer_width - 1):
                top = matrix[layer][layer + k]
                right = matrix[layer + k][layer + layer_width - 1]
                bottom = matrix[layer + layer_width - 1][layer + layer_width - 1 - k]
                left = matrix[layer + layer_width - 1 - k][layer]

                matrix[layer][layer + k] = left
                matrix[layer + k][layer + layer_width - 1] = top
                matrix[layer + layer_width - 1][layer + layer_width - 1 - k] = right
                matrix[layer + layer_width - 1 - k][layer] = bottom


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
s.rotate(matrix)
print(matrix)
