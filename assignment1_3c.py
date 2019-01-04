import numpy as np
import pandas as pd
from numpy import linalg as LA

data = pd.read_csv("~/Desktop/ML/Assignment 1/Fraud(1).csv")
df = data[['FRAUD', 'TOTAL_SPEND', 'DOCTOR_VISITS', 'NUM_CLAIMS', 'MEMBER_DURATION', 'OPTOM_PRESC', 'NUM_MEMBERS']]

print("The dimensions of the dataset are", df.ndim)

df.to_csv("~/Desktop/out.csv", sep = ',',header=None, index = False)
data_2 = pd.read_csv("~/Desktop/out.csv")

data_3 = np.matrix (data_2)
data_4 = np.matrix(data_2.transpose())
data_5 = data_4 * data_3

evals, evecs = LA.eigh(data_5)
print("Eigen values are", evals)

print("Eigen Vectors are", evecs)

transf = evecs * LA.inv(np.sqrt(np.diagflat(evals)));
print("Transformation Matrix = \n", transf)

transf_x = data_3 * transf;
print("The Transformed x = \n", transf_x)

xtx = transf_x.transpose() * transf_x;
print("Expect an Identity Matrix = \n", xtx)

