# ============================================================
# LESSON 3: GUIDED WARM-UP - DICTIONARY BASICS & CRUD
# ============================================================

# 1. CREATE: Initialize a character dictionary
player = {
    "name": "Kaelen",
    "class": "Rogue",
    "hp": 90,
    "max_hp": 100,
    "gold": 65
}

print(f"Loaded Adventurer: {player['name']} the {player['class']}")

# 2. READ: Direct lookup vs safe lookup
print("Current HP :", player["hp"])
print("Mana Pool  :", player.get("mana", "No Mana Ability"))  # Safe lookup

# 3. UPDATE: Modify an existing stat and add a new key
player["hp"] -= 15           # Took combat damage
player["gold"] += 20         # Found gold
player["level"] = 2          # Added new key-value pair
print(f"Updated Stats: Level {player['level']} | HP: {player['hp']}/{player['max_hp']} | Gold: {player['gold']}g")

# 4. DELETE: Remove a temporary status effect
player["poisoned"] = True
print("Status Effect Applied : Poisoned =", player["poisoned"])
del player["poisoned"]
print("Status Effect Cleared : Poisoned key removed successfully!")