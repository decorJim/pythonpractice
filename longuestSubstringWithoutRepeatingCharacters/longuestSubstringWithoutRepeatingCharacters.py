


def longuestSubstringWithoutRepeatingCharacters(s:str):
    print(s)
    print()
    
    i = 0
    j = 0

    uniques = set()

    maxLength = 0

    while j < len(s):

        while s[j] in uniques:
            
            uniques.remove(s[i])
            i += 1

        uniques.add(s[j])

        if j - i + 1 > maxLength:
            maxLength = j - i + 1
            print(maxLength)
            print(uniques)
        
        j += 1

    return maxLength


s = "abcabcbb"
print(longuestSubstringWithoutRepeatingCharacters(s))
print()

s = "bbbbb"
print(longuestSubstringWithoutRepeatingCharacters(s))
print()

s = "pwwkew"
print(longuestSubstringWithoutRepeatingCharacters(s))
print()
