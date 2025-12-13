viratScoreSet={34,56,76,89,99,34,76}
print(viratScoreSet)

# 1. Remove all the duplicate score
print(viratScoreSet) # Set will automatically do that

# 2. Short this score in to descending order
print("2. Short this score in to descending order")
# Home Assignment

# 3. Find the Avg. of Score
sumofSore = sum(viratScoreSet)
print("Sum ::",sumofSore)
numberofMatches=len(viratScoreSet)
print("Number of Matches ::",numberofMatches)
avgofScore=sumofSore/numberofMatches
print("AVG::",avgofScore)

# 4. Count the number of Matches which score more than 70
count=0
for x in viratScoreSet:
    if( x>70):
        count=count+1
print("Count the number of Matches which score more than 70 :: ",count)

# 5. Remove the duplicate word from String
myString = "Get Certified Get Ahead "
wordList=myString.split()
print(wordList) # ['Get', 'Certified', 'Get', 'Ahead']
wordSet=set(wordList)
print(wordSet)