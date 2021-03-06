# -*- coding: utf-8 -*-
"""FINAL YEAR PROJECT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vFLEF9jyAzDO8-mNj4HsjxQ7TtdG1prT
"""

#Description: Predicitng CardioVascular Disease in a Person Using Machine Learning

#import libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
from matplotlib import rcParams
from matplotlib.cm import rainbow
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#load the dataset
from google.colab import files
uploaded = files.upload()

#store the dataset into a variable
df = pd.read_csv('heart.csv')

#printing the first 10 rows of dataset
df.head(10)

#get the no of rows and column of the dataset
df.shape

#empty/null value in each column
df.isna().sum()

#view statistics
df.describe()

#get a count of no. of individual suffering with a CardioVascular Disease or not.
df['target'].value_counts()

#visualise the chart
sns.countplot(df['target'])

#corelation of column
df.corr()

#visualise
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, fmt='.0%')

df.hist()

#it is always a good practise to check dataset is balanced or not
sns.set_style('whitegrid')
sns.countplot(x='target', data=df, palette='RdBu_r')

#here i will use get_dummies method to create dummy columns for such variables
dataset = pd.get_dummies(df, columns= ['sex','cp','fbs','restecg','exang','slope','ca','thal'])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
StandardScaler = StandardScaler()
columns_to_scale = ['age','trestbps','chol','thalach','oldpeak']
dataset[columns_to_scale]= StandardScaler.fit_transform(dataset[columns_to_scale])

dataset.head()

y= dataset['target']
x= dataset.drop(['target'], axis=1)

from sklearn.model_selection import cross_val_score
knn_scores =[]
for k in range (1,21):
  knn_classifier = KNeighborsClassifier(n_neighbors = k)
  score= cross_val_score(knn_classifier,x,y,cv=10)
  knn_scores.append(score.mean())

plt.plot([k for k in range(1,21)], knn_scores, color= 'blue')
for i in range(1,21):
  plt.text(i, knn_scores[i-1], (i, knn_scores[i-1]))
  plt.xticks([i for i in range(1,21)])
  plt.ylabel('Number of Neighbors (k)')
  plt.title('K Neighbors Classifier For Diffrent K Value')

from sklearn.ensemble import RandomForestClassifier

randomforest_classifier= RandomForestClassifier(n_estimators=10)

score.mean()

rf_scores = []
estimators = [10, 100, 200, 500, 1000]
for i in estimators:
    rf_classifier = RandomForestClassifier(n_estimators = i, random_state = 0)
    rf_classifier.fit(x,y)
    rf_scores.append(rf_classifier.score(x,y))

colors = rainbow(np.linspace(0, 1, len(estimators)))
plt.bar([i for i in range(len(estimators))], rf_scores, color = colors, width = 0.8)
for i in range(len(estimators)):
    plt.text(i, rf_scores[i], rf_scores[i])
plt.xticks(ticks = [i for i in range(len(estimators))], labels = [str(estimator) for estimator in estimators])
plt.xlabel('Number of estimators')
plt.ylabel('Scores')
plt.title('Random Forest Classifier scores for different number of estimators')

from sklearn.svm import SVC
svc_scores = []
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for i in range(len(kernels)):
    svc_classifier = SVC(kernel = kernels[i])
    svc_classifier.fit(x,y)
    svc_scores.append(svc_classifier.score(x, y))

colors = rainbow(np.linspace(0, 1, len(kernels)))
plt.bar(kernels, svc_scores, color = colors)
for i in range(len(kernels)):
    plt.text(i, svc_scores[i], svc_scores[i])
plt.xlabel('Kernels')
plt.ylabel('Scores')
plt.title('Support Vector Classifier scores for different kernels')



from sklearn.tree import DecisionTreeClassifier
desctree_scores = []
for i in range(1, len(x.columns) + 1):
    desctree_classifier = DecisionTreeClassifier(max_features = i, random_state = 0)
    desctree_classifier.fit(x,y)
    desctree_scores.append(desctree_classifier.score(x,y))

plt.plot([i for i in range(1, len(x.columns) + 1)], desctree_scores, color = 'green')
for i in range(1, len(x.columns) + 1):
    plt.text(i, desctree_scores[i-1], (i, desctree_scores[i-1]))
plt.xticks([i for i in range(1, len(x.columns) + 1)])
plt.xlabel('Max features')
plt.ylabel('Scores')
plt.title('Decision Tree Classifier scores for different number of maximum features')