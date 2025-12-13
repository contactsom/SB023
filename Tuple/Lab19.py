#-6  -5, -4, -3, -2, -1 => -Ve Index
# A   B   C   D   E   F
# 0   1   2   3   4   5 => +Ve Index

myNameTuple=("A","B","C","D","E","F") # String
print(myNameTuple)
print("**** Before Change **** ")
myNameTuple[0]="Apple" # I am trying to update the Value
# TypeError: 'tuple' object does not support item assignment

print("**** After Change **** ")
print(myNameTuple)


