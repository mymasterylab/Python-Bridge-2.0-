# STEP 1: Building a Crash-Proof Integer Validator
def get_positive_integer(prompt):
    while True:
        raw_val = input(prompt).strip()
        try:
            val = int(raw_val)
            if val <= 0:
                print("Please enter a number greater than zero.")
                continue
            return val
        except ValueError:
            print(f"Invalid input: '{raw_val}' is not a valid whole number! Try again.")

bet = get_positive_integer("Enter your gold wager: ")
print(f"Wager locked: {bet} gold coins!")

# STEP 2: Guarding a Missing Save File with Fallbacks
save_file = "hero_save.txt"
try:
    with open(save_file, "r") as f:
        hero_data = f.read().strip()
        print(f"Loaded existing save: {hero_data}")
except FileNotFoundError:
    print(f"Notice: '{save_file}' was not found. Generating default adventurer profile...")
    hero_data = "Hero:Level 1:100 HP"
    with open(save_file, "w") as f:
        f.write(hero_data + "\n")
    print("New hero save file generated successfully.")