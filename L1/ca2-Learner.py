# ============================================================
# LESSON 1: MYSTERY DUNGEON LOOT RUN
# Concepts: random.choice, branch logic, negative accumulation, win condition
# ============================================================

import random

bag = []
gold_pouch = []
MAX_CAPACITY = 4
GOAL_GOLD = 50

chest_events = [
    "Shiny Ruby",
    "Rusty Dagger",
    "Ancient Coin",
    "Mimic Trap",
    "Healing Salve",
    "Diamond Ring",
]

print("=== ENTER THE MYSTERY DUNGEON ===")
print(f"Goal: Collect {GOAL_GOLD} gold before filling your bag ({MAX_CAPACITY} items max)!\n")

while len(bag) < MAX_CAPACITY:
    print("--------------------------------------------------")
    print(f"Slots remaining: {MAX_CAPACITY - len(bag)}")
    action = input("Press [ENTER] to open a chest (or 'q' to flee): ").strip().lower()

    if action == "q":
        print("You fled the dungeon early!")
        break

    loot = random.choice(chest_events)
    print(f"\nYou opened a chest and found: {loot}")

    if loot == "Mimic Trap":
        print("IT'S A TRAP! A pickpocket steals 10 gold!")
        gold_pouch.append(-10)
    else:
        bag.append(loot)
        coins = random.randint(10, 25)
        gold_pouch.append(coins)
        print(f"Safely packed {loot}! Found {coins} gold.")

# Display final bag contents
print("\n=== DUNGEON RUN COMPLETE: BAG CONTENTS ===")
for item in bag:
    print(f"- {item}")

# Accumulator pattern
total_gold = 0
for coins in gold_pouch:
    total_gold = total_gold + coins

if total_gold < 0:
    total_gold = 0

print(f"\nTotal Gold Extracted: {total_gold} coins")

# Evaluation
if total_gold >= GOAL_GOLD:
    print("VICTORY! You escaped rich and beat the dungeon quota!")
else:
    print("DEFEAT! You survived, but did not collect enough gold.")