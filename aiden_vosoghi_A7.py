# Program Name: aiden_vosoghi_A7.py
# Assignment #7 - Online Order Shopping Cart Category Menu
# Author: Aiden Vosoghi

# The purpose of this program is to provide the user with options
# to buy products from an "online shopping" store. The user can
# add multiple items to their cart and find out their total before
# checking out.

import os, sys

# getAmount function asks user how many items they would like to
# purchase, which will be used for determining total cost for 'x'
# items.

def getAmount():
  amount = int(input('\nHow many items would you like to add to'
                     ' your cart: '))
  return amount

# calcTotal function uses amount entered by the user and multiplies
# it by the individual cost of that item.

def calcTotal (a, b):
  for i in b:
    b[i][0] += a
    total = a * i
    b[i][1] += total
  return total

# printCart function prints the results by displaying the cost of x items
# along with the cost for each individual item.

def printCart(x, y, z):
  for i in x:
    print('\nYou added',y,'items to your cart for a total of $',z,'($',i,'per item)')
  input("\nPress 'Enter' to return to the menu screen")

# printCheckout iterates through the item amount along with its corresponding
# total cost. If the user does not add a specific item to their cart, then
# the amount for that item is set to zero by default, in which case it
# does NOT appear in the checkout screen.

def printCheckout(m,n):
  for i in n:
      if n[i][0]:
        print('|',n[i][2],'\t|\t',m,'\t |     $',n[i][1])

# checkoutTotal function adds the total number of items and cost for each
# cart into a running total which is categorized by itemTotal and cartTotal,
# respectively. Afterwards, the total amount for both items and cost is
# displayed to the user after the printCheckout function.

def checkoutTotal(a, b, c):
  itemTotal = 0
  cartTotal = 0
  for i in a:
    itemTotal += a[i][0]
    cartTotal += a[i][1]
  for i in b:
    itemTotal += b[i][0]
    cartTotal += b[i][1]
  for i in c:
    itemTotal += c[i][0]
    cartTotal += c[i][1]

  print('----------------------------------------------------')
  print('| Total \t|\t',itemTotal,' \t |     $',cartTotal,'\n')
  return itemTotal, cartTotal

# resetItemAndPriceTotals function takes the values in all dictionaries
# which are responsible for # of items as well as total for those items
# and resets them back to zero. This function is only executed if the user
# wants to add another cart to their order.

def resetItemAndPriceTotals(x):
  for i in x:
    x[i][0] = 0
    x[i][1] = 0
  return x

# endProgramResults function is executed when the user decides they are
# finished with their order. The function's main purpose is to print out
# the final results of the program, which includes a running total of
# number of carts processed (numCarts), total number of items (finalItems),
# and the total amount of all items (finalTotal). Afterwards, the program
# prompts the user to hit 'Enter' to exit the program.

def endProgramResults(numCarts, finalItems, finalTotal):
  print('Total number of carts processed:',numCarts,
        '\nTotal number of item(s) purchased across',numCarts,'cart(s):',finalItems,
        '\nRunning total of',finalItems,'item(s) across',numCarts,'cart(s): $',finalTotal)
  input("\nPress 'Enter' to exit the program")
  sys.exit()

# The 'menu' variable is used to display the available items for purchase
# as well as a checkout option for when the user is finished shopping.

menu = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - Books ($6.25 ea)
                          2 - Electronics ($150.00 ea)
                          3 - Clothing ($31.25 ea)
                          c - Checkout

                   |-------------------------------------|
"""

# Define dictionaries for all items (books, electronics, clothing) as
# they will store information about the total costs, names, and so on.
# Also define variables for the amounts of each item, number of carts,
# and the running totals of items and their costs.

bookDetails = {6.25 : [0, 0.00,'Books']}
electronicDetails = {150.00 : [0, 0.00,'Electronics']}
clothingDetails = {31.25 : [0, 0.00,'Clothing']}

amountBooks = 0
amountElectronics = 0
amountClothing = 0
numCarts = 1
runningTotal = 0
allItems = 0

while True:

# The program begins by clearing the screen of any previous displays
# and prints the menu along with an option for user input (1 - 3 or 'c').

  os.system('cls')
  print(menu)
  option = input("Select one of the following categories"
                 " or checkout (1 - 3 or 'c'): ")

# if the user enters '1' as their option, then the appropriate code
# for 'bookDetails' is executed. If '2' is entered, 'electronicDetails'
# is executed. And finally if '3' is entered, 'clothingDetails' is
# executed.

  if option == '1':
    os.system('cls')
    amountBooks = getAmount()
    bookTotal = calcTotal(amountBooks, bookDetails)
    printCart(bookDetails, amountBooks, bookTotal)

  elif option == '2':
    os.system('cls')
    amountElectronics = getAmount()
    electronicTotal = calcTotal(amountElectronics, electronicDetails)
    printCart(electronicDetails, amountElectronics, electronicTotal)

  elif option == '3':
    os.system('cls')
    amountClothing = getAmount()
    clothingTotal = calcTotal(amountClothing, clothingDetails)
    printCart(clothingDetails, amountClothing, clothingTotal)


# If the user enters 'c' for checkout, then the following code will
# be executed. A print statement prints the title of the checkout screem
# and then displays # of items for each product the user ordered as well
# as the totals for each item, which is then added to the 'total' section
# which counts the running total for number of items and price per cart.

# Should the user want to add more carts to the order, they simply enter 'y'
# into the prompt and then the program starts from the beginning, clearing all
# previous values back to zero. Otherwise, the program prints the total number
# of carts processed, items purchased, and complete total for all items.

  elif option == 'c':
    os.system('cls')
    print('| Item Category |   # of Items   |  Cost of Items\n'
          '----------------------------------------------------')
    printCheckout(amountBooks,bookDetails)
    printCheckout(amountElectronics,electronicDetails)
    printCheckout(amountClothing,clothingDetails)
    totalItems,totalPrice = checkoutTotal(bookDetails,electronicDetails,clothingDetails)
    allItems += totalItems
    runningTotal += totalPrice
    choice = input("Enter 'Y' to add more shopping carts\nor any other key to"
                   " finalize your purchase: ")
    choice = choice.lower()

    if choice == 'y':
      os.system('cls')
      numCarts += 1
      resetItemAndPriceTotals(bookDetails)
      resetItemAndPriceTotals(electronicDetails)
      resetItemAndPriceTotals(clothingDetails)
      
    else:
      os.system('cls')
      endProgramResults(numCarts, allItems, runningTotal)

# If the user enters something else besides 1 - 3 or 'c', then the program
# will notify the user that the option entered was incorrect and that they
# must try again.

  else:
    input('\nInvalid option. Please try again.')
    continue
      
