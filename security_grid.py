# Problem 3 - “Security Grid”
 
# Given a 5x5 grid:
 
# 1 1 0 0 1
# 0 1 1 0 0
# 0 0 1 0 1
# 1 0 0 1 1
# 0 0 1 0 0
 
 
# Movement allowed: Up/down/left/right only
 
# Find: Number of connected clusters

grid = [
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0]
]
 
rows = len(grid)
cols = len(grid[0])
 
visited = [[False] * cols for _ in range(rows)]
 
# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
def dfs(r, c):
    visited[r][c] = True
 
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
 
        if (0 <= nr < rows and
            0 <= nc < cols and
            grid[nr][nc] == 1 and
            not visited[nr][nc]):
 
            dfs(nr, nc)
 
clusters = 0
 
for i in range(rows):
    for j in range(cols):
 
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            clusters += 1
 
print("Number of connected clusters:", clusters)
 