print("Let's Revise")
print()

#Int, Bool, String, Float
anInt:int = 3
print(anInt)
DeclareValFirst:float
DeclareValFirst = 7.35
print(DeclareValFirst)
print()

#Declaring Variables
#An identifier must contain only alphabets, number or underscore symbol. 
#[ "A-Z", "a-z", "0-9", "_" ]
#An identifier must start with an alphabet. Delete hashtag in next 2 lines to see error
#!kskskhkj&^% = 0
#print(!kskskhkj&^%)


#To the power of is "**"
print(3**2)
print()

#Modulo(Remainders) is "%"
print(3%2)
print()

#Add(+), Subtract(+), Multiply(*), Divide(/), Int Divide(//)
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print()

#String Interpolation
ThisValue = 10
print(ThisValue,"is the value of ThisValue")
print()

#Loops
Number = int(input("Type a number: "))
for i in range(Number):
     #range = 0...n-1
     print(i)
print()

for i in range(7,6):
     print(i) # 9 to 12-1
print()

for i in range(0,11,2):
     print(i) # 0 to 10(11 - 1) increased by 2 - 0,2,4 etc
print()

for i in range(10,0,-1):
     print(i) #10 to 1(one number before 0 in this sense), increased by -1 - 10,9,8
print()

for i in "Chicken Wings":
     print(i)


