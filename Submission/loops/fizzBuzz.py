# FizzBuzz Program
for i in range(1, 101):  # Loop through numbers from 1 to 100
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Print "FizzBuzz" for multiples of both 3 and 5
    elif i % 3 == 0:
        print("Fizz")  # Print "Fizz" for multiples of 3
    elif i % 5 == 0:
        print("Buzz")  # Print "Buzz" for multiples of 5
    else:
        print(i)  # Print the number if it's not a multiple of 3 or 5
