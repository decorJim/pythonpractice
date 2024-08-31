from typing import List

def happyNumber(n: int):

    seen = set()

    while n != 1:

        digits = []

        while n > 0:

            digits.append(n % 10)
            n = n // 10

        for digit in digits:
            n += pow(digit, 2)

        print(n)

        if n in seen:
            return False
        
        seen.add(n)

    return True

print(happyNumber(19))
print()

print(happyNumber(2))
print()



