#Week 2 Day 1: Importing Data from a File

#YOU MUST IMPORT THE CSV LIBRARY IN ORDER FOR FILES TO BE ACCESSED

#CSV: Comma Separated Values
#RECORDS: rows of the file, different types of data all belonging together
#FIELDS: columns of the file, sets of data (all data in a column is the same "type" ie names, ages, salaries, email addresses, etc)

#BASE PROGRAM CODE-------------------------------------------------------------------

import csv #import csv library so we can read the file


total_records = 0 #you should ALWAYS have a total records var for your first few attempts at file reading

total_salary = 0 #holds all salaries in file for total print at end

#prnt header
print("{0:15} \t {1} \t {2:10}".format("NAME", "AGE", "SALARY"))


#right-click the text/csv file in folder view --> "Properties" to find the file location
#these file locations are cAsE sEnSiTiVe & space/special character sensitive so DOUBLE CHECK THEM!
#flip all '\' to '/'

with open("C:/Users/KTRUCHON/Downloads/example.csv") as csvfile: 

    #notice ':' everything must be INDENTED now (until we're ready to "close" the file)

    file = csv.reader(csvfile)
    #now the file we have connected is known in the program as 'file'
    #file has several records, each record has several fields

    #below is a FOR loop
    #for loops are loops -- continually repeated sequence of code
    #they continue NOT based on a CONDITION but on a RANGE
    #range: '0 - 10', 'a - f'
    
    for rec in file:

        #notice the ':' everything in the for loop must be INDENTED
        #RANGE: for each record in the file, do the following
        #rec is a variable that is initialized the the for loop range
        #           on line 35

        total_records += 1 #total_records = total_records + 1

        #print(rec) #print entire record of file. we are seeing this as a LIST
                    #lists can hold multiple points of data at once
                    #in order to specify a data point over another, we need to know its POSITION IN THE LIST

        #print only the names in the file -- specify position of data in lit
        #print("RECORD #: {0} \t {1}".format(total_records, rec[0]))

        #print("RECORD #: {0} \t {1} \t${2}".format(total_records, rec[0], rec[2]))

        #add all salaries to total_salary -- REMEMBER: all data entering a Python program is treated as a STRING unless cast otherwise
        total_salary += float(rec[2])


        
        print("{0:15} \t {1} \t ${2:10,.2f}".format(rec[0], rec[1], float(rec[2])))
        #add field width to ensure columns stay aligned

 

print("\n\nTOTAL RECORDS: ", total_records)
print("TOTAL SALARY: ${0:.2f}".format(total_salary))