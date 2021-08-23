# Program Name: aiden_vosoghi_A10.py
# Assignment #10 - Online Order Shopping Cart Category (v 4.0)
# Author: Aiden Vosoghi

# The purpose of this program is to build upon the previous
# assignment (A9) and add sub-categories for Books, Electronics
# and Clothing. A newer and more neatly formatted checkout
# screen will also be printed for every time the user finishes
# processing a cart.

# Import the 'os' and 'datetime' functions. The 'os' function will
# be used for clearing the user's screen every time they switch
# menus or go to checkout. The 'datetime' function will be used
# to gather the very moment that either another cart has been
# processed or the session is complete.

import os, datetime

# Define three distinct methods: itemMenu, displayCart, and
# validateSelection. 'itemMenu' will build a menu of the items
# using the corresponding tuple that is passed to it.

# 'displayCart' shows the user what items are currently in their cart,
# the price for each item, total number of items in the cart,
# and finally the total cost of that cart.

# The last method, 'validateSelection', is used to verify if the user
# wants to add a specific item to their cart. If they respond with 'y',
# the product is appended. If they enter 'n', they are returned to the
# category menu and prompted to select another item. If there is a
# duplicate entry within the shopping cart, the method simply increments
# the counter of the item instead of adding a whole new entry to the list.

def itemMenu(category, itemList):
    """itemMenu function - displays menu of variable number of shopping items.
       Inputs: category (books, etc.), list of item descriptions and prices.
       Returns: selected menu item (integer, 1 to n), d, or x
       ---------------------------------------------------------------------"""
    os.system('cls')
    print('\n\n\t\t ' + category + ' menu')
    print('\n\t\t Select from the following items, display cart, or checkout: ')
    print('\n\t\t\t {0:3s}  {1:26s}  {2:8s}'.format('No.', 'Item Description', 'Price '))
    print('\t\t\t {0:3s}  {1:26s} {2:8s}'
          .format('===', '===========================', '========'))
    for n in range(0, len(itemList)):
        print('\t\t\t {0:>2s} - {1:26s}  ${2:8.2f}'.format(str(n + 1), itemList[n][0], float(itemList[n][1])))
    print('\n\t\t\t {0:>2s} - {1:26s} '.format('d', 'display cart contents '))
    print('\t\t\t {0:>2s} - {1:26s} '.format('x', 'return to category menu '))
    menuPic = input('\n\nEnter Selection (1 to {0:>2s}, "d", or "x"): '.format(str(len(itemList))))
    return menuPic


def displayCart(shopCart):
    os.system('cls')
    if len(cart) > 0:
        print('\n\t{0:25s}\t{1:3s}\t{2:8s}'.format('Item Purchased','QTY','Cost of Item'))
        print('\t{0:25s}\t{1:3s}\t{2:8s}'.format('-------------------------','---', '------------'))
        for i in shopCart:
            displayItemsCost = 0.0
            displayItemsCost = int(i[2]) * float(i[1])
            print('\t{0:25s}\t{1:3s}\t${2:8.2f}'.format(i[0],str(i[2]),displayItemsCost))
        input('\nPress "Enter" to return to the menu')
    else:
        input('Your Shopping Cart is Empty :(\n'
              'Press "Enter" to return to the menu')


def validateSelection(item, category, shopCart):
    confirmSelect = ' '
    while confirmSelect != 'y' or confirmSelect != 'n':
        confirmSelect = input('\nAdd {} to your shopping cart (y/n)?  '
                              .format(category[int(itemSelect) - 1][0]))
        confirmSelect = confirmSelect.lower()
        if confirmSelect == 'y':
            found = False
            if len(shopCart) > 0:
                for i in shopCart:
                    if i[0] == category[int(itemSelect) - 1][0]:
                        found = True
                        i[2] += 1
                        break
            if not found:
                shopCart.append(category[int(itemSelect) - 1])
            return shopCart
        elif confirmSelect == 'n':
            break
        elif confirmSelect not in ('y', 'n'):
            input('Invalid option selected. Press "Enter" to try again')
            continue


menu = """
                           Welcome to Amazin.com!
                   |-------------------------------------|

                          1 - Books
                          2 - Electronics
                          3 - Clothing
                          d - Display Cart Contents
                          c - Checkout

                   |-------------------------------------|
"""

# Define the variables for determining the number of carts (numCarts),
# total # of items in each cart (cartItems), and the total cost for
# that cart (cartCost). There will also be a variable 'log' which keeps
# track of all transactions that have been completed.

# The first 'while' loop defines an empty cart list, which is used to
# collect the items that the user inputs, along with its corresponding price.
# Three lists are created: bookList, electronicList, and clothingList.
# These lists will get populated with data via reading from their corresponding
# text files on the user's machine. A sentry variable 'more' is defined which
# tells the program whether or not the user wants to add more info.

numCarts = 0
cartItems = 0
cartCost = 0.0
log = ''

