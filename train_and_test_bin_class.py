import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm



MODE = "just_heuristics"
# drop some data depending on the mode (used for testing)
df = pd.read_csv("bin_training_data.csv")
df.drop('min_neighbors_heuristic', axis=1)
if MODE == "just_heuristics":
    df = df.iloc[:, 25:]
elif MODE == "just_pos":
    df = df.drop('ideal_neighbors_heuristic', axis=1)
    df = df.drop('max_neighbors_heuristic', axis=1)
    df = df.drop('min_neighbors_heuristic', axis=1)
print(df)

# Split the data into features (X) and target (y)
X = df.drop('is_infinite', axis=1)
y = df['is_infinite']

# print the number of rows that do have infinite life -- to understand how balanced the dataset is
num_infinite = len(list(filter(lambda is_infinite: is_infinite, y)))
print('num infinite', num_infinite)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# -------------------- KNN --------------------
knn = KNeighborsClassifier(n_neighbors=17)
knn.fit(X_train, y_train)

# testing the knn neighbors model
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('KNN: ')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# finding the best k value

# k_values = [i for i in range (1,31)]
# scores = []
#
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
#
# for k in k_values:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     score = cross_val_score(knn, X, y, cv=5)
#     scores.append(np.mean(score))
#
# sns.lineplot(x = k_values, y = scores, marker = 'o')
# plt.xlabel("K Values")
# plt.ylabel("Accuracy Score")
# plt.show()

# -------------------- Linear SVC --------------------
prob_infinite = (num_infinite / len(y))
pos_weight = 1 / prob_infinite
neg_weight = 1 / (1 - prob_infinite)

class_weight = {True: pos_weight, False: neg_weight}
linear_svc = svm.SVC(kernel='linear', C = 1.0, class_weight=class_weight)
linear_svc.fit(X_train, y_train)

# testing the linear svc model
y_pred = linear_svc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("SVC:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# ------------------ Naive Bayes ----------------------
prob_infinite = (num_infinite / len(y))
pos_weight = 1 / prob_infinite
neg_weight = 1 / (1 - prob_infinite)

naive_bayes = BernoulliNB()
naive_bayes.fit(X_train, y_train)

# testing the linear svc model
y_pred = naive_bayes.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('NB: ')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)