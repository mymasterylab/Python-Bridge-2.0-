# ============================================================
# LESSON 1: WARM-UP & GUIDED STARTER
# Concepts: Lists, .append(), while loop with len(), for loop, accumulator
# ============================================================

bag = []
gold_pouch = []
MAX_CAPACITY = 4

print("=== WELCOME TO THE DUNGEON ===")
print("Your backpack can hold up to 4 items.\n")

# While loop: keep gathering until the backpack reaches capacity
while len(bag) < MAX_CAPACITY:
    item = input("What item did you find? ").strip()
    if item != "":
        bag.append(item)
        gold_pouch.append(15)  # 15 gold reward per item
        print(f"-> Packed {item}! (Slots used: {len(bag)}/{MAX_CAPACITY})")

print("\nBackpack is full! Escaping dungeon...")

# Display bag contents
print("\n--- Loot Inspection ---")
for item in bag:
    print("- " + item)

# Accumulator loop: calculate total gold
total_gold = 0
for coins in gold_pouch:
    total_gold = total_gold + coins

print(f"\nTotal Gold Gathered: {total_gold} coins!")