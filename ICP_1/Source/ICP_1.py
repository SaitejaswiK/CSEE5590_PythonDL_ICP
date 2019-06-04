
#  Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex
str = input('Enter the string:')

res = str.find('Python')

print(str.replace("python","Pythons"))

# Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it.
s = input('Enter the string:')
num = int(input('Enter number of characters to delete:'))

res = s[0:-num]
print(res[::-1])

# Take two numbers from user and perform arithmetic operations on them.
num1 = input('Enter first number:')
num2 = input('Enter second number:')

a = int(num1)
b = int(num2)


print('Addition:',a + b)
print('Subtraction:',a-b)
print('Multiplicaation:',a * b)
print('Division:',a / b)
print('Modulus:',a % b)
print('Exponent:',a ** b)
print('Floor division:',a // b)
