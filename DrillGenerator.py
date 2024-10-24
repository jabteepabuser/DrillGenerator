#random module
import random


#DRILL DATABASE STARTS HERE
#COUNTERS
counter_list: list[str] = []
counter_list.append("Parry Teep - Left Liver Shot - Left Hook - Low Kick.")
counter_list.append("LeanBack from Hook - Rear Body Kick - Cross - Lead Upper Elbow.")
counter_list.append("Defend Lead Hand Parry - Left Hook - Low Kick.")
counter_list.append("Parry Cross - Lead Downward Elbow - Knee.")
counter_list.append("Slip Jab - Cross - Lead Upper - Low Kick.")
counter_list.append("Cross Check Inside Leg - Low Kick - Teep.")
counter_list.append("Check Rear Kick - Lead Teep.")
counter_list.append("Long Guard  (Defend Against Overhand Right) - Rear Upper - Left Hook - Low Kick.")
counter_list.append("Arm Block Left Hook - Cross - Left Hook - Body Kick.")
counter_list.append("Move lead leg back - Rear Teep.")

#COUNTER ENDS
#DRILL DATABASE ENDS HERE




#FUNCTION STARTS HERE
#generates a random combo from database
while True: #while True means that while all conditions are true, keep executing, break ends it.
    random_counter = random.choice(counter_list) # for counters #random.choice is the function for random items.
    print("Remember to do each drill with the intent of flow and nothingness. Add Exits for safety.") #first loop
    print("What do you wish to work on? \n Counters\n Weaknesses \n Blitzing Combos \n Initiation")
    user_input: str = input("").strip().lower() #makes the program not care about the spacing nor the capitalization of input.
    if user_input == "counters":
        print(random_counter) #proceeds to the second loop
    else: #prints an error message if the user does an invalid input.
        print("Error, please only enter the ones above. or check your spelling.")
        continue #goes back to the first loop

    print("Would you like to do another combo? Y/N?") #this is the second loop
    last_prompt = input("").strip().lower()
    if last_prompt != "y": #loop ends if the condition is not true
        print("Fuck You Then LOL.")
        break #initially breaks loop.


#FUNCTION ENDS HERE