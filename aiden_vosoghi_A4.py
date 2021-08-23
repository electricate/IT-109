# Program File Name: aiden_vosoghi_A4.py
# A4: Oscar Movie List Display
# Author: Aiden Vosoghi

# Import the 'sys' function which will be used at a later time. Define the
# movies list by first including the year, followed by the title of the film
# and its corresponding category. Also define a menu variable which will
# display to the user their available options.

import sys
categories = ('drama','musical','comedy','historical','action',
              'western','fantasy')
              
movies = [[1939,'Gone With the Wind','drama'],
          [1943,'Casablanca','drama'],
          [1965,'The Sound of Music','musical'],
          [1969,'Midnight Cowboy','drama'],
          [1972,'The Godfather','drama'],
          [1973,'The Sting','comedy'],
          [1977,'Annie Hall','comedy'],
          [1982,'Gandhi','historical'],
          [1986,'Platoon','action'],
          [1990,'Dances with Wolves','western'],
          [1992,'Unforgiven','western'],
          [1994,'Forrest Gump','comedy'],
          [1995,'Braveheart','historical'],
          [1997,'Titanic','historical'],
          [1998,'Shakespeare in Love','comedy'],
          [2000,'Gladiator','action'],
          [2001,'A Beautiful Mind','historical'],
          [2002,'Chicago','musical'],
          [2009,'The Hurt Locker','action'],
          [2010,'The Kings Speech','historical'],
          [2011,'The Artist','comedy'],
          [2012,'Argo','historical'],
          [2013,'12 Years a Slave','drama'],
          [2014,'Birdman','comedy'],
          [2016,'Moonlight','drama'],
          [2017,'The Shape of Water','fantasy']] 

menu = """
        ----------------------------------------------------------------
            1 - display winning movie by year
            2 - display movie and category by year
            p - print entire movie list – year, title, category
            pc – print movies in a selected category – year and title
            q - quit
        ----------------------------------------------------------------
"""

# Start main program with a while loop which continuously prompts the user to
# enter an option as long as they don't press 'q', which force quits the program.

while True:

# Print the menu which was defined above as well as provide user input for what
# they would like to enter.

    print(menu)
    option = str(input('Select one of the menu options above: '))

# Each 'if' statement corresponds to the input the user inputs and for each input,
# a different set of instructions follows. If the user input is '1', then ask
# the user to enter a year. If the year is valid, return the winning movie for
# said year. If not valid, print an error statement and restart.

    if option == '1':
        found1 = False
        year = int(input('\nEnter the year of the movie: '))
        if year < 1927 or year > 2020:
            print('\nYear entered is out of range!'
                  ' Please enter a valid year between 1927 and 2020.')
            continue
        for y in movies:
            if year == y[0]:
                print('\nThe winning movie for the year',year,'was',y[1])
                found1 = True
                break
        if not found1:
            print('\nYear not found. Please restart and try again. ')
            continue

    elif option == '2':
        found2 = False
        year = int(input('\nEnter the year of the movie: '))
        if year < 1927 or year > 2020:
            print('\nYear entered is out of range!'
                  ' Please enter a valid year between 1927 and 2020.')
            continue
        for y in movies:
            found2 = False
            if year == y[0]:
                print('\nThe winning movie for the year',year,'was',y[1],'.\nThe'
                      ' category of the film is',y[2])
                found2 = True
                break
        if not found2:
            print('\nYear not found. Please restart and try again. ')
            continue

    elif option == 'p':
        print('\n| Year | Winning Film For That Year | Film Category |\n--------------------'
              '---------------------------------')
        for item in movies:
            print('|',item[0],'|',item[1],' '*(25-len(item[1])),
                  '|',item[2],' '*(12-len(item[2])),'|')

    elif option == 'pc':
        found3 = False
        genre = input('Enter a movie category: ')
        print('\n| Year | Winning Film of the Category | ')
        if genre not in categories:
            print('Invalid category entered. Please try again.')
            continue
        else:
            for m in movies:
                if genre == m[2]:
                    print('|',m[0],'|',m[1])
    elif option == 'q':
        sys.exit()

    else:
        input('\nInvalid option entered. Please try again.')
        continue
