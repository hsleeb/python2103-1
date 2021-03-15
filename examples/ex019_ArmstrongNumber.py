# A positive integer is called an Armstrong number of order n if
# abcd... = an + bn + cn + dn + ...

# Check Armstrong number (for 3 digits), ex : 407
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# ===================================
# # Check Armstrong number of n digits
# num = 1634
#
# # Changed num variable to string,
# # and calculated the length (number of digits)
# order = len(str(num))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** order
#    temp //= 10
#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")