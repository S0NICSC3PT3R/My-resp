#Range check
while True:
     x = int(input("Enter marks(0...100) : "))
     if 0<= x and x <= 100:
          break
     else:
          print("Invalid input ")

#Type check
while True:
     try:
          x = int(input("Enter marks(0...100) : "))
          if 0<= x and x <= 100:
               break
          else:
               raise Exception
     except Exception:
          print("Your input is invalid")
          
#Presence check
while True:
     y = input("Type your name : ")
     if y != "":
          break
     else:
          print("Invalid input")
