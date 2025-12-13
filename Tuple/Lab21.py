#-6  -5, -4, -3, -2, -1 => -Ve Index
# A   B   C   D   E   F
# 0   1   2   3   4   5 => +Ve Index

# Slice [X:Y]
# Here X = Start Index
# Y = End Index , [Y-1]th Value
# X<=Y

myNameList=("A","B","C","D","E","F")
print(myNameList[-1:-3]) # [] because start index > End Index
print(myNameList[-5:-3]) # ['B', 'C']
print(myNameList[-6:-1]) # ['A', 'B', 'C', 'D', 'E']
print(myNameList[-0:-0]) # [] Because there is nothing called -0
print(myNameList[-6:-100]) # []
print(myNameList[-100:-6]) # []








