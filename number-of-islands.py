from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if grid is None:
            return 0
        i_len = len(grid)
        for i in range(i_len):
            row = grid[i]
            j_len = len(row)
            for j in range(j_len):
                print(f"i={i}, j={j}, value = {grid[i][j]}")
                if grid[i][j] == "1":
                    islands += 1
                    lands = [[i, j]]
                    while len(lands) > 0:
                        l_i, l_j = lands.pop()
                        grid[l_i][l_j] = "0"
                        if (l_i + 1 != i_len) and (grid[l_i + 1][l_j] == "1"):
                            lands.append([l_i + 1, l_j])
                        if (l_i != 0) and (grid[l_i - 1][l_j] == "1"):
                            lands.append([l_i - 1, l_j])
                        if (l_j + 1 != j_len) and (grid[l_i][l_j + 1] == "1"):
                            lands.append([l_i, l_j + 1])
                        if (l_j != 0) and (grid[l_i][l_j - 1] == "1"):
                            lands.append([l_i, l_j - 1])
        return islands


print(Solution.numIslands(self=None,
                          grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                                ["0", "0", "0", "0", "0"]]))
