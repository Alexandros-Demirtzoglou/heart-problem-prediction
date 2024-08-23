import os
import pandas as pd
import random
random.seed(1)

# Load the CSV file
year = '2015'
data = pd.read_csv('/kaggle/input/behavioral-risk-factor-surveillance-system/{year}.csv')

# Display the first five rows of the DataFrame
print(data.head())

# Split the data into Features and Labels
X = data.drop('HeartDiseaseorAttack', axis=1)  # Features
y = data['HeartDiseaseorAttack']  # Labels

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

# Create the model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score

# Predict classes for the test data
y_pred = model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy: {:.2f}%".format(accuracy * 100))