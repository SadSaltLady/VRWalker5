import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


file = 'ANDY/Andy-2.csv'
data = pd.read_csv(file, sep='\t')
#extract the last row 
lastrow = data.iloc[-1]
#delete last row
data = data.drop(data.index[-1])
#sanitize the rows
averagelen = 180
#check for rows longer than averagelen
print(len(data.iloc[0].to_string()))
'''
for i in range(len(data)):
    if len(data.iloc[i]) > averagelen:
        print("ERROR: row " + str(i) + " is " + str(len(data.iloc[i])) + " long")
        print(data.iloc[i])
print(averagelen)
'''


assert(False)
#----------------------------------
header1 = ["time", "PosX", "PosY", "PosZ","LeftX","LeftY", "LeftZ", "RightX", "RightY", "RightZ"]
header2 = ["AccAngularX", "AccAngularY", "AccAngularZ", "AccLinearX", "AccLinearY", "AccLinearZ", "VelAngularX", "VelAngularY", "VelAngularZ", "VelLinearX", "VelLinearY", "VelLinearZ"]
header = header1 + header2
data = pd.read_csv(file, sep=',', names=header)

#----------------------------------
#for now, DROP everything in dropdata from data
dropdata = ["AccAngularX", "AccAngularY", "AccAngularZ", "VelAngularX", "VelAngularY", "VelAngularZ"]
data.drop(dropdata, axis=1, inplace=True)
#----------------------------------
#calculate the velocityXYZ
data["VelLinearX"] = data["PosX"].diff()
data["VelLinearY"] = data["PosY"].diff()
data["VelLinearZ"] = data["PosZ"].diff()
data["VelLinearX"][0] = 0
data["VelLinearY"][0] = 0
data["VelLinearZ"][0] = 0
#----------------------------------
#plot "PosX", "PosY" on an XY graph
'''
plt.plot(data["PosX"], data["PosY"])
plt.show()
'''
#----------------------------------
#save as a new csv file called "Andy-1-processed.csv"
#data.to_csv("Andy-2-processed.csv", sep='\t', index=False)
#print(data)