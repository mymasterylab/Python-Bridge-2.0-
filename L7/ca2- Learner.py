import random

SIZE = 5
GRID_SIZE = 5
grid = []
for row in range(GRID_SIZE):
    grid_row = []
    for col in range(GRID_SIZE):
        grid_row.append(".")
    grid.append(grid_row)
player_r, player_c = 0, 0
gold_r, gold_c = random.randint(1, 4), random.randint(0, 3)
trap_r, trap_c = random.randint(0, 3), random.randint(1, 4)
exit_r, exit_c = 4, 4

gold_collected = 0
player_hp = 3

def print_dungeon():
    print("\n" + "=" * 25)
    print(f"HP: {'❤️ ' * player_hp} | Gold: {gold_collected} coins")
    print("-" * 25)
    for r in range(SIZE):
        row_cells = []
        for c in range(SIZE):
            if r == player_r and c == player_c:
                row_cells.append("P")
            elif r == exit_r and c == exit_c:
                row_cells.append("E")
            else:
                row_cells.append(grid[r][c])
        print("  ".join(row_cells))
    print("=" * 25)

while player_hp > 0:
    print_dungeon()
    cmd = input("Move [W/A/S/D] or [Q]uit: ").strip().upper()
    if cmd == "Q":
        print("Retreated from the dungeon.")
        break

    dr, dc = 0, 0
    if cmd == "W": dr = -1
    elif cmd == "S": dr = 1
    elif cmd == "A": dc = -1
    elif cmd == "D": dc = 1
    else:
        print("Invalid key! Use W, A, S, or D.")
        continue

    nr, nc = player_r + dr, player_c + dc
    if not (0 <= nr < SIZE and 0 <= nc < SIZE):
        print("\n* THUD! * You walked straight into a solid stone wall.")
        continue

    player_r, player_c = nr, nc

    # Tile Events
    if player_r == gold_r and player_c == gold_c:
        print("\n✨ You found a chest of ancient dungeon gold! (+50g)")
        gold_collected += 50
        gold_r, gold_c = -1, -1
    elif player_r == trap_r and player_c == trap_c:
        print("\n💥 SNAP! You stepped on a hidden spike trap! (-1 HP)")
        player_hp -= 1
        trap_r, trap_c = -1, -1
    elif player_r == exit_r and player_c == exit_c:
        print(f"\n🏆 ESCAPED! You reached the stairs with {gold_collected} gold!")
        break

if player_hp <= 0:
    print("\n💀 You collapsed inside the dark corridors. Game Over.")