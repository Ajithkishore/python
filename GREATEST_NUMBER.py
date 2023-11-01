
binary1 = input("Enter first binary number: ")
binary2 = input("Enter second binary number: ")
binary3 = input("Enter third binary number: ")


decimal1 = int(binary1, 2)
decimal2 = int(binary2, 2)
decimal3 = int(binary3, 2)


maximum = max(decimal1, decimal2, decimal3)


print(f"The greatest binary number is: {bin(maximum)[2:]}")
