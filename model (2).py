# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import pickle

data = pd.read_csv(r"ML PROJECT DATA SET 4.csv")
print(data.head())
obj = (data.dtypes == 'object')
object_cols = list(obj[obj].index)
print("Categorical variables:", len(object_cols))

int_ = (data.dtypes == 'int')
num_cols = list(int_[int_].index)
print("Integer variables:", len(num_cols))

fl = (data.dtypes == 'float')
fl_cols = list(fl[fl].index)
print("Float variables:", len(fl_cols))

sns.countplot(x='TYPE', data=data)

#We can also use the bar plot for analyzing Type and amount column simultaneously.

sns.barplot(x='TYPE', y='amount', data=data)

# Both the graph  type cash_out and transfer are maximum in count and as well as in amount.
#check the distribution of data among both the prediction values.

data['isFraud'].value_counts()

#check the distribution of data among both the prediction values.

sns.countplot(x='isFraud', data=data)

#Data Preprocessing

from sklearn.preprocessing import LabelEncoder

#1.Encoding of Type column

type_new = pd.get_dummies(data['TYPE'], drop_first=True)
data_new = pd.concat([data, type_new], axis=1)
data_new.head()

#2.Dropping irrelevant columns like nameOrig, nameDest

X = data_new.drop([ 'TYPE', 'nameOrig', 'nameDest', 'VALUE DATE'], axis=1)
Y = data_new['isFraud']

X
print(X.head())

Y

#check the shape of extracted data

X.shape, Y.shape

#split the data into 2 parts : Training and Testing.

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
	X, Y, test_size=0.3, random_state=42)

#model Training

#As the prediction is a classification problem so the models we will be using are :

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

model.fit(X_train,y_train) # training Model

pred=model.predict(X_test)
print(pred)

from sklearn.metrics import (accuracy_score,confusion_matrix)

accuracy_score(y_test,pred)

confusion_matrix(y_test,pred)

pickle.dump(pred,open("model.pkl",'wb'))