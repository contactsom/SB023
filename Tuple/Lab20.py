#-6  -5, -4, -3, -2, -1 => -Ve Index
# A   B   C   D   E   F
# 0   1   2   3   4   5 => +Ve Index

# Slice [X:Y]
# Here X = Start Index
# Y = End Index , [Y-1]th Value
# X<=Y

myNameList=("A","B","C","D","E","F")
print(myNameList[1:3]) # ['B', 'C']
print(myNameList[1:5]) # ['B', 'C', 'D', 'E']
print(myNameList[0:50]) # ['B', 'C', 'D', 'E','F']
print(myNameList[0:0]) # []
print(myNameList[:]) # ['A', 'B', 'C', 'D', 'E', 'F']





