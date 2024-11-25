import numpy as np
from sklearn.metrics import precision_score, recall_score


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

    def check1or0(self, question):
        # Check if the input is 0 or 1
        while True:
            try:
                val = int(input(question))
                if val in [0, 1]:
                    return val
                else:
                    print("Invalid input. Please enter 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

    def type_number(self, question):
        # Ask for the number and then run "int_check" to check if it is positive int
        n = input(question)
        return self.int_check(n)


Data_Process = DataProcess()
N = Data_Process.type_number("Enter the number of numbers (N): ")
print(f"N = {N}")
ground_truth = []
predicted_class = []

for i in range(N):
    x = Data_Process.check1or0(f"Enter the ground truth (X)  for Point #{i + 1}: ")
    y = Data_Process.check1or0(f"Enter the predicted class (Y) for Point #{i + 1}: ")
    ground_truth.append(x)
    predicted_class.append(y)

ground_truth = np.array(ground_truth)
predictions = np.array(predicted_class)

precision = precision_score(ground_truth, predictions)
recall = recall_score(ground_truth, predictions)

# Output
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
