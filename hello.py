# This is my first Python programming assignment
# Author: Mark Demot
# Date: August 31st 2026
name = input("Please enter your name: ")
print("Hello,", name)
my_id = 7305209
print(f"My number is {my_id}")
print(f"My number with leading zeros if less than 8 digits is {my_id:08d}")
print(f"My number with 2 decimals is {my_id:.2f}")
print(f"My number as a binary number is {my_id:b}")
print(f"My number as a hexadecimal number is {my_id:x}")
first_digit = my_id // 1000000
last_digit = my_id % 10
print(f"The sum of the first and last digit of my number is {first_digit + last_digit}")
