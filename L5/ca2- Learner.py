LOG_FILE = "quest_records.txt"

def append_quest(title, gold_reward):
    """Appends a new quest record to the log file in append mode."""
    record = f"{title}:{gold_reward}:Active\n"
    with open(LOG_FILE, "a") as f:
        f.write(record)
    print(f"-> Logged new quest: '{title}' ({gold_reward} gold)")

def load_all_quests():
    """Reads and parses saved quests from disk into a list of dictionaries."""
    quests = []
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned:
                    title, gold, status = cleaned.split(":")
                    quests.append({
                        "title": title,
                        "gold": int(gold),
                        "status": status
                    })
    except FileNotFoundError:
        pass
    return quests

def display_quest_board(quests):
    """Displays formatted active and completed quests."""
    print("\n=== PERSISTENT QUEST BOARD ===")
    if not quests:
        print("No quests found on the board.")
        return
    for idx, q in enumerate(quests, start=1):
        print(f"{idx}. {q['title']:<25} | Reward: {q['gold']:>4}g | Status: [{q['status']}]")

def complete_quest(quests, quest_index):
    """Marks a quest complete and rewrites the entire file using write mode ('w')."""
    if 0 <= quest_index < len(quests):
        quests[quest_index]["status"] = "Completed"
        with open(LOG_FILE, "w") as f:
            for q in quests:
                f.write(f"{q['title']}:{q['gold']}:{q['status']}\n")
        print(f"-> Marked '{quests[quest_index]['title']}' as Completed!")
    else:
        print("Invalid quest number.")

# Interactive Loop
while True:
    active_quests = load_all_quests()
    display_quest_board(active_quests)
    print("\nOptions: [1] Add Quest  [2] Complete Quest  [3] Exit")
    choice = input("Select an option: ").strip()

    if choice == "1":
        name = input("Enter quest title: ").strip()
        reward = input("Enter gold reward: ").strip()
        if reward.isdigit():
            append_quest(name, int(reward))
        else:
            print("Reward must be a valid number!")
    elif choice == "2":
        q_num = input("Enter quest number to mark complete: ").strip()
        if q_num.isdigit():
            complete_quest(active_quests, int(q_num) - 1)
        else:
            print("Please enter a valid number.")
    elif choice == "3":
        print("Closing quest terminal. All progress is saved to disk!")
        break