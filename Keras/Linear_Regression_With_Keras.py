##Arpan Bag
##Linear Regression

## Initialization
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import os

from Linear_Regression_Helper_Keras import *


np.set_printoptions(formatter={'float_kind':'{:f}'.format})	#Display numbers normally, not using exponent.






print("*****Linear Regression*******\n\n\n")
input("Press enter to select the Input data file.\n")



## Load Data


print('Loading data ...\n')
data = np.loadtxt(os.path.dirname(os.path.realpath(__file__)) + "\\" +"Sample_Data.txt",delimiter=",") #The file containing the training data. The Last column is the output (Y) and the rest of the columns are input (X) 

X = data[:,:-1] #Inputs
Y = data[:,-1].reshape(-1, 1)	 #Outputs
m = len(Y);		 #Number of training examples
num_features = X.shape[1]	 #No of features, which is the dimension of X
#Print out some data points
print('\nData loaded.\nFirst 10 examples from the dataset: \n')
print(np.column_stack((X,Y))[0:10,:])
input('\nPress enter to start Feature Standardization.\n')







## ================ Part 1: Feature Standardization ================


#Scale features and set them to zero mean
print('\nStandardizing Features ...\n') 
scaler = preprocessing.StandardScaler().fit(X) #Returned X = Feature standardized training inputs, X = (X-mu)/sigma, where mu = mean of X, sigma = standard deviation of X
mu = scaler.mean_	#mean
sigma = scaler.scale_	#standard deviation
X = scaler.transform(X)

#No need to add x0 intercept term to X (As x0 = 1 for all the examples), as keras automatically adds a bias



## ================ Part 2: Gradient Descent ================


#Input alpha and number of iteration values

alpha = input("Enter learning rate \nOr \npress Enter to use default (0.01): ")
if (alpha == ''):
	alpha = 0.01		#Default Learning rate
else:
	alpha = float(alpha)
print('\nLearning rate: %s\n' %alpha)

num_iters = input("\nEnter number of iterations \nOr \npress Enter to use default (500): ")
if (num_iters == ''):
	num_iters = 500	#Default Number if iterations
else:
	num_iters = int(num_iters)
print('\nNumber of iterations: %s\n' %num_iters)



print('\nRunning gradient descent ...\n')

#Run Gradient Descent
[model, weights, bias, J_history] = gradientDescent(X, Y, alpha, num_iters)

print('\nGradient Descent complete. Press enter to display results.\n')
input()

#Plot the convergence graph
plt.figure()
plt.plot(np.arange(len(J_history)), J_history)
plt.xlabel("Number of iterations")
plt.ylabel("Cost J")
plt.show(block=False)

#Display gradient descent's result
print('\nWeights computed from gradient descent: \n')
print(weights)
print('\n\nBias computed from gradient descent: \n')
print(bias)
print('\n')






##======================== Prediction ===========================

# ======================== CODE HERE =========================
# Recall that the first column of X is all-ones. Thus, it does
# not need to be standardized.

print('\nModel training complete. Press enter to start Prediction.\n')
input()
pred_x = np.zeros((1,num_features))

for i in range(num_features):
    pred_x[:,i]=input("Enter feature No. "+str(i+1)+": ")
	
pred_x = (pred_x-mu)/sigma		#Standardization

pred_y = predict(model,pred_x)	#Predict using helper function

#============================================================

print('\nPredicted output: \n'+ str(float(pred_y)))

print('\n\n\nProgram paused. Press enter to Exit.\n')
input()
























