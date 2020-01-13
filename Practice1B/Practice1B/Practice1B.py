#PRACTICE 1B SOLUTION

#1B edits 1A solution to allow user to control how many temps are entered (loop control no longer based on user answering a question every time)

#Starting Documentation
#-program prompt
#-pseudocode
#-starting notes
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY-------
#sumtotalTemps          the sum total of all F temps added during the session
#totalTemps             the count/number of temps added during session

#FUNCTIONS--------------------------------------------------------------------------

#BASE PROGRAM CODE / MAIN()---------------------------------------------------------

#initialize variables -- giving necessary vars initial values
sumtotalTemps = 0
totalTemps = 0

print("Welcome to my my Fahrenheit-t--Celsius Conversion Program!")

answer = int(input("\nEnter number of temps to convert for this session: "))

while (answer > totalTemps):
    
    tempF = float(input("Enter the temperature in Fahrenheit: "))

    totalTemps += 1             #same as: totalTemps = totalTemps + 1

    sumtotalTemps += tempF

    #FOR TESTING --> print(tempF)

    tempC = (tempF - 32) * (5 / 9)

    print("TEMPERATURES: {0:.1f}F | {1:.1f}C".format(tempF, tempC))

    #removed from previous 1A
    #answer = input("\nWould you like to go again? [y/n]: ")


#find the average of tempF
avgTempF = sumtotalTemps / totalTemps

avgTempC = (avgTempF - 32) * (5 / 9)

print("\nTEMPERATURES ENTERED: ", totalTemps)
print("AVERAGE TEMPS: {0:.1f} | {1:.1f}".format(avgTempF, avgTempC))

print("\n\nThank you for using my program!")