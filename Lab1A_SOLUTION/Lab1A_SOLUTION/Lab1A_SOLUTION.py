#LAB 1A SOLUTION 

#PROGRAM PROMPT:
#Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend.  If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations.  The user should be allowed to enter as many rooms as the want.  

#VARIABLE DICTIONARY:
#
#
#
#
#
#


#NOTES:
#       *all person displays should be positive!
#       *num = abs(num)  OR num = num * -1  OR num *= -1

#BASE PROGRAM CODE------------------------------------------------------------------

print("Welcome to my ROOM CAPACITY program!")

answer = input("Please enter 'y' to begin: ")

while answer == "y" or answer == "Y":

    room_cap = int(input("\n\tEnter the room capacity: "))
    attending = int(input("\n\tEnter the people attending the meeting: "))

    difference = room_cap - attending

    if difference > 0: #there are seats left in the room


    elif difference < 0: #the room has been oversold


    else: #the room is exactly at capacity



    answer = input("Would you like to check another room? [y/n]: ")




#FURTHER NOTES ABOUT PROGRAM:
#input values should be based off of integers -- you can't have 1/2 of a person