def simulate_liquid_flow(terrain):
   n = len(terrain)
   water_level = terrain[n // 2][n // 2]  # Start at the central cell
   wet_cells = {(n // 2, n // 2)}  # Set of wet cells

   while True:
       print("----------")
       print(f"Current water level: {water_level}")
       print_terrain(terrain, wet_cells)

       flowed = False
       new_wet_cells = set()
       for row, col in wet_cells:
           for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
               new_row, new_col = row + dr, col + dc
               if 0 <= new_row < n and 0 <= new_col < n and terrain[new_row][new_col] <= water_level:
                   new_wet_cells.add((new_row, new_col))
                   flowed = True

       wet_cells |= new_wet_cells  # Update wet cells

       if not flowed:
           water_level += 1
       else:
           if any(cell[0] == 0 or cell[0] == n - 1 or cell[1] == 0 or cell[1] == n - 1 for cell in wet_cells):
               print("Reached edge, exiting.")
               break

   print("Solution:")
   print_terrain(terrain, wet_cells)

def print_terrain(terrain, wet_cells):
   for row in range(len(terrain)):
       for col in range(len(terrain)):
           print("W" if (row, col) in wet_cells else ".", end="")
       print()

# Get input
n = int(input( "enter current water level"))
terrain = []
for _ in range(n):
   terrain.append(list(map(int, input().split())))

# Simulate liquid flow
simulate_liquid_flow(terrain)
