import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder
os.chdir("/home/ethan/Datasets")
df = pd.read_csv("drug_classification.csv")
df.head()

plt.scatter(df["Age"], df["Na_to_K"], c =enc.fit_transform(df[["Drug"]]))
plt.show()
df["Drug"].loc[df["Na_to_K"]>20]
# Should be able to predict if DrugY is prescribed based solely on the sodium to potassium ratio.


enc = OrdinalEncoder()
df_encoded = df
df_encoded[["Sex","BP","Cholesterol", "Drug"]] = enc.fit_transform(df[["Sex","BP","Cholesterol", "Drug"]])

df.loc[df["Na_to_K"]<15].loc[df["Sex"]==0]
pd.plotting.scatter_matrix(df_encoded,c = df_encoded["Drug"])
plt.show()
df.head()
 #DrugY appears to be perscribed to patients with a high Na to K ratio and the drug
