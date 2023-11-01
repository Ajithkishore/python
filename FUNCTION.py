def count_factors(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def first_n_factors(number, N):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            if len(factors) == N:
                break
    return factors


given_number = int(input("Given number: "))
N = int(input("N: "))


num_factors = count_factors(given_number)


first_N_factors = first_n_factors(given_number, N)


print(f"Number of factors = {num_factors}")
print(f"1st {N} factors are: {', '.join(map(str, first_N_factors))}")
