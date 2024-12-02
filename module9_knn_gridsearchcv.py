import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class DataProcess:
    def __init__(self):
        # Empty the list
        self.points = np.empty((0, 2), dtype=float)

    def int_check(self, num):
        # Check if it is positive int
        while True:
            try:
                val = int(num)
                if val <= 0:  # if the input is negative
                    num = input("Input must be a positive integer, try again! Enter number: ")
                    continue
                break
            except ValueError:  # if the input is not integer
                num = input("Input must be a integer, try again! Enter number: ")
        n = val
        return n

    def realnumber_check(self, question):
        while True:
            try:
                return float(input(question))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def type_number(self, question):
        # Ask for the number and then run "int_check" to check if it is positive int
        n = input(question)
        return self.int_check(n)


Data_Process = DataProcess()
N = Data_Process.type_number("Enter the number of numbers (N): ")
print(f"N = {N}")
n_features = []
n_labels = []
for i in range(N):
    x = Data_Process.realnumber_check(f"Enter x value for Point #{i + 1}: ")
    y = Data_Process.type_number(f"Enter y value (class label) for Point #{i + 1}: ")
    n_features.append([x])
    n_labels.append(y)

n_features = np.array(n_features)
n_labels = np.array(n_labels)

M = Data_Process.type_number("Enter the number of numbers (M): ")
print(f"M = {M}")
m_features = []
m_labels = []
for i in range(M):
    x = Data_Process.realnumber_check(f"Enter x value for Point #{i + 1}: ")
    y = Data_Process.type_number(f"Enter y value (class label) for Point #{i + 1}: ")
    m_features.append([x])
    m_labels.append(y)

m_features = np.array(m_features)
m_labels = np.array(m_labels)

best_k = 1
best_accuracy = 0
max_k = min(N, 10)
for k in range(1, max_k + 1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(n_features, n_labels)
    predictions = knn.predict(m_features)
    accuracy = accuracy_score(m_labels, predictions)
    print(f"Accuracy for k={k}: {accuracy:.2f}")
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

print(f"The best k is {best_k} with a test accuracy of {best_accuracy:.2f}")
