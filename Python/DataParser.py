import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

folder = 'Matthew'
filename = 'Mat-4'
suffix = '.csv'
file = folder + '/' + filename + "-cleaned" + suffix     
#----------------------------------
header1 = ["time", "PosX", "PosY", "PosZ","LeftX","LeftY", "LeftZ", "RightX", "RightY", "RightZ"]
header2 = ["AccAngularX", "AccAngularY", "AccAngularZ", "AccLinearX", "AccLinearY", "AccLinearZ", "VelAngularX", "VelAngularY", "VelAngularZ", "VelLinearX", "VelLinearY", "VelLinearZ"]
header = header1 + header2
data = pd.read_csv(file, sep=',', names=header)

#----------------------------------
#for now, DROP everything in dropdata from data
dropdata = ["AccAngularX", "AccAngularY", "AccAngularZ", "VelAngularX", "VelAngularY", "VelAngularZ", "AccLinearX", "AccLinearY", "AccLinearZ"]
data.drop(dropdata, axis=1, inplace=True)
#----------------------------------
#calculate the velocityXYZ taking into account of time interval
timediff = data["time"].diff()
data["VelLinearX"] = data["PosX"].diff() / timediff
data["VelLinearY"] = data["PosY"].diff() / timediff
data["VelLinearZ"] = data["PosZ"].diff() / timediff
data["VelLinearX"][0] = 0
data["VelLinearY"][0] = 0
data["VelLinearZ"][0] = 0
#----------------------------------
#calculate the magnitude of the velocity from XYZ
data["VelLinearMag"] = np.sqrt(data["VelLinearX"]**2 + data["VelLinearY"]**2)
#----------------------------------
#----------------------------------
#save as a new csv file called "Andy-1-processed.csv"
data.to_csv(filename + "-processed.csv", sep=',', index=False)