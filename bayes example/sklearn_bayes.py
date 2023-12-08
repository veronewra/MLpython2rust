import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, matthews_corrcoef
from sklearn.datasets import load_wine

# Load the wine dataset
data = load_wine()
X = data.data
y = (data.target > 6).astype(int)  # Convert targets to binary data

# Split the dataset into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.1, random_state=42)

# Train the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict the validation dataset
y_pred = model.predict(X_valid)

# Construct confusion matrix
cm = confusion_matrix(y_valid, y_pred)

# Print confusion matrix
print("Confusion Matrix:")
print(cm)

# Calculate and print accuracy and Matthews correlation coefficient
accuracy = accuracy_score(y_valid, y_pred)
mcc = matthews_corrcoef(y_valid, y_pred)

print(f"Accuracy: {accuracy:.7f}, MCC: {mcc:.7f}")