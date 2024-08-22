def longuestPalindrome(strs: str):

    lettersCount = {}

    for letter in strs:

        if letter in lettersCount:

            lettersCount[letter] += 1

        else:

            lettersCount[letter] = 1

    print(lettersCount)
    print()

    palindromeSize = 0
    largestOdd = 0

    for key, value in lettersCount.items():

        if value % 2 == 0:
            palindromeSize += value

        else:
            largestOdd = max(largestOdd, value)

    palindromeSize += largestOdd

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