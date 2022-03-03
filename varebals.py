

def askForInput(qustion, needs_to_be_above_zero = "N"):
    num_1 = int(input(qustion))
    if needs_to_be_above_zero == "Y":
        if num_1 > 0:
           return num_1
        else:
            print("please enter a nuber above Zero")
    else:
        return num_1

width = askForInput("what is the width", "Y")
