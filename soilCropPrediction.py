from sys import stdin,stdout

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram

trainingData = pd.read_csv('soilPredictionDataSets/DatasetWithCategory.csv')
testingData = pd.read_csv('soilPredictionDataSets/TestingDataSet.csv')

#print(trainingData)
trainfeature = trainingData.values[:,1:-1]
testfeature = testingData.values[:,1:]
#print(trainfeature)
#print(testfeature)
#print(np.concatenate((trainfeature,testfeature),axis=0))
traincat = trainingData.Category
#print(traincat)



global trainfeature,testfeature,traincat
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(trainfeature,traincat)
prediction = classifier.predict(testfeature)
 
 
pred_val = np.array([7.0,0.24,0.75,360,27,320,0.12,1.60,10.2,9.38,14.2]).reshape([1,11])

predictedValue = classifier.predict(pred_val);
print(predictedValue)
predictedString = ''

if predictedValue == 'SI':
    predictedString = 'slit'
elif predictedValue == 'LO':
    predictedString = 'loam'
else:
    predictedString = 'sandy'
    
typesOfSoil = ['SA','SI','LO']
typesOfSoil_zeros = []
for x in range(0,len(typesOfSoil)):
    typesOfSoil_zeros.append(0)
    

for x in range(0,len(typesOfSoil)):
    for z in typesOfSoil:
        if predictedValue==typesOfSoil[x]:
            typesOfSoil_zeros[x]=1


sdf = pd.read_csv('soilPredictionDataSets/soil.csv')
ydf = sdf.CROPS

from sklearn.tree import DecisionTreeClassifier
dclassifier = DecisionTreeClassifier(criterion='entropy')
dclassifier.fit(sdf,ydf)

print('The crops that are suitable for your field are: \n')
print(dclassifier.predict(typesOfSoil_zeros))
    

    



    


 




