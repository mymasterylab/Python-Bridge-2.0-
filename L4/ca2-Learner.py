import random


def calculate_mitigation(armor_value):
  # Standard RPG diminishing returns formula: armor / (armor + 50)
  mitigation = armor_value / (armor_value + 50)
  return min(0.75, round(mitigation, 2))


def compute_damage(raw_attack, armor_value, is_crit=False, crit_bonus=1.5):
  multiplier = crit_bonus if is_crit else 1.0
  boosted_attack = raw_attack * multiplier
  mitigation_factor = calculate_mitigation(armor_value)

  net_damage = boosted_attack * (1 - mitigation_factor)
  return max(1, int(round(net_damage)))


def apply_damage_to_target(target_name, current_hp, incoming_damage):
  new_hp = max(0, current_hp - incoming_damage)
  is_defeated = new_hp == 0
  print(
      f"-> {target_name} takes {incoming_damage} damage! HP remaining: {new_hp}"
  )
  return new_hp, is_defeated


# Combat Loop Implementation
player = {"name": "Aria", "hp": 100, "attack": 28, "armor": 15}
enemy = {"name": "Cave Troll", "hp": 85, "attack": 22, "armor": 30}

round_number = 1
while player["hp"] > 0 and enemy["hp"] > 0:
  print(f"\n--- Round {round_number} ---")

  # Player's Turn
  is_player_crit = random.random() < 0.25
  if is_player_crit:
    print("CRITICAL STRIKE OPPORTUNITY!")

  dmg_dealt = compute_damage(
      player["attack"], enemy["armor"], is_crit=is_player_crit
  )
  enemy["hp"], troll_down = apply_damage_to_target(
      enemy["name"], enemy["hp"], dmg_dealt
  )

  if troll_down:
    print(f"\nVICTORY! {enemy['name']} was defeated!")
    break

  # Enemy's Turn
  enemy_dmg = compute_damage(enemy["attack"], player["armor"])
  player["hp"], hero_down = apply_damage_to_target(
      player["name"], player["hp"], enemy_dmg
  )

  if hero_down:
    print(f"\nDEFEAT! {player['name']} has fallen in battle.")
    break

  round_number += 1