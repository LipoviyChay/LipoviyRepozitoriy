def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

print(palindrome('дед'))
print(palindrome('шашлык'))
