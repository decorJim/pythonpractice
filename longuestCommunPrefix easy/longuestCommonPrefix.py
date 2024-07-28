from typing import List


def longuestCommunPreix(strs:List[str]):
    
    print(strs)
    print()

    # we used first word in array to compare with others
    # arbitrary chosen we handle the case in if statement
    for i in range(len(strs[0])):
        print(strs[0][i])
        for word in strs:

            # if one of the words has a smaller length than the first word
            # the common prefix is that word so no need to check other strings
            if i == len(word) or word[i] != strs[0][i]:
                print("different", strs[0][i], word[i])
                print()
                return word[0:i]
                
        print()
            
    print()
    return strs[0]
   
a = ["flower","flow","flight"]

print(longuestCommunPreix(a))