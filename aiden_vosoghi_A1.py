# aiden_vosoghi_A1.py     A1- A Simple Calculator     Author: Aiden Vosoghi

# Begin program with an intro message
import sys
print('\nStart of Calculator Program')

# Ask user for operation type as well as the two input numbers
op = input('\n\nEnter the Desired Operation (+,-,*,/,**): ')

# Determine if the operation is valid or invalid. If valid, begin calculating result.
if op == '+':
  a = int(input('\nEnter the first input number: '))
  b = int(input('\nEnter the second input number: '))
  ans = a + b

elif op == '-':
  a = int(input('\nEnter the first input number: '))
  b = int(input('\nEnter the second input number: '))
  ans = a - b

elif op == '*':
  a = int(input('\nEnter the first input number: '))
  b = int(input('\nEnter the second input number: '))
  ans = a * b

elif op == '/':
  a = int(input('\nEnter the first input number: '))
  b = int(input('\nEnter the second input number: '))
  ans = a / b

elif op == '**':
  a = int(input('\nEnter the first input number: '))
  b = int(input('\nEnter the second input number: '))
  ans = a ** b

# If invalid, display an error message which ends the program.
else:
  input('\nYou have entered an invalid operation! Please restart and try again.')
  sys.exit()

# Print the results as well as display the end of the program
# Provide user input to exit the program
print('\n\n',a,op,b,'=',ans)
print('\n\nEnd of Calculator Program')
input('\nHit "Enter" to End Program')
