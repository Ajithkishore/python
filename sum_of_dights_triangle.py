def sum_of_digits_in_triangle(triangle):
    total_sum = 0
    for row in triangle:
        for number in row:
            total_sum += int(number)
    return total_sum


triangle = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

result = sum_of_digits_in_triangle(triangle)
print(f"Sum of all digits in the triangle: {result}")