while True:

    cart = []
    
    fileBooks = open('C:/Users/Aiden/Desktop/books.txt','r')
    bookFile = fileBooks.readlines()
    bookList = [ ]
    for b in bookFile:
        x = b[:-1].split(',')
        x.append(1)
        bookList.append([x[0], x[1].strip(),x[2]])
    fileBooks.close()

    fileElectronics = open('C:/Users/Aiden/Desktop/electronics.txt','r')
    electronicFile = fileElectronics.readlines()
    electronicList = [ ]
    for e in electronicFile:
        y = e[:-1].split(',')
        y.append(1)
        electronicList.append([y[0], y[1].strip(), y[2]])
    fileElectronics.close()

    fileClothing = open('C:/Users/Aiden/Desktop/clothing.txt','r')
    clothingFile = fileClothing.readlines()
    clothingList = [ ]
    for c in clothingFile:
        z = c[:-1].split(',')
        z.append(1)
        clothingList.append([z[0], z[1].strip(), z[2]])
    fileClothing.close()

    more = 'y'

# The program starts off by displaying the category screen (menu) to the user.
# The user can choose one of 5 options: 1, 2, 3, 'c' for checkout, or 'd' for
# displaying shopping cart contents. If a user tries to checkout or display
# their cart when it's empty, the program simply tells the user their
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
                itemSelect = itemMenu('Books', bookList)
                if itemSelect == 'd':
                    displayCart(cart)
                elif itemSelect.isdigit():
                    a = int(itemSelect)
                    if a in range(1, (len(bookList) + 1)):
                        validateSelection(a, bookList, cart)
                    else:
                        input('Invalid item selected. Press "Enter" to try again')
                        continue
                elif itemSelect != 'x':
                    input('Invalid item selected. Press "Enter" to try again')

        elif option == '2':
            itemSelect = ' '
            while itemSelect != 'x':
                os.system('cls')
                itemSelect = itemMenu('Electronics', electronicList)
                if itemSelect == 'd':
                    displayCart(cart)
                elif itemSelect.isdigit():
                    b = int(itemSelect)
                    if b in range(1, (len(electronicList) + 1)):
                        validateSelection(itemSelect, electronicList, cart)
                    else:
                        input('Invalid item selected. Press "Enter" to try again')
                        continue
                elif itemSelect != 'x':
                    input('Invalid item selected. Press "Enter" to try again')

        elif option == '3':
            itemSelect = ' '
            while itemSelect != 'x':
                os.system('cls')
                itemSelect = itemMenu('Clothing', clothingList)
                if itemSelect == 'd':
                    displayCart(cart)
                elif itemSelect.isdigit():
                    c = int(itemSelect)
                    if c in range(1, (len(clothingList) + 1)):
                        validateSelection(itemSelect, clothingList, cart)
                    else:
                        input('Invalid item selected. Press "Enter" to try again')
                        continue
                elif itemSelect != 'x':
                    input('Invalid item selected. Press "Enter" to try again')

        elif option == 'd':
            displayCart(cart)

        elif option == 'c':
            break
        elif option not in ('1', '2', '3'):
            input('Invalid category selected. Press "Enter" to try again')
            continue

# Once the user has entered at least one item into their cart and when they
# select 'c', they will be shown the items they have purchased, the quantity
# of each item, and the overall cost for that item. All of this information will
# be neatly formatted so that the user can esily read what items they have selected.

    if option == 'c':
        os.system('cls')
        print('\t\t\tCheckout Screen')
    if len(cart) > 0:
        totalCost = 0.0
        totalItems = 0
        print('\n\t{0:25s}\t{1:3s}\t{2:8s}'.format('Item Purchased','QTY','Cost of Item'))
        print('\t{0:25s}\t{1:3s}\t{2:8s}'.format('-------------------------','---', '------------'))
        for i in cart:
            print('\t{0:25s}\t{1:3s}\t${2:8.2f}'.format(i[0], str(i[2]),(i[2]*float(i[1]))))
            totalCost += (i[2] * float(i[1]))
            totalItems += i[2]
        print('\n\tTotal # of items: {0:4d}    Cost: ${1:8.2f}\n'.format(totalItems, totalCost))
        numCarts += 1
        cartItems += totalItems
        cartCost += totalCost
        x = datetime.datetime.now().__str__()
        log += ('\n{0:3s}     Cart                {1:8s}        {2:8s}   {3:8.2f}'
                .format(x,str(numCarts),str(totalItems),totalCost))
    else:
        print('There are no items in your cart :(')

# The user is prompted to see if they would like to add any additional carts
# for processing. If they select 'yes', then the program repeats. If they
# select 'no', then the program prints a 'dump file' which displays the
# end of session summaries from ALL previous transactions completed. The
# new session is appended to the file. Finally, the user is prompted to hit
# the 'Enter' key to end the program.

    more = input('Would you like to process another shopping cart (y/n): ')
    if more == 'y':
        continue
    else:
        break
os.system('cls')
print('{0:25s}\t{1:10s}\t{2:8s}\t{3:8s}\t{4:10s}'
      .format('Date/Time','Type','Cart #','Items','Cost'))
print('{0:25s}\t{1:10s}\t{2:8s}\t{3:8s}\t{4:6s}'
      .format('-------------------------','----------','--------','--------','--------'))
x = datetime.datetime.now().__str__()
log += ('\n{0:3s}     Session Summary     {1:8s}        {2:8s}   {3:8.2f}\n'
        .format(x,str(numCarts),str(cartItems),cartCost))
appendTransactions = open('C:/Users/Aiden/Desktop/IT109A10Log.txt','a')
appendTransactions.write(log)
appendTransactions.close()
readTransactions = open('C:/Users/Aiden/Desktop/IT109A10Log.txt','r')
readLog = readTransactions.read()
readTransactions.close()
print(readLog)
input("\nHit 'Enter' to exit the program")
