# STEP 1: Initializing a 4x4 Grid Matrix
GRID_SIZE = 4
grid = []
for row in range(GRID_SIZE):
    grid_row = []
    for col in range(GRID_SIZE):
        grid_row.append(".")
    grid.append(grid_row)

# STEP 2: Placing Player and Hidden Treasure
player_r, player_c = 0, 0
treasure_r, treasure_c = 2, 3

grid[player_r][player_c] = "P"

def render_grid(g):
    print("\n--- DUNGEON MAP ---")
    for row in g:
        print(" ".join(row))

render_grid(grid)

# STEP 3: Single Step Movement with Boundary Verification
move = input("\nEnter move (W/A/S/D): ").strip().upper()
dr, dc = 0, 0
if move == "W": dr = -1
elif move == "S": dr = 1
elif move == "A": dc = -1
elif move == "D": dc = 1

new_r = player_r + dr
new_c = player_c + dc

if 0 <= new_r < GRID_SIZE and 0 <= new_c < GRID_SIZE:
    grid[player_r][player_c] = "."  # Clear previous tile
    player_r, player_c = new_r, new_c
    grid[player_r][player_c] = "P"  # Set new position
    print(f"Moved to ({player_r}, {player_c})")
else:
    print("BONK! You hit an ancient dungeon wall.")

render_grid(grid)