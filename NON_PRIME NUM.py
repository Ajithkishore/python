def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def non_prime_numbers_between_range(a, b):
    non_prime_numbers = []
    for num in range(a, b + 1):
        if not is_prime(num):
            non_prime_numbers.append(num)
    return non_prime_numbers


A = 12
B = 19


non_prime_numbers = non_prime_numbers_between_range(A, B)


print(", ".join(map(str, non_prime_numbers)))
