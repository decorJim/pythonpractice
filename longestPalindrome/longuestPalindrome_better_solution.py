def longuestPalindrome(strs: str):

    oddLength = False

    lettersCount = {}

    for letter in strs:

        if letter in lettersCount:

            lettersCount[letter] += 1

        else:

            lettersCount[letter] = 1

    print(lettersCount)
    print()

    palindromeSize = 0

    for key, value in lettersCount.items():

        if value % 2 == 0:
            palindromeSize += value

        else:
            # all other odd number we take their even part and add it
            palindromeSize += value - 1
            # this is just to tell that there is at least 1 odd count for a letter
            oddLength = True

    if oddLength:
        # add back 1 for the letter that has the highest odd count
        palindromeSize += 1

    return palindromeSize

print(longuestPalindrome("aabbcc"))
print()

print(longuestPalindrome("aab"))
print()

print(longuestPalindrome("aabb"))
print()

print(longuestPalindrome("abccccdd"))
print()

print(longuestPalindrome("a"))
print()