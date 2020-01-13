#PRACTICE 1C - FUNCTION -SOLUTION

#1C edits 1B to include a function. This function handles the Celsius conversion. This function should be passed the temp in F and return the temp in C.  This function should be called any time a celsius conversion takes place.
#PARAMETER --> values that the function relies on in order to complete its execution (needed values)
#ARGUMENTS --> values that are passed to a function during the function call to supply waiting variables in the function header (PARAMETERS) so that it may execute properly

#Starting Documentation
#-program prompt
#-pseudocode
#-starting notes
#-guidelines / information for anyone reading your documentation

#VARIABLE DICTIONARY-------
#sumtotalTemps          the sum total of all F temps added during the session
#totalTemps             the count/number of temps added during session

#FUNCTIONS--------------------------------------------------------------------------

def celsius(tf): #<--FUNCTION HEADER

    #running the conversion to celsius
    tc = (tf - 32) * (5 / 9)

    #return that celsius value
    return tc

    #nothing will execute after the return -- because the machine is literally transferring a value here and returning to the point of call
    print("howdy")


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

    #tempC = (tempF - 32) * (5 / 9)
    
    tempC = celsius(tempF)
    

    print("TEMPERATURES: {0:.1f}F | {1:.1f}C".format(tempF, tempC))

    #removed from previous 1A
    #answer = input("\nWould you like to go again? [y/n]: ")


#find the average of tempF
avgTempF = sumtotalTemps / totalTemps

avgTempC = celsius(avgTempF)

print("\nTEMPERATURES ENTERED: ", totalTemps)
print("AVERAGE TEMPS: {0:.1f} | {1:.1f}".format(avgTempF, avgTempC))

print("\n\nThank you for using my program!")