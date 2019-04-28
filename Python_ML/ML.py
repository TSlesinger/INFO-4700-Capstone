#Imports
import pandas as pd
import numpy as np
from skimage.io import imread
import skimage
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
scalar = StandardScaler()

from sklearn.tree import DecisionTreeClassifier




#Function takes a filepath of an image
#converts to features for ML
def spek_to_feature(filepath):
	
	im = imread(filepath, as_gray = True)

    #Crop Picture to get rid of top section
    #50 pixels is the standard header
	im = im[49:]

    #Find Bounds of image (to give baseline)
	y_bound, x_bound = im.shape

    #Looping across the x-axis (predefined resolution)
	score = []
	temp = 0

	for ii in range(0, y_bound):
	    #If the sum of the pixels across the row is 
	    if sum(im[ii]) != 0:
	        temp += 1
	        score.append(temp)
	    #If the sum is 0 we give a bad score
	    elif sum(im[ii]) == 0:
	        temp -= 1
	        score.append(temp)

	return np.asarray(score)



def main():

	#filepath = input()

	#Finding Features of new Spectogram

	features = spek_to_feature(r'C:\Users\spitf_000\Desktop\spek_pictures\01 - Try it Out.mp3.png')


	#Training the Algorithm
	df = pd.read_csv('SCORE.csv', header = None)
	

	#Finding and converting raw data
	Y = df.iloc[:799, 0].values
	X = df.iloc[:799, 1:].values
	scalar.fit(X)
	X = scalar.transform(X)

	#Finding and converting test data
	Y_test = df.iloc[800:, 0].values
	X_test = df.iloc[800:, 1:].values

	scalar.fit(X_test)
	X_test = scalar.transform(X_test)

	#classifier = DecisionTreeClassifier(random_state = 123)

	#classifier.fit(X,Y)

	#print(classifier.predict(features.reshape(1,-1)))

if __name__ == '__main__':
	main()
