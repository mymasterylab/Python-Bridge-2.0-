DATA_FILE = "player_data.txt"

def load_player_profile():
    """Safely reads the save file or initializes default values if missing."""
    default_stats = {"name": "Aria", "gold": 120, "potions": 2}
    try:
        with open(DATA_FILE, "r") as f:
            stats = {}
            for line in f:
                cleaned = line.strip()
                if cleaned and ":" in cleaned:
                    k, v = cleaned.split(":")
                    stats[k] = int(v) if v.isdigit() else v
            print("Save file loaded successfully!")
            return stats
    except FileNotFoundError:
        print(f"'{DATA_FILE}' not found! Initializing starter character profile...")
        save_player_profile(default_stats)
        return default_stats

def save_player_profile(stats):
    """Safely serializes player attributes back to disk."""
    with open(DATA_FILE, "w") as f:
        for k, v in stats.items():
            f.write(f"{k}:{v}\n")

def get_valid_purchase_amount(max_gold, unit_cost):
    """Validates user shopping inputs against string errors and budget limits."""
    while True:
        raw_input = input("Enter quantity to purchase (or '0' to cancel): ").strip()
        try:
            quantity = int(raw_input)
            if quantity < 0:
                print("Quantity cannot be negative! Try again.")
                continue
            if quantity == 0:
                return 0

            total_cost = quantity * unit_cost
            if total_cost > max_gold:
                print(f"Insufficient funds! You need {total_cost}g, but only have {max_gold}g.")
                continue

            return quantity
        except ValueError:
            print(f"Error: '{raw_input}' is not a valid integer. Digits only!")

# Run Shop
player = load_player_profile()
POTION_PRICE = 20

print(f"\nWelcome back, {player['name']}!")
print(f"Current Gold: {player['gold']}g | Potions Owned: {player['potions']}")
print(f"Health Potions are {POTION_PRICE} gold each.\n")

qty = get_valid_purchase_amount(player["gold"], POTION_PRICE)

if qty > 0:
    cost = qty * POTION_PRICE
    player["gold"] -= cost
    player["potions"] += qty
    save_player_profile(player)
    print(f"Purchased {qty} potion(s) for {cost} gold.")
    print(f"Updated Wallet: {player['gold']}g | Total Potions: {player['potions']}")
else:
    print("Transaction cancelled.")