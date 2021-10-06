from collections import defaultdict

def is_isogram(word):
    word = word.lower()
    counts = defaultdict(int) # or defaultdict(lambda: 0)
    for letter in word:
        counts[letter] += 1
        if letter in [chr(i) for i in range(65,670)] and counts[letter] > 1:
            return False
    return True