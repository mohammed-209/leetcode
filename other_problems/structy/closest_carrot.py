from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  q = deque([(starting_row, starting_col, 0)])
  visited = set([ (starting_row, starting_col) ])
  
  while q:
    row, col, distance = q.popleft()
    
    if grid[row][col] == "C":
      return distance

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for direction in directions:
      dr, dc = direction
      r, c = dr + row, dc + col
      pos = (r, c)
      row_inbound = 0 <= r < len(grid)
      col_inbound = 0 <= c < len(grid[0])
      if pos not in visited and row_inbound and col_inbound and grid[r][c] != "X":
        q.append((r, c, distance+1))
        visited.add(pos)

  return -1