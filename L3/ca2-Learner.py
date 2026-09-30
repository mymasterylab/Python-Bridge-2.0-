# ============================================================
# LESSON 3: RPG CHARACTER SHEET & MERCHANT SHOP
# Concepts: Nested structures, .get(), funds verification, CRUD
# ============================================================

# Complete Character Data
character = {
    "name": "Eldrin",
    "class": "Ranger",
    "gold": 120,
    "hp": 90,
    "max_hp": 100,
    "stats": {"strength": 12, "agility": 16, "intelligence": 10},
    "inventory": ["Iron Bow", "Quiver (20)"],
}

# Merchant Wares: item_name -> price
shop_stock = {
    "healing_potion": 25,
    "leather_armor": 60,
    "elven_boots": 80,
    "smoke_bomb": 15,
}

print(f"=== WELCOME TO THE OUTPOST MERCHANT, {character['name'].upper()}! ===")
print(f"Balance: {character['gold']} gold | HP: {character['hp']}/{character['max_hp']}")

# Display Merchant Catalog using .items()
print("\n--- Available Wares ---")
for item, price in shop_stock.items():
    formatted_name = item.replace("_", " ").title()
    print(f" - {formatted_name:<18} : {price} gold")

# Purchasing Interface
choice = (
    input("\nEnter the item name you wish to buy: ")
    .strip()
    .lower()
    .replace(" ", "_")
)

# Safe Price Check using .get()
price = shop_stock.get(choice)

if price is None:
    print(f"\nThe merchant tilts their head: 'I have never heard of {choice}.'")
elif character["gold"] >= price:
    # Deduct currency and append item
    character["gold"] -= price
    character["inventory"].append(choice.replace("_", " ").title())
    print(f"\nPurchase successful! You acquired {choice.replace('_', ' ').title()}.")
    print(f"Remaining Gold: {character['gold']} coins.")
else:
    deficit = price - character["gold"]
    print(f"\nInsufficient funds! You need {deficit} more gold to buy that.")

# Display Final Character Sheet
print("\n=== UPDATED CHARACTER SHEET ===")
for key, value in character.items():
    if key == "stats":
        print("Stats:")
        for stat_name, stat_val in value.items():
            print(f"   * {stat_name.title()}: {stat_val}")
    elif key == "inventory":
        print("Inventory :", ", ".join(value))
    else:
        print(f"{key.capitalize():<10}: {value}")