def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n
def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum
def perfect_squares_with_digit_sum_limit(start, end, limit):
    perfect_squares = []
    for number in range(start, end + 1):
        if is_perfect_square(number) and sum_of_digits(number) < limit:
            perfect_squares.append(number)
    return perfect_squares
start_range = 1
end_range = 40
digit_sum_limit = 10
result = perfect_squares_with_digit_sum_limit(start_range, end_range, digit_sum_limit)
print("Perfect squares with digit sum less than", digit_sum_limit, "in the range", start_range, "to", end_range, "are:", result)



