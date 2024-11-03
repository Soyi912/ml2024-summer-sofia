class DataProcess:
    def __init__(self):
        # Empty the list
        self.numbers = []

    def int_check(self, num):
        # Check if it is positive int
        while True:
            try:
                val = int(num)
                if val < 0:  # if the input is negative
                    num = input("Input must be a positive integer, try again! Enter number: ")
                    continue
                break
            except ValueError:  # if the input is not integer
                num = input("Input must be a integer, try again! Enter number: ")
        n = val
        return n

    def type_number(self, question):
        # Ask for the number and then run "int_check" to check if it is positive int
        n = input(question)
        return self.int_check(n)

    def insert_number(self, num):
        # Insert a number into the list
        self.numbers.append(num)

    def find_number(self, x):
        # Searches for the number x in the list and return
        if x in self.numbers:
            print(self.numbers.index(x) + 1)
        else:
            print("-1")


Data_Process = DataProcess()
N = Data_Process.type_number("Enter the number of numbers (N): ")

for i in range(N):
    number = Data_Process.type_number(f"Enter number {i + 1}: ")
    Data_Process.insert_number(number)

# Ask for the number X
X = Data_Process.type_number("Enter the number to find (X): ")
# Find if X in the list and return the index or -1
Data_Process.find_number(X)
