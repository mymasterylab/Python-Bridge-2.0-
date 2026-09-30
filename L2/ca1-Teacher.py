# ============================================================
# LESSON 2: GUIDED STARTER - STRING SANITIZER & SLICING
# ============================================================

# 1. Raw user input with messy casing and whitespace
raw_text = input("Enter a message with spaces (e.g., '  HeLLo WoRLd  '): ")

# 2. Sanitization pipeline
clean_text = raw_text.strip().lower()
print(f"Sanitized: '{clean_text}'")

# 3. String slicing
first_three = clean_text[:3]
last_three = clean_text[-3:]
reversed_text = clean_text[::-1]

print(f"First 3 characters : '{first_three}'")
print(f"Last 3 characters  : '{last_three}'")
print(f"Reversed string    : '{reversed_text}'")