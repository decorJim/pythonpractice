def removeAllAdjacentDuplicate(s: str):

    stack = []

    for character in s:

        # if the stack is not empty and the top of the stack character
        # is the same as the current one the remove it so both disappears
        if stack and stack[-1] == character:
            stack.pop()

        else:
            stack.append(character)

    ans = ""

    for character in stack:

        ans += character

    return ans

print(removeAllAdjacentDuplicate("abbaca"))
print()

print(removeAllAdjacentDuplicate("azxxzy"))
print()

# in this problem we only want to remove duplicates adjacent so 
# if there is a third or any odd identical character we will keep one at the end
print(removeAllAdjacentDuplicate("aaa"))
print()




