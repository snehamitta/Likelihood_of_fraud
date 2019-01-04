# To predict likelihood of fraud

The data, FRAUD.csv, contains results of fraud investigations of 5,960 cases.  The binary variable FRAUD indicates the result of a fraud investigation: 1 = Fraudulent, 0 = Otherwise.  The other interval variables contain information about the cases.

1.	TOTAL_SPEND: Total amount of claims in dollars
2.	DOCTOR_VISITS: Number of visits to a doctor  
3.	NUM_CLAIMS: Number of claims made recently
4.	MEMBER_DURATION: Membership duration in number of months
5.	OPTOM_PRESC: Number of optical examinations
6.	NUM_MEMBERS: Number of members covered

The Nearest Neighbor algorithm will be used to predict the likelihood of fraud.

Also some Non Parametric Methods have been explored using the NormalSample Dataset. 