

def is_palindrome(word: str):
    y = 0
    x = -1
    word_backward = []
    for _ in word:
        word_backward.append(word[x])
        x -= 1
    word_forward = []
    for _ in word:
        word_forward.append(word[y])
        y += 1
    if word_forward == word_backward:
        return True
    else:
        return False


"""
returns boolean value,
argument is str 
znaki z argumentu są umieszczane w liście -word_forward pokolei
oraz w liście - word_backward w odwrotnej kolejności
następnie obie listy są porównywane zwracana jest wartość true jeśli są takie same
a false jeśli różne
"""



print(is_palindrome("tenet"))
