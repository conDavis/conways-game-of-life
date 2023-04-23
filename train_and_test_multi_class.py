import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm



MODE = "all_data"
# drop some data depending on the mode (used for testing)
df = pd.read_csv("tern_training_data.csv")
if MODE == "just_heuristics":
    df = df.iloc[:, 25:]
elif MODE == "just_pos":
    df = df.drop('ideal_neighbors_heuristic', axis=1)
    df = df.drop('max_neighbors_heuristic', axis=1)
    df = df.drop('min_neighbors_heuristic', axis=1)
print(df)

# Split the data into features (X) and target (y)
X = df.drop('life_span_class', axis=1)
y = df['life_span_class']

# print the number of rows that do have infinite life -- to understand how balanced the dataset is
num_infinite = len(list(filter(lambda is_infinite: is_infinite, y)))
print('num infinite', num_infinite)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# -------------------- KNN --------------------
knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X_train, y_train)

# testing the knn neighbors model
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print('KNN: ')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# finding the best k value

# k_values = [i for i in range (1,31)]
# scores = []
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


# ------------------ Naive Bayes ----------------------
prob_infinite = (num_infinite / len(y))
pos_weight = 1 / prob_infinite
neg_weight = 1 / (1 - prob_infinite)

naive_bayes = BernoulliNB()
naive_bayes.fit(X_train, y_train)

# testing the linear svc model
y_pred = naive_bayes.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print('NB: ')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)


# -------------------- Linear SVC --------------------
num_infinite = len(list(filter(lambda life_span: life_span == 2, y)))
print('num infinite', num_infinite)
num_medium = len(list(filter(lambda life_span: life_span == 1, y)))
num_short = len(list(filter(lambda life_span: life_span == 0, y)))

prob_2 = (num_infinite / len(y))
life_span_2_weight = 1 / prob_2
prob_1 = (num_infinite / len(y))
life_span_1_weight = 1 / prob_1
prob_0 = (num_infinite / len(y))
life_span_0_weight = 1 / prob_0


#class_weight = {0: life_span_0_weight, 1: life_span_1_weight, 2: life_span_2_weight}
linear_svc = svm.SVC(kernel='linear', C = 1.0) #class_weight=class_weight)
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