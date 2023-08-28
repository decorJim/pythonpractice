class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        map={                       # map containing digit mapped to their letters
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }

        temp=""                     # variable to store a single combination
        answers=[]                  # array to store all possible combination

        def process(index,word):    # takes current index of the input and temporary constructed word
          if len(word)==len(digits):
             answers.append(word)
             return
          else:
             key=int(digits[index])     # set the key for example "abc" [0]=a
             for character in map[key]:           # iterate through all letter in corresponding array
                 process(index+1,word+character)  # recursion call function but increment index and glue character of the current level 
                                                  # before going to next function call
        process(0,temp)
        return answers  