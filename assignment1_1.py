import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Reading Data

data = pd.read_csv('/Users/snehamitta/Desktop/ML/Assignment 1/NormalSample(1).csv')
N = (len(data))
print ("The number of observations are",N)

# Q1.a) Izenman Method for calculating the bin width

iqr = np.subtract(*np.percentile(data.iloc[:,0].values, [75, 25]))
h = (2*iqr)*(N**(-1/3))
print ("The Izenman method results the bin width as",h)

# Q1.b)The Beautification step

u = np.log10(h)
v = np.sign(u)*np.ceil(np.abs(u)) 
newh = 10**v
print ("The beautified bin width yields",newh)


# Q1.c) h = 0.5, minimum = 45, maximum = 55, to find coordinates of density estimator 
m = [] 
for i in range (45,55):
	x = i + 0.25
	m.append(x)
	x = i + 0.75
	m.append(x)
	
print ("The array of mid points are",m)

u = []
w = []
p = []
h = 0.5
	
for x in m:
	for y in data.iloc[:,0].values:
		z = (y - x)/h   
		u.append(z)
	for i in u:
		if i >= -0.5 and i <=0.5:
			w.append(1)
		else:
			w.append(0)
	del u[:]
	p.append(sum(w)/(N*h))
	del w[:]

print(p)

fig, ax = plt.subplots(nrows=1,ncols=1)
plt.step(m,p, where = 'mid')
ax.set_xticks(m)
plt.ylim(0,max(p)+0.1)
plt.show()

# Q1.d) h = 1, minimum = 45, maximum = 55, to find coordinates of density estimator 
m = []
for i in range (45,55):
	x = i + 0.5
	m.append(x)
	
print ("The array of mid points are",m)

u = []
w = []
p = []
h = 1
	
for x in m:
	for y in data.iloc[:,0].values:
		z = (y - x)/h   
		u.append(z)
	for i in u:
		if i >= -0.5 and i <=0.5:
			w.append(1)
		else:
			w.append(0)
	del u[:]
	p.append(sum(w)/(N*h))
	del w[:]

print(p)

fig, ax = plt.subplots(nrows=1,ncols=1)

plt.step(m,p, where = 'mid')
ax.set_xticks(m)
plt.ylim(0,max(p)+0.1)
plt.show()

# Q1.d) h = 2, minimum = 45, maximum = 55, to find coordinates of density estimator 
m = []
for i in range (45,55,2):
	x = i + 1
	m.append(x)

	
print ("The array of mid points are",m)

u = []
w = []
p = []
h = 2
	
for x in m:
	for y in data.iloc[:,0].values:
		z = (y - x)/h   
		u.append(z)
	for i in u:
		if i >= -0.5 and i <=0.5:
			w.append(1)
		else:
			w.append(0)
	del u[:]
	p.append(sum(w)/(N*h))
	del w[:]

print(p)

fig, ax = plt.subplots(nrows=1,ncols=1)

plt.step(m,p, where = 'mid')
ax.set_xlim(45,55)
ax.set_xticks(m)
plt.ylim(0,max(p)+0.1)
plt.show()



	

