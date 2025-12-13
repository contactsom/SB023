myStudentDetails={
    1:"Siva",
    2:"Manshi",
    3:"Amit",
    4:"Nitish",
    5:"Narendra",
    6:"ABC",
    600:"Simplilearn",

}
print(myStudentDetails)
myStudentDetails.setdefault(600,"I am 600 default Value")
myStudentDetails.setdefault(400,"I am 400 default Value")
myStudentDetails.setdefault(601,"I am 601 default Value")

print(myStudentDetails[600])
print(myStudentDetails[400])
print(myStudentDetails[601])












