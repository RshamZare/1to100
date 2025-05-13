# 6. FizzBuzz
# For numbers from 1 to 50:
# Print “Fizz” for multiples of 3,
# “Buzz” for multiples of 5,
# “FizzBuzz” for both.


for i in range(1,51):
    if i % 3 == 0:
        print("FIZZ")
    if i % 5 == 0:
        print("BUZZ")
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZ BUZZ")