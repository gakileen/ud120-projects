#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
target_all, features_all = targetFeatureSplit( data )

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(features_all, target_all)
predictions = reg.predict(features_all)

from outlier_cleaner import biggestOutlier
cleaned_data = biggestOutlier( predictions, features_all, target_all )

for k, v in data_dict.items():
	if v[features[1]] == cleaned_data[0][0] and v[features[0]] == cleaned_data[1]:
		print k