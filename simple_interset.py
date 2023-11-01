def calculate_simple_interest(principal, years, gender, senior_citizen):
    if senior_citizen == 'y':
        rate_of_interest = 0.15
    elif gender == 'f':
        rate_of_interest = 0.10
    else:
        rate_of_interest = 0.12
        
    interest = principal * rate_of_interest * years
    return interest


def main():
    principal = float(input("Enter the principal amount: "))
    years = int(input("Enter the number of years: "))
    gender = input("Gender (m/f): ").lower()
    senior_citizen = input("Is the customer a senior citizen (y/n): ").lower()

    interest = calculate_simple_interest(principal, years, gender, senior_citizen)
    print(f"Interest: {interest}")


if __name__ == "__main__":
    main()
