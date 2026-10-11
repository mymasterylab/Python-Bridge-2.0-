# STEP 1: Define a calculation function with parameters and return
def calculate_attack_power(base_attack, level_multiplier=1.2):
  total_power = int(base_attack * level_multiplier)
  return total_power


# STEP 2: Define a pure status check function
def is_hero_standing(health):
  return health > 0


# STEP 3: Execute function and capture returned values
base_strike = 20
effective_strike = calculate_attack_power(base_strike, level_multiplier=1.5)
print(f"Calculated Effective Attack Power: {effective_strike} pts")

target_hp = 25
target_hp -= effective_strike
print(f"Target Health Remaining: {max(0, target_hp)}")
print(f"Is Target Still Standing? {is_hero_standing(target_hp)}")