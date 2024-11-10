import numpy as np


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
        # Check if it is positive int
        while True:
            try:
                return float(input(question))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def type_number(self, question):
        # Ask for the number and then run "int_check" to check if it is positive int
        n = input(question)
        return self.int_check(n)


class KNN:
    def __init__(self):
        self.points = np.empty((0, 2), dtype=float)

    def insert_point(self, x, y):
        new_point = np.array([x, y])
        self.points = np.vstack((self.points, new_point))

    def calculate_knn(self, x, k):
        # Calculate the X distances
        distances = np.abs(self.points[:, 0] - x)
        # Sort and pick first k points of them
        sort_distance = np.argsort(distances, kind='mergesort')[:k]
        # Calculate the average y-value of the k-nearest neighbors
        average_y = np.mean(self.points[sort_distance, 1])
        return average_y


Data_Process = DataProcess()
kNN = KNN()
N = Data_Process.type_number("Enter the number of numbers (N): ")
print(f"N = {N}")
k = Data_Process.type_number("Enter the k value: ")
print(f"k = {k}")
for i in range(N):
    x = Data_Process.realnumber_check(f"Enter x for Point #{i + 1}: ")
    y = Data_Process.realnumber_check(f"Enter y for Point #{i + 1}: ")
    kNN.insert_point(x, y)
for i in range(N):
    print(f"Point #{i+1} : [{kNN.points[i,0]}, {kNN.points[i,1]}]")
# Ask for the number X
X = Data_Process.realnumber_check("Enter the number X: ")
if k > N:
    print("Error: k cannot be greater than the number of points (N)")
else:
    result = kNN.calculate_knn(X, k)
    print(f"The predicted Y-value at X = {X} using {k}-NN regression is: {result}")
