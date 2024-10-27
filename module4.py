def int_check(n):
    while True:
        try:
            val = int(n)
            if val < 0:     # if the input is negative
                n = input("Input must be a positive integer, try again! Enter number: ")
                continue
            break
        except ValueError:  # if the input is not integer
            n = input("Input must be a integer, try again! Enter number: ")

    n = val
    return n


N = int_check(input("Enter the number of numbers (N): "))

# Add the N numbers
numbers = []
for i in range(N):
    number = int_check(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Ask the user for the number X to find
X = int_check(input("Enter the number to find (X): "))

# check if X is among N. If yes, return the index of X
if X in numbers:
    print(numbers.index(X) + 1)
else:
    print("-1")
