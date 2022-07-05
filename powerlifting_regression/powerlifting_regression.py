import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import scipy as sp
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import pylab as py
# used to read the origional file from kaggle
#useful_col = ['Sex', 'Equipment', 'Age', 'Division', 'BodyweightKg', 'WeightClassKg','BestSquatKg', 'BestBenchKg', 'BestDeadliftKg', 'TotalKg']
#df = pd.read_csv("openpowerlifting.csv", usecols = useful_col)
df = pd.read_csv("powerlifting_processed.csv")

# columns that include names will not be used in this analysis
# derived quantities like wilks are nice however are derived from quantities we are trying
# to predict

enc = OrdinalEncoder()
def clean(df):
	df[["Sex"]] = enc.fit_transform(df[["Sex"]])
	df = df.dropna()
	df["BestSquatKg"] = np.abs(df["BestSquatKg"])
	df["BestBenchKg"] = np.abs(df["BestBenchKg"])
	df["BestDeadliftKg"] = np.abs(df["BestDeadliftKg"])
	return df



df = clean(df)

mens_raw = df.loc[df["Sex"]==1].loc[df["Equipment"]=='Raw'].loc[df["Division"]=="Open"]
# subset of the data we will use for this investigation

sns.heatmap(mens_raw.corr())
plt.show()
df.head()

X_train, X_test, Y_train,Y_test = train_test_split(mens_raw[["BodyweightKg"]], mens_raw[["TotalKg"]])


lm = LinearRegression(fit_intercept = True)


# fit the data and look at the goodness of fit
lm.fit(X_train, Y_train)
lm.score(X_train, Y_train)
lm.score(X_test, Y_test)
lm.coef_
lm.intercept_


# plot of the data with best fit line
plt.scatter(X_train, Y_train)
plt.scatter(X_test, Y_test)
plt.plot(X_train.to_numpy(), lm.predict(X_train))
plt.show()

# residual analysis
res = lm.predict(mens_raw[["BodyweightKg"]])- mens_raw[["TotalKg"]]
res.hist(bins = 20) # could be normally distributed.  Hard to tell so we will use hypothesis testing to determine if the data is normally distributed
plt.show()

# if the data was drawn from a bi-variate normal distribution, then the residuals 
# from the linear regression should be normally distributed.
# The wilk Shapiro test is a hypothesis test with H_0: the data is normally distributed.
sp.stats.shapiro(res) 
# we find that the p value is small meaning the null hypothesis is excessively unlikely given this data
# reject null hypothesis.  Residuals are not normally distributed
# we can not proceed under the assumption that our data is normally distributed.




# to obtain more information from the data given to make a better prediction
# we need to find what the "division" attribute means
# unfortunately each power lifting federation calls their divisions
# different things and each federations divisions follow different rules.














