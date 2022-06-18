import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("drug_classification.csv")
enc = OrdinalEncoder()
df.head()
df.columns
df[["Drug", "Sex", "BP", "Cholesterol"]]=enc.fit_transform(df[["Drug", "Sex", "BP", "Cholesterol"]])
scaler = StandardScaler()
df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']] = scaler.fit_transform(df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']])
X_train, X_test, Y_train,Y_test = train_test_split(df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']],df["Drug"], stratify = df["Drug"],test_size=  .2)\

lm = LogisticRegression()
svc = SVC() 
nnclf = MLPClassifier(solver = "lbfgs", max_iter = 500, hidden_layer_sizes = (), random_state = 10)
tree = DecisionTreeRegressor()

tree.fit(X_train, Y_train)
svc.fit(X_train, Y_train)
lm.fit(X_train, Y_train)
nnclf.fit(X_train,Y_train)

svc.score(X_train, Y_train)
svc.score(X_test,Y_test )
lm.score(X_train, Y_train)
lm.score(X_test,Y_test)
tree.score(X_train, Y_train)
tree.score(X_test, Y_test)
nnclf.score(X_train,Y_train)
nnclf.score(X_test,Y_test)

