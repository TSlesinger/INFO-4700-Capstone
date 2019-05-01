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

from sklearn.svm import SVC



#Function takes a filepath of an image
#converts to features for ML gives an overall idea of how much black is in the pic
def spek_to_feature(filepath):
	
	im = imread(filepath, as_gray = True)

	#Crop Picture to get rid of top section
	#50 pixels is the standard header
	im = im[58:]

	#Find Bounds of image (to give baseline)
	y_bound, x_bound = im.shape

	#Looping across the x-axis (predefined resolution)
	final_score = []

	for ii in range(0, x_bound-1):
	    #Reset Score per-coluimn
	    score = 0
	    for jj in range(0, y_bound-1): #Loop down each "x column"
	        try:
	            if im[ii, jj] == 0:
	                score -= 1
	            elif im[ii,jj] != 0:
	                score += 1
	        except:
	            'IndexError'

	    final_score.append(score)

	return np.asarray(final_score)



def main():

	print('Please input the filepath of the spectogram.')
	#filepath = input()

	#Finding Features of new Spectogram

	features = spek_to_feature(r'C:\Users\spitf_000\Desktop\spek_pictures\01 - Knife Party - Rage Valley (VIP).flac.png')


	#Training the Algorithm
	df = pd.read_csv('SCORE_v1.csv', header = None)
	
	#Finding and converting raw data
	Y = df.iloc[:, 0].values.astype(str)
	X = df.iloc[:, 1:].values.astype(float)
	scalar.fit(X)
	X = scalar.transform(X)

	#Finding and converting test data
	Y_test = df.iloc[800:, 0].values
	X_test = df.iloc[800:, 1:].values.astype(float)

	scalar.fit(X_test)
	X_test = scalar.transform(X_test)


	classifier = SVC(probability = True, random_state = 123)

	classifier.fit(X,Y)
	print('fitted')
	#Outputing the prediction and probability
	output = str(classifier.predict([features]))
	proba = np.amax(classifier.predict_proba([features]))

	with open('output.txt', 'w') as f:
		print(output, file = f)
		print(proba, file = f)


if __name__ == '__main__':
	main()