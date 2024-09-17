def removeAllAdjacentDuplicate(s: str, k:int):

    stack = [] # character, count

    for character in s:

        # stack is not empty and top of stack the character is same as current
        if stack and stack[-1][0] == character:

            # increment the count of the character
            stack[-1][1] += 1

        else:

            stack.append([character, 1])

        # if the count of the character reached k then we remove it from the stack
        if stack[-1][1] == k:
            stack.pop()

    ans = ""

    for character, count in stack:
        # the remaining character that has not k duplicate 
        # concatenate them with their count
        ans += (character * count)

    return ans 


print(removeAllAdjacentDuplicate("abcd", 2))
print()

print(removeAllAdjacentDuplicate("deeedbbcccbdaa", 3))
print()

print(removeAllAdjacentDuplicate("pbbcggttciiippooaais", 2))
print()





