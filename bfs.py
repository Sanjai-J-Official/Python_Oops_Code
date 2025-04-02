from collections import deque

def min_steps(grid):
    rows, cols = len(grid), len(grid[0])
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = set((0, 0))
    
    while queue:
        r, c, steps = queue.popleft()
        
        # If we reach the bottom-right corner, return steps taken
        if r == rows-1 and c == cols-1:
            return steps
        
        # Try moving in all four directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, steps + 1))
                visited.add((nr, nc))
    
    return -1  # No path found

# Example Grid (0 = open path, 1 = obstacle)
grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1 ]
    
]
print(min_steps(grid))  # Output: 6 (minimum steps to reach bottom-right)
