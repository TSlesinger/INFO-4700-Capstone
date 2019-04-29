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
#converts to features for ML gives an overall idea of how much black is in the pic
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

	print('Please input the filepath of the spectogram.')
	filepath = input()

	#Finding Features of new Spectogram

	features = spek_to_feature(str(filepath))


	#Training the Algorithm
	df = pd.read_csv('SCORE.csv', header = None)
	

	
	#Finding and converting raw data
	Y = df.iloc[:799, 0].values.astype(str)
	X = df.iloc[:799, 1:].values.astype(float)
	scalar.fit(X)
	X = scalar.transform(X)

	#Finding and converting test data
	Y_test = df.iloc[800:, 0].values
	X_test = df.iloc[800:, 1:].values.astype(float)

	scalar.fit(X_test)
	X_test = scalar.transform(X_test)


	classifier = DecisionTreeClassifier(random_state = 123)

	classifier.fit(X,Y)

	#Outputing the prediction and probability
	output = str(classifier.predict([features]))
	proba = np.amax(classifier.predict_proba([features]))

	with open('output.txt', 'w') as f:
		print(output, file = f)
		print(proba, file = f)


if __name__ == '__main__':
	main()