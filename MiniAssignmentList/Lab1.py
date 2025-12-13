viratScoreList=[34,56,76,89,99,34,76]
print(viratScoreList)

# 1. Remove all the duplicate score
viratSet=set(viratScoreList)
viratUniqueScoreList=list(viratSet)
print("1. Remove all the duplicate score")
print(viratUniqueScoreList)

# 2. Short this score in to descending order
viratScoreList.sort(reverse=True)
print("2. Short this score in to descending order")
print(viratScoreList)

# 3. Find the Avg. of Score
sumofSore = sum(viratScoreList)
print("Sum ::",sumofSore)
numberofMatches=len(viratScoreList)
print("Number of Matches ::",numberofMatches)
avgofScore=sumofSore/numberofMatches
print("AVG::",avgofScore)

# 4. Count the number of Matches which score more than 70
count=0
for x in viratScoreList:
    if( x>70):
        count=count+1
print("Total Count :: ",count)
