import numpy as np
import pandas as pd
import os
import copy

'''
this file cleans all the errors that could have been generated and prepares 
it for DataParser.py. It writes to a new file called filename-cleaned.csv
'''

folder = 'MATTHEW'
filename = 'Mat-'
suffix = '.csv'
for order in range(1, 5):
    #generate new file name
    file = folder + '/' + filename +str(order) + suffix

    #get the average length of all the rows
    f = open(file, "r")
    l = f.readlines()
    lines = copy.deepcopy(l)
    f.close()
    #get rid of the last line because it's not the right data
    lines = lines[:-1]
    #calculate the average length
    averagelen = 0 
    averagelenbuffer = [len(lines[i]) for i in range(len(lines))]
    averagelen = sum(averagelenbuffer)
    averagelen = averagelen / len(lines)
    print ("average length: " + str(averagelen))
    iterations = 0
    alldone = False
    while(not alldone):
        #go through again and check for rows longer than averagelen
        count = 0
        caughtIndex = []
        caughtItems = []
        cleanedItem = []
        extraItems = []
        for i in range(len(lines)):
            if len(lines[i]) > averagelen:
                count+= 1
                caughtIndex.append(i)
                caughtItems.append(lines[i])
        print("caught: " + str(count))

        #add extra lines to files such that the insert doesn't go out of bounds later
        for i in range(len(caughtItems)):
            lines.append('')

        #correct each of the caught items
        for i in range(len(caughtItems)):
            caught = caughtItems[i]
            #split line by comma
            caught = caught.split(',')
            #break line after 22 commas
            #clean = data at the line i
            clean = caught[:22]
            clean[-1] = "0.00 \n"
            clean = ','.join(clean)
            #extra = data that got bunched up
            extra = caught[21:]
            extra[0] = extra[0][4:] #account for error of appending 0.00
            extra = ','.join(extra)
            #write to the lists
            extraItems.append(extra)
            cleanedItem.append(clean)

        #insert these items into the file
        for i in range(len(caughtItems)):
            lines[caughtIndex[i] + i] = cleanedItem[i]
            lines.insert(caughtIndex[i] + i + 1, extraItems[i])

        #check that it's actually right
        complete = True
        for i in range(len(lines)):
            if (len(lines[i]) > round(averagelen + 1)):
                print(str(i) + "is wrong")
                complete = False
                iterations += 1
                break
        
        if complete:
            alldone = True
        else:
            alldone = False

    print("iterations: " + str(iterations))
    #final verification: make sure the first element of each line is stricly increasing
    first = ''
    firstprev = ''
    for i in range(len(lines)):
        if i == 0:
            first = lines[i].split(',')[0]
            continue
        else:
            #get the first element of each line
            firstprev = first
            first = lines[i].split(',')[0]
            #compare the first element of the current line to the first element of the previous line
            if ((first < firstprev) and (first != '')):
                print("error at line: " + str(i))
                print("first: " + first)
                print("line: " + lines[i])
                print("firstprev: " + firstprev)
                print("lineprev: " + lines[i-1])
                print("")

    #write the file to file+'cleaned'
    newfilename = folder + '/' + filename +str(order) + "-cleaned" + suffix
    #make new file and write to it
    with open(newfilename, 'w') as ff:
        for line in lines:
            ff.write(line)

    #close files
    ff.close()