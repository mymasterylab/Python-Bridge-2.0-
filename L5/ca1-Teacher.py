# STEP 1: Appending a Quest Entry to Disk (Append Mode 'a')
quest_entry = "Defeat Goblin King:150:Active\n"

with open("quest_log.txt", "a") as file:
    file.write(quest_entry)
print("Quest successfully logged to disk!")

# STEP 2: Reading the Saved Quests Line-by-Line (Read Mode 'r')
print("\n--- Current Saved Quests ---")
with open("quest_log.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:
            title, gold, status = cleaned_line.split(":")
            print(f"Quest: {title:<20} | Reward: {gold:>4} gold | Status: [{status}]")