import sys, os
from sklearn.utils import shuffle
import random as rand
from cross_validation import cross_validation
sys.path.append(os.path.realpath('..\data'))
from data import load_data

from CitationKNN import CitationKNN
from KNN import KNN


print('Started')

#Load Data 
bags, labels, _ = load_data('data_gauss')
# Bags: list of 2x2 matrices, each representing a bag
# labels: list of 1x1 matrices, each representing a label per bag

#Shuffle Data
bags, labels = shuffle(bags, labels, random_state=rand.randint(0, 100))

#Number of Folds 
folds=4

for k in range(2, 11):
    citationknn_classifier = CitationKNN() 
    parameters_citationknn = {'references': k, 'citers': k+2}
    knn_classifier = KNN();
    parameters_knn = {'k': k}
    accuracy_model1, accuracy_model2 = cross_validation(bags=bags,labels=labels, model_1=citationknn_classifier, model_2=knn_classifier, folds=folds, parameters_1=parameters_citationknn, parameters_2 = parameters_knn)
    print("k=" + str(k)+", references="+str(k)+", citers="+str(k+2))
    print('knn accuracy='+str(accuracy_model2)+", citation knn accuracy = "+str(accuracy_model1))
