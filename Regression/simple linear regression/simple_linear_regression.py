from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
dataframe = pd.read_csv(r"C:\Users\mateus chou\Desktop\nova_pasta\Machine learning\Regression\Salary_Data.csv")
x = dataframe.iloc[:,:-1].values  # just the first column
y = dataframe.iloc[:,-1].values # list with elements of the last column

#split the dataset training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

#training the simple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#predicting test set
y_pred = regressor.predict(x_test)

#predict the salary of employee with 10 years of experience
print("salary of employee with 10 years of experience", regressor.predict([[10]])[0])

#print the values of coefficients a = b0 + xb1
print("b0 =", regressor.intercept_)
print("b1 =", regressor.coef_[0])

#visualize training set results
#scatter for spots and plot for line
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title("Train set")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

#visualize test set result
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_test, y_pred, color = 'blue')
plt.title("Test set")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

