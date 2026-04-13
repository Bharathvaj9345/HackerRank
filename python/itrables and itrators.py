from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
indices = list(range(1, n + 1))
all_combos = list(combinations(indices, k))
a_indices = [i + 1 for i, char in enumerate(letters) if char == 'a']
count = 0
for combo in all_combos:
    if any(i in a_indices for i in combo):
        count += 1
print(f"{count / len(all_combos):.4f}")
