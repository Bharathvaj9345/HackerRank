from itertools import groupby

# Read the input string
S = input().strip()

# Iterate through groups created by groupby
# 'k' is the character, 'g' is an iterator of the consecutive occurrences
results = []
for k, g in groupby(S):
    count = len(list(g))
    results.append(f"({count}, {k})")

# Print all groups joined by a single space
print(" ".join(results))
