import pandas
data = pandas.read_csv('/Users/snehamitta/Desktop/ML/Assignment1/Fraud(1).csv',
                       delimiter=',')

from sklearn.neighbors import NearestNeighbors as kNN
import numpy as np

kNNSpec = kNN(n_neighbors = 5, algorithm = 'brute', metric = 'euclidean')

trainData = data[['TOTAL_SPEND', 'DOCTOR_VISITS', 'NUM_CLAIMS', 'MEMBER_DURATION', 'OPTOM_PRESC', 'NUM_MEMBERS']]
print (trainData.shape)
# Build nearest neighbors
nbrs = kNNSpec.fit(trainData)
print(nbrs.shape)
distances, indices = nbrs.kneighbors(trainData)
print (distances)
print (indices)

target = data[['FRAUD']]
print(target.shape)

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5 , algorithm = 'brute', metric = 'euclidean')
nbrs = neigh.fit(trainData, target)

class_result = nbrs.predict(trainData)
print(class_result)

class_prob = nbrs.predict_proba(trainData)
print(class_prob)

accuracy = nbrs.score(trainData, target)
print (accuracy)

# Find the nearest neighbors of these focal observations       
focal = trainData[(trainData['TOTAL_SPEND'] == 7500)&(trainData['DOCTOR_VISITS'] == 15)&(trainData['NUM_CLAIMS'] == 3)&(trainData['MEMBER_DURATION'] == 127)&(trainData['OPTOM_PRESC'] == 2)&(trainData['NUM_MEMBERS'] == 2)]  

myNeighbors = nbrs.kneighbors(focal, return_distance = False)
print("My Neighbors = \n", myNeighbors)

print(data[587:588])
print(data[576:577])
print(data[581:582]) 
print(data[572:573])
print(data[574:575])