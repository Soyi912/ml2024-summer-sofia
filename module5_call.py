from module5_mod import DataProcess

Data_Process = DataProcess()
N = Data_Process.type_number("Enter the number of numbers (N): ")

for i in range(N):
    number = Data_Process.type_number(f"Enter number {i + 1}: ")
    Data_Process.insert_number(number)

# Ask for the number X
X = Data_Process.type_number("Enter the number to find (X): ")
# Find if X in the list and return the index or -1
Data_Process.find_number(X)
