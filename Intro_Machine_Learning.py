# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:06:57 2018


MACHINE LEARNING INTRO
"""

# data
activities = ['soccer', 'swimming', 'rock climbing'] # what are we creating in this line?
students = [5, 3, 8]

# exploration
import pandas
student_activities = pandas.DataFrame({'activity': activities, 'number_students': students})
student_activities

# We use this special command at the top to tell Python we want to show a plot. 
%matplotlib inline 
import seaborn 
seaborn.barplot(x = 'activity', y = 'number_students', data = student_activities)




### titanic dataset
import pandas
import matplotlib.pyplot as plt
import seaborn
%matplotlib inline 


# (didn't run this part)
'''
import warnings
warnings.filterwarnings('ignore')
'''

data = pandas.read_csv("C:\\Work\\Git\\Repos\\Python-Library\\Data\\reduced_titanic.csv")
data.Survived


# Split the data into X_train, X_test, y_train, and y_test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
                                   data.drop('Survived', axis=1), 
                                   data['Survived'], 
                                   test_size=0.33, 
                                   random_state=42)
X_train.head()


# then train model...
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

decision_tree = DecisionTreeClassifier()

# training model with just two features
features = ['Gender', 'Age']
model = decision_tree.fit(X_train[features], y_train)


# How good is the model?
model.score(X_test[features], y_test)


# test. NOTE: UNLIKE ONLINE EXAMPLE, NEW PACKAGES NEED LIST OF LIST DATA INPUT
Gender = 0
Age = 18 # how much can you pay for the tickets?  

Result = decision_tree.predict([[Gender, Age]])

Survive_Prob = decision_tree.predict_proba([[Gender, Age]])[0,1]*100

if Result==1: 
    print('He/She has a {0:.2f}% chance of survival! :)'.format(Survive_Prob))
else: 
    print('He/She has a {0:.2f}% chance of survival :('.format(Survive_Prob))


# Exercise    
features = ['Gender', 'Age', 'Class', 'Fare'] # complete this list]
model = decision_tree.fit(X_train[features], y_train)
# How good is our model? Is it better or worse than the one with less features? Why?
model.score(X_test[features], y_test)  





''' Questions
machine learning w/ text (email example)
first level question: does each level have the most important feature (not already used)
split data part: declaring multiple variables there?
'''

''' Reference
https://hub.mybinder.org/user/jrigelo-intro_t-achine_learning-ok754sd8/notebooks/Intro_to_Machine_Learning.ipynb
feature = calc column 
linear or logistic regression recommendedd start
logistic = classifying
using a decision tree here
'''
