from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # 1. Count occurrences of each character
    counts = Counter(s)
    
    # 2. Sort by frequency (descending) then by character (ascending)
    # x[0] is the character, x[1] is the count
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 3. Print the top three
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
