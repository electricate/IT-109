# Program Name: aiden_vosoghi_A8.py
# Assignment #8 - Online Order Shopping Cart Category (v 2.0)
# Author: Aiden Vosoghi

# The purpose of this program is to build upon the previous
# assignment (A7) and add sub-categories for Books, Electronics
# and Clothing. A newer and more neatly formatted checkout
# screen will also be printed for every time the user finishes
# processing a cart.

# Import the 'os' function, which is primarily used to clear the
# user's screen every time they make a selection. Define four menu
# screen variables: 'menu','menuBooks','menuElectronics', and
# 'menuClothing'. Each menu contains items within the category.

import os

menu = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - Books
                          2 - Electronics
                          3 - Clothing
                          c - Checkout

                   |-------------------------------------|
"""

menuBooks = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - Origin, $19.95
                          2 - Grant, $24.50
                          3 - Prairie Fires, $18.95
                          x - Return to Category Menu

                   |-------------------------------------|
"""

menuElectronics = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - HP Laptop, $429.50
                          2 - EyePhone 10, $790.00
                          3 - Bose 20 Speakers, $220.00
                          x - Return to Category Menu

                   |-------------------------------------|
"""

menuClothing = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - T-shirt, $9.50
                          2 - Shoes, $45.00
                          3 - Pants, $24.00
                          x - Return to Category Menu

                   |-------------------------------------|
"""

# Define the variables for determining the number of carts (numCarts),
# total # of items in each cart (cartItems), and the total cost for
# that cart (cartCost).

# The first 'while' loop defines an empty cart list, which is used to
# collect the items that the user inputs, along with its corresponding price.
# Three lists are also created: bookDetails, electronicDetails, and clothingDetails
# which contain the sub-category item names and their prices. A sentry variable 'more'
# is defined which tells the program whether or not the user wants to add more info.

numCarts = 0
cartItems = 0
cartCost = 0.0

while True:

  cart = []
  bookDetails = [['Origin',19.95],['Grant',24.50],['Prairie Files',18.95]]
  electronicDetails = [['HP Laptop',429.50],['EyePhone 10',790.00],['Bose 20 Speakers',220.00]] 
  clothingDetails = [['T-shirt',9.50],['Shoes',45.00],['Pants',24.00]]
  more = 'y'


# The program starts off by displaying the category screen (menu) to the user.
# The user can choose one of 4 options: 1, 2, 3, or 'c' for checkout. If a user
# tries to checkout with an empty cart, the program simply tells the user their
# cart is empty and returns them to the main menu

# Once the user has selected which category they want to buy from, the
# corresponsing sub-menu will be presented, showing the available products
# as well as their prices. Every time the user adds an item, its name and
# price are stored in the 'cart' list, which will be used later. Should the
# user want to return to the main menu, they must enter 'x'.

  while more == 'y':

    os.system('cls')
    print(menu)
    option = input("Select one of the following categories"
                   " or checkout (1 - 3 or 'c'): ")

    itemSelect = ' '
    if option == '1':
      itemSelect = ' '
      while itemSelect != 'x':
        os.system('cls')
        print(menuBooks)
        itemSelect = input('Select one of the options or press "x" to return\n'
                           ' to the main menu: ')
        if itemSelect in ('1','2','3'):
          cart.append(bookDetails[int(itemSelect) - 1])
        elif itemSelect != 'x':
          input('Invalid item selected. Press "Enter" and try again')

    elif option == '2':
      itemSelect = ' '
      while itemSelect != 'x':
        os.system('cls')
        print(menuElectronics)
        itemSelect = input('Select one of the options or press "x" to return\n'
                           ' to the main menu: ')
        if itemSelect in ('1','2','3'):
          cart.append(electronicDetails[int(itemSelect) - 1])
        elif itemSelect != 'x':
          input('Invalid item selected. Press "Enter" and try again')

    elif option == '3':
      itemSelect = ' '
      while itemSelect != 'x':
        os.system('cls')
        print(menuClothing)
        itemSelect = input('Select one of the options or press "x" to return\n'
                           ' to the main menu: ')
        if itemSelect in ('1','2','3'):
          cart.append(clothingDetails[int(itemSelect) - 1])
        elif itemSelect != 'x':
          input('Invalid item selected. Press "Enter" and try again')

    elif option == 'c':
      break
    elif option not in ('1','2','3'):
      input('Invalid category selected. Press "Enter" and try again')
      continue
  
# Once the user has entered at least one item into their cart and when they
# select 'c', they will be shown the total number of items they have selected
# as well as the cost for all those items combined. All of this information will
# be neatly formatted so that the user can esily read what items they have selected
# and how much they cost.

  if option == 'c':
    os.system('cls')
    print('\t\t\tCheckout Screen')
  if len(cart) > 0:
    totalCost = 0.0
    print('\n\t{0:20s}\t\t{1:8s}'.format('Item Purchased','Cost of Item'))
    print('\t{0:20s}\t\t{1:8s}'.format('--------------------','------------'))
    for i in cart:
      print('\t{0:20s}\t\t${1:8.2f}'.format(i[0],i[1]))
      totalCost += i[1]
    print('\nTotal # of items: {0:4d}    Cost: ${1:8.2f}'.format(len(cart), totalCost))
    numCarts += 1
    cartItems += len(cart)
    cartCost += totalCost
  else:
    print('There are no items in your cart :(')

# The user is prompted to see if they would like to add any additional carts
# for processing. If they select 'yes', then the program repeats. If they
# select 'no', then the program prints out the final receipt, which displays
# the total # of carts processed, the total # of items, and the total cost.

# Finally, the user is prompted to hit the 'Enter' key to end the program.
  
  more = input('Would you like to process another shopping cart (y/n): ')
  if more == 'y':
    continue
  else:
    break
os.system('cls')
print('\nTotal number of carts processed:',numCarts)
print('Total number of items purchased:', cartItems)
print('Total cost of items: $%8.2f' % (cartCost))
input("\nHit 'Enter' to exit the program")
