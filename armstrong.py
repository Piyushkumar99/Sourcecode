def is_armstrong_number(num):
    # Convert the number to a string to iterate over digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    return sum_of_powers == num

number = 153  # Change this to check a different number
print(f"{number} is an Armstrong number: {is_armstrong_number(number)}")
