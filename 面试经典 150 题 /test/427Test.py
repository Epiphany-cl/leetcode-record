class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


two_dimensional_array = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
                         [1, 1, 1, 1, 0, 0, 0, 0]]

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def create_node(row_start: int, column_start: int, row_end: int, column_end: int) -> 'Node':
            # 判断该区域值是否相同 相同则创建叶子节点，否则创建根节点
            if all(grid[row_start][column_start] == grid[r][c] for r in range(row_start, row_end) for c in
                   range(column_start, column_end)):
                return Node(grid[row_start][column_start] == 1, True, None, None, None, None)
            else:
                return Node(
                    True,
                    False,
                    create_node(row_start, column_start, (row_start + row_end) // 2, (column_start + column_end) // 2),
                    create_node(row_start, (column_start + column_end) // 2, (row_start + row_end) // 2, column_end),
                    create_node((row_start + row_end) // 2, column_start, row_end, (column_start + column_end) // 2),
                    create_node((row_start + row_end) // 2, (column_start + column_end) // 2, row_end, column_end)
                )
        return create_node(0, 0, len(grid), len(grid[0]))