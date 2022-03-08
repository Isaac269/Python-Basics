
# inport requred modules
from pkg_resources import require


try:
    import pyttsx3
    module = 1
except:
    print("pyttsx3 not found")
    module = 0
print("")
# speak command
def speak(text):
    if module == 1:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        pass


def ask_For_Input(qustion, needs_to_be_above_zero = "N"):
    
    try:
        # get number
        qustion = qustion + " "
        num_1 = int(input(qustion))

        # checks if it needs to be above zero
        if needs_to_be_above_zero == "N":
            return num_1
        else:
            if num_1 > 0:
                return num_1
            else:
                print("please enter a number above 0")
                speak("please enter a number above 0")
                num_1 = 1
                return num_1
    except ValueError:
        print("please enter a number above 0")
        speak("please enter a number above 0")
        num_1 = 1
        return num_1
    
    

loop = False

while not loop:
    # get input
    width = ask_For_Input("what is the width", "Y")
    print("")
    height = ask_For_Input("what is the height", "Y")
    print("")
    # calculate the perimenter 
    area = (width * height)
    perimenter = (width * 2 + height * 2)
    # gives output
    print("this is the area ",area,"² units")

    speak("this is the area")
    speak(area)
    print("")

    print("this is the perimenter ",perimenter, " units")

    speak("this is the perimenter")
    speak(perimenter)

    print("")

    # checks if you wish to repeat
    end_loop = input("do you want to use the program again ")

    if "0" in end_loop or "y" in end_loop or "yes" in end_loop:
        loop = False
    else:
        loop = True
    