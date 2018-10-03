s = input('enter a word: ').lower()

def f(word):
    for i in range((len(s)+1)//2):

        if s[i] != s[len(s)-1-i]:
            return False
    return True

print(f(s))
