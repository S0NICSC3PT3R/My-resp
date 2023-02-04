scores = []
more_input = "Y"
while more_input == "Y":
    done = False
    while done == False:
        current_score = float(input("Please input score: "))
        if current_score < 100 and current_score > 0:
            scores = scores + [current_score]
            done = True
        else: print("ERROR, Number typed out of range")
    done = False
    while done == False:
        more_input = input("Do you want to enter another score? 'Y' or 'N': ")
        if more_input == 'Y' or more_input =='N':
            done = True
            if more_input == 'N': 
                sum = 0
                for num in scores: sum += num
                mean = sum//len(scores)
                print("Mean value is : ", int(mean))
        else:
            print("ERROR, Input not acceptable")
