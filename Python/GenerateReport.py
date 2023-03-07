import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

folder = 'ANALYSIS'
filename = 'Mat-1'
suffix = '.csv'

file = folder + '/' + filename + "-processed" + suffix 

#read file 
data = pd.read_csv(file, sep=',')
#----------------------------------
#last round of cleaning
#subtract start form all the time values
data["time"] = data["time"] - data["time"][0]
#----------------------------------
#Distance based section:
#collect total distance travelled
Distances = np.sqrt(data["PosX"]**2 + data["PosY"]**2)
totalDistance = sum(Distances)

#----------------------------------
#Velocity based section:
#collect average and max velocity
maxVelocity = max(data["VelLinearMag"])
avgVelocity = np.mean(data["VelLinearMag"])

#----------------------------------
#Graphing section:
#plot the data
plt.plot(data["time"], data["VelLinearMag"]*100)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity over time" + filename)
plt.show()

#plot "PosX", "PosY" on an XY graph
#colorize the points based on the magnitude of the velocity
plt.scatter(data["PosX"], data["PosY"], c=data["VelLinearMag"], cmap='viridis')
plt.plot(data["PosX"], data["PosY"])
plt.show()


#save the graph
print (data)
print (totalDistance)