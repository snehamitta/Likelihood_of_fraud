import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls

#Reading Data

data = pd.read_csv("/Users/snehamitta/Desktop/ML/Assignment 1/NormalSample(1).csv")

#Q2.a) To find five number summary of X

Q1 = np.percentile(data.iloc[:,0].values, 25)
Q3 = np.percentile(data.iloc[:,0].values, 75)
Q2 = np.percentile(data.iloc[:,0].values, 50)

iqr = Q3 - Q1

LW = Q1 - 1.5*iqr
UW = Q3 + 1.5*iqr

print ("The five number summary for x are", LW, Q1, Q2, Q3, UW)
a1 = [LW, Q1, Q2, Q3, UW]

#To check for outliers
o1 = []
for i in range (0, len(data)):
	if data.iloc[:,0][i] < LW and data.iloc[:,0] > UW:
		o1.insert(i,data.iloc[:,0][i])
print("The outliers for this boxplot are", o1)

#Q2.b) To find five number summary of X for each category of group

g1 = []
g2 = []

for i in range(0, len(data)):
	if data.iloc[:,1][i] == 1:
		g1.insert(i,data.iloc[:,0][i])
	elif data.iloc[:,1][i] == 0:
		g2.insert(i,data.iloc[:,0][i])


Q1 = np.percentile(g1, 25)
Q3 = np.percentile(g1, 75)
Q2 = np.percentile(g1, 50)

iqr = Q3 - Q1

LW = Q1 - 1.5*iqr
UW = Q3 + 1.5*iqr

print ("The five number summary for x in group 1 are", LW, Q1, Q2, Q3, UW)
a2 = [LW, Q1, Q2, Q3, UW]

# To check for outliers
o2 = []
for i in range (0, len(data)):
	if data.iloc[:,0][i] < LW and data.iloc[:,0] > UW:
		o2.insert(i,data.iloc[:,0][i])		
print("The outliers in group 1 are", o2)

Q1 = np.percentile(g2, 25)
Q3 = np.percentile(g2, 75)
Q2 = np.percentile(g2, 50)

iqr = Q3 - Q1

LW = Q1 - 1.5*iqr
UW = Q3 + 1.5*iqr

print ("The five number summary for x in group 0 are", LW, Q1, Q2, Q3, UW)
a3 = [LW, Q1, Q2, Q3, UW]

# To check for outliers
o3 = []
for i in range (0, len(data)):
	if data.iloc[:,0][i] < LW and data.iloc[:,0] > UW:
		o3.insert(i,data.iloc[:,0][i])
print("The outliers in group 0 are", o3)

#Q2.c) Boxplot of x

plt.boxplot(data.iloc[:,0].values)
plt.show()

#Q2.d) Boxplot of all three

finalplot = [data.iloc[:,0].values, g1, g2]

mpl_fig = plt.figure(1, figsize=(9, 6))
ax = mpl_fig.add_subplot(111)

ax.boxplot(finalplot)
plt.show()




