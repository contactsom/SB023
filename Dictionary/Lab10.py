myStudentDetails={
    1:"Siva",
    2:"Manshi",
    3:"Amit",
    4:"Nitish",
    5:"Narendra",
    6:"ABC"
}

print(myStudentDetails[1])
print(myStudentDetails[2])
print(myStudentDetails[3])
print(myStudentDetails[4])
print(myStudentDetails[5])

if (6 in myStudentDetails):
    print(myStudentDetails[6])
else:
    print(" Key 6 Does not exist")

'''
6 you have not defined inside bracket so python will automatically consider it as key value?
'''


