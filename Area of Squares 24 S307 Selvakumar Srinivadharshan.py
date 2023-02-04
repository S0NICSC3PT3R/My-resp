x11, y11, x12, y12 =input("Set 1: ").split()
x11 = int(x11)
y11 = int(y11)
x12 = int(x12)
y12 = int(y12)
x21, y21, x22, y22 =input("Set 2: ").split()
x21 = int(x21)
y21 = int(y21)
x22 = int(x22)
y22 = int(y22)
if x21 in range(x11,x12+1) :
     if x21 > x11:
          print((x21-x11)*(y21-y11))
     elif x11>x21:
          print((x11-x21)*(y11-y21))
elif x22 in range(x11,x12+1) :
     if x22 > x11:
          print((x21-x11)*(y21-y11))
     elif x11>x21:
          print((x11-x21)*(y11-y21))
else:
     print("No overlaying area")
     
     
