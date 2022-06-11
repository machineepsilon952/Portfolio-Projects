import pandas as pd

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

df = pd.read_csv("drug_classification.csv")

enc = OrdinalEncoder()
df[["Drug", "Sex", "BP", "Cholesterol"]]=enc.fit_transform(df[["Drug", "Sex", "BP", "Cholesterol"]])

scaler = StandardScaler()
df[["Age","Na_to_K"]] = scaler.fit_transform(df[["Age","Na_to_K"]])

X_train, X_test, Y_train,Y_test = train_test_split(df[ ["Sex", "BP", "Cholesterol","Na_to_K"]],df["Drug"], stratify = df[["Drug"]], random_state = 10)


lm = LogisticRegression()
svc = SVC() 
nnclf = MLPClassifier(solver = "lbfgs", max_iter = 200, hidden_layer_sizes = (), random_state = 10)

print("Support vector machine scores")
svc.fit(X_train, Y_train)
print("Accuracy at predicting the correct drug on training data is: ",round( 100*svc.score(X_train, Y_train),2),"%")
print("Accuracy at predicting the correct drug on the test data is: ",round( 100*svc.score(X_test, Y_test),2),"%")


print("Logistic Regression Scores")
lm.fit(X_train, Y_train)
print("Accuracy at predicting the correct drug on training data is: ",round( 100*lm.score(X_train, Y_train),2), "%")
lm.score(X_test,Y_test)
print("Accuracy at predicting the correct drug on the test data is: ",round( 100*lm.score(X_test, Y_test),2), "%")


print("MLPClassifer accuracy")
nnclf.fit(X_train, Y_train)
print("Accuracy at predicting the correct drug on training data is: ",round(100*nnclf.score(X_train,Y_train),2), "%")
print("Accuracy at predicting the correct drug on the test data is: ",round( 100*nnclf.score(X_test, Y_test),2), "%")



