import numpy as np
import pandas as pd
import os
import copy

folder = 'MATTHEW'
filename = 'Mat-'
suffix = '.csv'

verification = list(range(1, 6)) + list(range(1, 6)) + list(range(1, 6))
#each one of these needs to be a string
for i in range(len(verification)):
    verification[i] = str(verification[i])
#create output dataframe
data = pd.DataFrame(columns = ["number", "value1", "value2", "value3", "value4"])
data["number"] = verification
Error = False

for order in range(1, 5):
    #generate new file name
    file = folder + '/' + filename + str(order) + suffix
    f = open(file, "r")
    lines = f.readlines()
    lastline = lines[-1]
    f.close()

    lastline = lastline.split(',')

    #extract the odd index values
    values = lastline[1::2]
    #extract the even index values
    numbers = lastline[::2]
    #and drop the last number
    numbers = numbers[:-1]

    #assert that every button has been pressed
    if (numbers != verification):
        print("ERROR: not all buttons have been pressed" + str(order))
        print("numbers: " + str(numbers))
        print("verification: " + str(verification))
        break

    #add values in the data
    data["value" + str(order)] = values

if (not Error):
    print(data)
    data.to_csv(filename + "buttons.csv")