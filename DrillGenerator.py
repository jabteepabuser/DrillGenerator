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

#FEINTS
feint_list: list[str] = []
feint_list.append("Teep - Fake Teep - Left Hook.")
feint_list.append("Teep - Fake Teep - Jab - Low Kick")
feint_list.append("Teep - Fake Teep - Jab - Lead Head Kick - Cross.")
feint_list.append("Lead Hand Trap - Lead Uppercut Once Their Arm Is Extended - Cross - Low Kick.")
feint_list.append("Jab Jab - Cross to body - Fake Body Cross - Left Hook - Low Kick.")
feint_list.append("Teep - Fake Teep - Check Hook - Head Kick.")
feint_list.append("Teep - Fake Teep - Switch Head Kick - Cross.")
feint_list.append("JabCross - Fake Cross - Livershot - Low Kick.")
feint_list.append("Jab - Low Kick - Feint Dip - Feint Low Kick - Sweep Leg if opponent Leg Raised.")
#FEINTS ENDS

#BLITZ
blitz_list: list[str] = []
blitz_list.append("Jab - LivershotLeftHook - Switch Kick Head Off Centre Line. ")
blitz_list.append("Cross - Hook - Low Kick")
blitz_list.append("Overhand Right - Lead UpperCut - Low Kick.")
blitz_list.append("Overhand Right - Livershot - Low Kick.")
blitz_list.append("Jab - Check Hook to Left - Head Kick.")
blitz_list.append("Jab - Lead Upper - Head Kick.")
#BLITZ ENDS


#DRILL DATABASE ENDS HERE




#FUNCTION STARTS HERE
#generates a random combo from database
print("Welcome To DrillGenerator, Remember to flow in each combination and Add Exits for safety.")  # first prompt on UI.
while True: #while True means that while all conditions are true, keep executing, break ends it.
    random_counter = random.choice(counter_list) # for counters #this is where the initial loop begins.
    random_feint = random.choice(feint_list) # for feints #random.choice is the function for random items.
    random_blitz =random.choice(blitz_list) # for blitz #random.choice is the function for random items.
    print("What do you wish to work on? Write the first letter of the combo of your choice: \nCounters(C)\nFeints(F)\nBlitzing Combos(B)")#first prompt on UI as well.
    user_input: str = input("").strip().lower() #makes the program not care about the spacing nor the capitalization of input.
    if user_input == "c":
        print(random_counter) #proceeds to executing the function for counters
    elif user_input == "f":
        print(random_feint) #proceeds to executing the function for feint
    elif user_input == "b":
        print(random_blitz) #proceeds to executing the function for blitz.
    else: #prints an error message if the user does an invalid input.
        print("Error, please only enter the ones above. or check your spelling.")
        continue #continue means it goes back to the initial loop.

    print("Would you like to do another combo? Y/N?") #this is the second prompt
    last_prompt = input("").strip().lower()
    if last_prompt == "y":
        continue
    elif last_prompt== "n":
        print("Ok fuck off then lol.")
        break
    else:
        print("Error! Only input either Y or N!") #THIS PART NEEDS TO BE FIXED, INSTEAD OF ASKING THE FIRST PROMPT AGAIN, IT NEEDS TO ASK THE SECOND





#FUNCTION ENDS HERE