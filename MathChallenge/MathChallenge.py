

def mathChallenge(num):

    # convert num into a string and for each character convert it into a integer
    # put each inside a map and convert it all into a list
    digits = list(map(int, str(num)))

    if len(digits) == 1:
        return -1

    # start at second last position so there is always a i - 1
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i-1]:
        i -= 1

    # the number is already in the form of 54321 no permutation will get a higher number
    if i == -1:
        return -1

    # find the number at the right of i that is still bigger than current number at i
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # swap it with number at i
    digits[i], digits[j] = digits[j], digits[i]

    # sort the rest at the right in ascending order from right to left
    # keep all of left until i and from i + 1 to end place in reverse order
    digits = digits[:i+1] + digits[i+1:][i::]

    # concatenate all without anything seperating them
    next_greater = ''.join(map(str, digits))

    myAns = str(next_greater) + "j48zc5xef3"
    filtered = ''.join(char if (i + 1) % 3 != 0 else 'X' for i, char in enumerate(myAns))

    return filtered


print(mathChallenge(4113484492))




