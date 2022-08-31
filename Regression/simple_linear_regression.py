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

