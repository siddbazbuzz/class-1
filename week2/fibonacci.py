try:
    max_number = int(input("Enter the maximum number in the Fibonacci sequence: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()


fibonacci_sequence = [0, 1]


while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= max_number:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)


print("Fibonacci sequence up to", max_number, ":", fibonacci_sequence)