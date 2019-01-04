import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading data

data = pd.read_csv("/Users/snehamitta/Desktop/ML/Assignment 1/Fraud(1).csv")

# Q3.a) Percentage of cases found to be fradulent

x = 0
y = 0
for i in range (0, len(data)):
	if data.iloc[:,1][i] == 1:
		x = x + 1
	else:
		y = y + 1

percentage = (x/len(data)) * 100
percent = round(percentage, 4)
print("The percent of investigations that were found to be fraudulent are", percent)

# Q3.b) To find boxplots for all interval variables based on their fraud quotient

ts1 = [] 
ts0 = []
dv1 = []
dv0 = []
nc1 = []
nc0 = []
md1 = []
md0 = []
op1 = []
op0 = []
nm1 = []
nm0 = []

for i in range(0, len(data)):
	if data.iloc[:,1][i] == 1:
		ts1.insert(i,data.iloc[:,2][i])
		dv1.insert(i,data.iloc[:,3][i])
		nc1.insert(i,data.iloc[:,4][i])
		md1.insert(i,data.iloc[:,5][i])
		op1.insert(i,data.iloc[:,6][i])
		nm1.insert(i,data.iloc[:,7][i])
	elif data.iloc[:,1][i] == 0:
		ts0.insert(i,data.iloc[:,2][i])
		dv0.insert(i,data.iloc[:,3][i])
		nc0.insert(i,data.iloc[:,4][i])
		md0.insert(i,data.iloc[:,5][i])
		op0.insert(i,data.iloc[:,6][i])
		nm0.insert(i,data.iloc[:,7][i])

ts3 = [ts0,ts1]
dv3 = [dv0,dv1]
nc3 = [nc0,nc1]
md3 = [md0,md1]
op3 = [op0,op1]
nm3 = [nm0,nm1]

df = pd.DataFrame(ts3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()

df = pd.DataFrame(dv3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()

df = pd.DataFrame(nc3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()

df = pd.DataFrame(md3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()

df = pd.DataFrame(op3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()

df = pd.DataFrame(nm3, index=['fraud = 1', 'fraud = 0'])
df.T.boxplot(vert=False)
plt.subplots_adjust(left=0.25)
plt.show()


