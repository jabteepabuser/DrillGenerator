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
#COUNTER ENDS

#DRILL DATABASE ENDS HERE




#FUNCTION STARTS HERE
print("Remember to do each drill with the intent of flow and nothingness. Add Exits for safety.")
print(" Counters\n Weaknesses \n Blitzing Combos \n Initiation")
user_input: str = input("What do you wish to work on? ")

#random.choice is the function for random items.
random_drill = random.choice(counter_list)

if user_input == "Counters":
    print(random_drill)
elif user_input == "counters":
    print(random_drill)
else:
    print("Error, please only enter the ones above.")



#FUNCTION ENDS HERE