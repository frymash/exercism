import string
def is_isogram(str):
    s = str.lower()
    letter = dict()
    for i in s:
        letter[i] = letter.get(i,0)+1
        if i in string.ascii_lowercase and letter[i] > 1:
            return False
    return True