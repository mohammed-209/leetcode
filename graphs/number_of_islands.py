# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.explore(grid, r, c, visited):
                    count += 1

        return count

    def explore(self, grid, r, c, visited):
        if not 0 <= r < len(grid):
            return False
        if not 0 <= c < len(grid[0]):
            return False
        if grid[r][c] == "0":
            return False
        if (r, c) in visited:
            return False
        visited.add((r, c))
        
        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)

        return True