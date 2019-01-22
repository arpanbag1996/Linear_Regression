#Arpan Bag

#Helper file that contains all the required user defined functions for Linear Regression



## Initialization
import numpy as np



#=================== Feature Normalization =========================

#FEATURENORMALIZE Normalizes the features in X 
#   FEATURENORMALIZE(X) returns a normalized version of X where
#   the mean value of each feature is 0 and the standard deviation
#   is 1. This is often a good preprocessing step to do when
#   working with learning algorithms.

def featureNormalize(X):
	X_norm = X
	mu = np.zeros((1, X.shape[1]))
	sigma = np.zeros((1, X.shape[1]))
	
	# =================================CODE HERE ======================
	#Instructions: First, for each feature dimension, compute the mean
    #           of the feature and subtract it from the dataset,
    #           storing the mean value in mu. Next, compute the 
    #           standard deviation of each feature and divide
    #           each feature by it's standard deviation, storing
    #           the standard deviation in sigma. 
	#
    #           Note that X is a matrix where each column is a 
    #           feature and each row is an example. You need 
    #           to perform the normalization separately for 
    #           each feature. 
	
	mu = np.mean(X,axis=0)
	sigma = np.std(X,ddof=1,axis=0)
	X_norm = (X_norm - mu)/sigma
	
	return X_norm, mu, sigma
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
       
