import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import svm
from sklearn.model_selection import train_test_split


if(len(sys.argv) == 3):
    while(True):
        if(os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2])):
            dfData = pd.read_excel(sys.argv[1])
            dfTarget = pd.read_excel(sys.argv[2])
            data = np.array(dfData.as_matrix())
            target = np.squeeze(np.asarray(dfTarget.as_matrix()))
            X_train, X_test, y_train, y_test = train_test_split(data, target)

            cmd = input(">")
            if(cmd == "LinearRegression"):
                clf = LinearRegression()
                clf.fit(X_train, y_train)
                predicted = clf.predict(X_test)
                print(predicted)
            elif(cmd == "GradientBoostingRegressor"):
                print(cmd)
                clf = LinearRegression()
                clf.fit(X_train, y_train)
                predicted = clf.predict(X_test)
                print(predicted)
            elif(cmd == "SupportVectorMachine"):
                print(cmd)
                clf = svm.SVR()
                clf.fit(X_train, y_train)
                predicted = clf.predict(X_test)
                print(predicted)
            elif(cmd == "visualise"):
                plt.scatter(predicted, y_test)
                plt.plot([5, 50], [10, 40])

            elif(cmd == "help"):
                print(">LinearRegression")
                print(">GradientBoostingRegressor")
                print(">SupportVectorMachine")
                print(">visualise**unifinished**")
                print(">help")
                print(">quit")

            elif(cmd == "quit"): # read user input: "quit"
                sys.exit()
            else:
                print("failed usage")
        else:
            print("path doesn't exist")
            sys.exit()
else:
    print ("one argument require, provide data; both feature data and target data")


# def
