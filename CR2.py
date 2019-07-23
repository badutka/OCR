import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets, neighbors, linear_model, metrics


digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

n_samples = len(X_digits)

X_train = X_digits[:int(0.9 * n_samples)]
y_train = y_digits[:int(0.9 * n_samples)]
X_test = X_digits[int(0.9 * n_samples):]
y_test = y_digits[int(0.9 * n_samples):]

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression(solver='newton-cg', multi_class='multinomial')

print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
print('LogisticRegression score: %f'
      % logistic.fit(X_train, y_train).score(X_test, y_test))
predictions = logistic.predict(X_test)
cm = metrics.confusion_matrix(y_test, predictions)
print(cm)
score = logistic.score(X_test, y_test)
print(score)

plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 15)
plt.show()

