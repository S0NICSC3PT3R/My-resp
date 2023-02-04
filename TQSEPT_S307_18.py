#Grades Function
def getGrades(N):
     grade = ""
     if N >= 75:
          grade = "A1"
     elif N >=70:
          grade = "A2"
     elif N >=65:
          grade = "B3"
     elif N >=60:
          grade = "B4"
     elif N >=55:
          grade = "C5"
     elif N >=50:
          grade = "C6"
     elif N >=45:
          grade = "D7"
     elif N >=40:
          grade = "E8"
     else:
          grade = "F9"
     return(grade)

#Validations and inputs
valid = False
while valid == False:
     L1 = input("L1 : ")
     try:
          float(L1)
     except ValueError:
          print("Value must be a Float")
     else:
          L1 = float(L1)
          valid = True
          
valid = False
while valid == False:
     L2 = input("L2 : ")
     try:
          float(L2)
     except ValueError:
          print("Value must be a Float")
     else:
          L2 = float(L2)
          valid = True

valid = False
while valid == False:
     M1 = input("M1 : ")
     try:
          float(M1)
     except ValueError:
          print("Value must be a Float")
     else:
          M1 = float(M1)
          valid = True

valid = False
while valid == False:
     M2 = input("M2 : ")
     try:
          float(M2)
     except ValueError:
          print("Value must be a Float")
     else:
          M2 = float(M2)
          valid = True

valid = False
while valid == False:
     S1 = input("S1 : ")
     try:
          float(S1)
     except ValueError:
          print("Value must be a Float")
     else:
          S1 = float(S1)
          valid = True

valid = False
while valid == False:
     S2 = input("S2 : ")
     try:
          float(S2)
     except ValueError:
          print("Value must be a Float")
     else:
          S2 = float(S2)
          valid = True

valid = False
while valid == False:
     H1 = input("H1 : ")
     try:
          float(H1)
     except ValueError:
          print("Value must be a Float")
     else:
          H1 = float(H1)
          valid = True

valid = False
while valid == False:
     H2 = input("H2 : ")
     try:
          float(H2)
     except ValueError:
          print("Value must be a Float")
     else:
          H2 = float(H2)
          valid = True

#Displaying Grades
print("L1:",getGrades(L1))
print("L2:",getGrades(L2))
print("M1:",getGrades(M1))
print("M2:",getGrades(M2))
print("S1:",getGrades(S1))
print("S2:",getGrades(S2))
print("H1:",getGrades(H1))
print("H2:",getGrades(H2))

#L1R3B1
L1 = int(str(getGrades(L1))[1])
R3 = 0
if M1 < M2:
     M = M2
else:
     M = M1
if S1 < S2:
     S = S2
else:
     S = S1
if H1 < H2:
     H = H2
else:
     H = H1
R3 += (int(str(getGrades(M))[1]) +int(str(getGrades(S))[1])+int(str(getGrades(H))[1]))

B1 = 0

if M1 != M:
     M = M2
else:
     M = M1
     
if H1 != H:
     H = H2
else:
     H = H1

if S1 != S:
     S = S2
else:
     S = S1
     
M = int(str(getGrades(M))[1])
S =int(str(getGrades(S))[1])
H = int(str(getGrades(H))[1])

B1 = max(S,H,M)

print("L1R3B1 : "+str(R3+B1+L1))
