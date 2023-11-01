
def is_harshad_number(number):
    
    digit_sum = sum(int(digit) for digit in str(number))
    
    return number % digit_sum == 0


number = int(input("Enter number: "))


if is_harshad_number(number):
    print("Given number
