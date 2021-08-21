def is_isogram(string):
    s = string.lower()
    return len(set(s)) == len(s)