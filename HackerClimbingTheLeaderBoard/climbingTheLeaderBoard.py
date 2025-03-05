#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # [ 100 100 50 40 40 20 10 ]
    ranked.sort(reverse=True)
    ranks = []
    # { 100 50 40 20 10 }
    uniques = []
    for score in ranked:
        if len(uniques) == 0 or (uniques and score != uniques[-1]):
            uniques.append(score)
            
    if len(uniques) == 0:
        ranks.append(1)
            
    # [ 5 25 50 120 ]
    # since by getting rid of elements player
    # we dont need to iterate throught the whole array every single score
    # { 100 50 40 20 10 }  5 <-[25 50 120]
    
    else:
        # last index so { 100 50 40 20 [10] }
        i = len(uniques) - 1
        for playerScore in player:
            # only decrements if the player score is higher
            while i >= 0 and playerScore > uniques[i]:
                i -= 1
            
            # once stopped there is only 2 cases 
            # score is equal to current score
            if playerScore == uniques[i]:
                # index is the rank - 1
                # to get the rank just add +1 to index
                rank = i + 1
                ranks.append(rank)
            else:
                # the score is higher than the current score
                # add 1 to get the rank of the current score and add 1 to get player's score
                rank = i + 1
                ranks.append(rank + 1)
                    
    return ranks
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
