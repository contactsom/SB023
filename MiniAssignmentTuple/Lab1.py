viratScoreTuple=(34,56,76,89,99,34,76)

# 1. Find the Higest Scored Run
higestScore = max(viratScoreTuple)
print("Find the Higest Scored Run :: ",higestScore)

# 2. Find the Lowest Score Run
lowestScore = min(viratScoreTuple)
print("Find the Lowest Score Run :: ",lowestScore)
# 3. Find the duplicate score or two matches same score

viratScoreTuple=(34,56,76,89,99,34,76)
'''
# Simple Solutions
for score in viratScoreTuple:
    if viratScoreTuple.count(score)>1 :
        print("Duplicate Score Found ",{score},"Count ",{viratScoreTuple.count(score)})
'''

seen=()
for score in viratScoreTuple:
    if score not in seen:
        if viratScoreTuple.count(score) > 1:
            print("Duplicate Score Found ", {score}, "Count ", {viratScoreTuple.count(score)})
        seen=seen+(score,)

