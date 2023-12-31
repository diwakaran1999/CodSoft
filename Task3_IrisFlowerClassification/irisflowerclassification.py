# -*- coding: utf-8 -*-
"""IrisFlowerClassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HK0Gy522M4RTDAyA3Xwbs6QgNIDJ2wDd

Load Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/IRIS.csv')

df

df.head()

"""Visualization"""

sns.catplot(x = 'species', hue = 'species', kind = 'count', data = df)

#Bar plot for Species Vs Petal Width
plt.bar(df['species'],df['petal_width'])

#Paired Plot
sns.set()
sns.pairplot(df[['sepal_length','sepal_width','petal_length','petal_width','species']],  hue = "species", diag_kind="kde")

"""Data processing"""

df.describe()

df.columns

df.info()

df

#dropping the 'species' column
X = df.drop(['species'], axis=1)
X

df['species'],categories =pd.factorize(df['species'])
df.head()

"""Encoding the categorical feature as a one-hot numeric feature"""

Label_Encode = LabelEncoder()
Y = df['species']
Y = Label_Encode.fit_transform(Y)
Y

df['species'].nunique()

X = np.array(X)
X

Y

"""Spliting the dataset"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)

X_train

X_train.shape

X_test.shape

Y_test.shape

Y_train.shape

"""Model Preparation
K-Means
"""

df

color_map=np.array(['Red','green','blue'])
figure=plt.scatter(df['petal_length'],df['petal_width'],c=color_map[Y],s=30)

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3,random_state=0,)
y_predicted = km.fit_predict(df[['petal_length','petal_width']])
y_predicted

df['cluster']=y_predicted
df.head(150)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(df.species, df.cluster)
cm

true_labels = df.species
predicted_labels= df.cluster

cm = confusion_matrix(true_labels, predicted_labels)
class_labels = ['Setosa', 'versicolor', 'virginica']

# Plot confusion matrix
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(class_labels))
plt.xticks(tick_marks, class_labels)
plt.yticks(tick_marks, class_labels)

# Fill matrix with values
for i in range(len(class_labels)):
    for j in range(len(class_labels)):
        plt.text(j, i, str(cm[i][j]), ha='center', va='center', color='white')

plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()

X_train.size

Y_train.size

from sklearn import tree
D_tree = tree.DecisionTreeClassifier()
D_tree.fit(X_train,Y_train)

pred_tree=D_tree.predict(X_test)
accuracy=accuracy_score(Y_test,pred_tree)*100
accuracy