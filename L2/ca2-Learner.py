# ============================================================
# LESSON 2: TEXT COMMAND CLEANER & CIPHER PARSER
# Concepts: .strip(), .lower(), .split(), list slicing, [::-1]
# ============================================================

valid_verbs = ["take", "drop", "inspect", "use", "open", "decode"]

print("=== DUNGEON TERMINAL INTERFACE ===")
print("Type a command (e.g., '  INSPECT ancient iron chest  ' or 'decode #!emocleW')\n")

raw_command = input("terminal> ")

# Step 1: Clean and tokenize
sanitized = raw_command.strip()
words = sanitized.split()

if not words:
    print("Error: No command detected.")
else:
    # Step 2: Separate verb from target tokens using list slicing
    action = words[0].lower()
    target_tokens = words[1:]
    target = " ".join(target_tokens) if target_tokens else "nothing"

    print(f"\n[Command Parsed]")
    print(f"  -> Action Verb : {action}")
    print(f"  -> Target Item : {target}")

    # Step 3: Validate action
    if action in valid_verbs:
        print("  -> Status      : Command recognized by game engine.")
    else:
        print("  -> Status      : Unknown command.")

    # Step 4: Secret Cipher Parser Subroutine
    if action == "decode":
        # Check for marker '#!' and reverse the payload
        if target.startswith("#!"):
            payload = target[2:]  # Slice away the '#!' prefix
            solved = payload[::-1]  # Reverse to reveal plain text
            print(f"\n🔓 CIPHER CRACKED: '{solved}'")
        else:
            print("\nInvalid cipher format. Must start with '#!' prefix.")