def sum_of_digits(number):
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))
    # If the sum is greater than 9, keep finding the sum of its digits until a single digit is obtained
    while digit_sum > 9:
        digit_sum = sum(int(digit) for digit in str(digit_sum))
    return digit_sum

# Read input
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

# Calculate the sum of digits
result = sum_of_digits(number)

# Output the result
print(f"Sum of {N} digit number: {result}")
