

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


print(is_palindrome("tenet"))
