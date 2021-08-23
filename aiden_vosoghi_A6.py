# Program File Name: aiden_vosoghi_A6.py
# A6: Oscar Movie List Using a Dictionary
# Author: Aiden Vosoghi

# Define functions for modifying an existing movie entry (modMovie), adding a
# new entry to the dictionary (addMovie), and checking to see if the entered year
# is within a certain range (validateYear).

# The addMovie function is incorporated into options 1, 2, and 3. This
# function appends a new year/title/category to the movies dictionary. Similar
# to the modMovie function, addMovie checks to see if a title length limit is
# reached and if the category entered by the user is within the 'categories'
# tuple. At the end, the new entry is added into the dictionary.

def addMovie(years,category):
    add = input('\nYear not found. Would you like to add a new entry (Y/N): ')
    add = add.upper()
    while True:
        if add == 'Y':
            title = input('Enter the name of the film: ')
            if len(title) > 40:
                print('Length of movie title exceeded 40 character'
                      ' limit. Please enter a shorter name.')
                continue
            cat = input('\nEnter the category of the film:\n(drama, musical, comedy,'
                        ' historical, action, western, fantasy, scifi): ')
            if cat not in categories:
                print('Category not recognized. Please enter again.')
                continue
            else:
                movies.update({year:[title, cat]})
                break
        else:
            break

# modMovie is defined to update the movie title and category for the entered
# year and replace it with user input. If the title of the film exceeds the
# 40 character limit, ask the user to enter again. If the category entered
# by the user is not in the 'categories' tuple, an error message is displayed
# and the user has to enter again. When done, print the gathered info into
# the dictionary.

def modMovie(years,categories):
    del movies[years]
    while True:
        title = input('\nEnter the title of the movie: ')
        if len(title) > 40:
            print('\nLength of movie title exceeded 40 character'
                  ' limit. Please enter a shorter name.')
            continue
        else:
            cat = input('\nEnter the category of the film:\n\n(drama, musical, comedy,'
                        ' historical, action, western, fantasy, scifi): ')
            if cat not in categories:
                print('\nCategory not recognized. Please enter again.\n')
                continue
            else:
                break
            break
    movies.update({year:[title, cat]})

# Function validateYear checks to see if the year entered by the user is within
# a certain range. In this case, the earliest year that can be entered is 1927
# and the lastest year being 2020. If the year is out of range, the user is
# prompted to re-enter a year until it is within range. Once the year has been
# validated, the loop ends and the resulting year is returned back to main.

def validateYear(year):
    while True:
        if year < 1927 or year > 2020:
                year = int(input('\nYear entered is out of range!\n'
                        'Please enter a valid year between 1927 and 2020: '))
                continue
        else:
            break
    return year

def clear():
    os.system('cls')

def mainMenu():
    input('\nPress any key to return to the main menu')


# Import the 'sys' function which will be used at a later time. Define the
# movies dictionary by first creating an empty dictionary set, followed by
# code that defines the key (year) and corresponding values (title, category).
# Also, define a menu variable which will display the available options to
# the user.

import sys, os
categories = ('drama','musical','comedy','historical','action',
              'western','fantasy','scifi')
movies = {}
movies = {1939:['Gone With the Wind','drama'],
          1943:['Casablanca','drama'],
          1965:['The Sound of Music','musical'],
          1969:['Midnight Cowboy','drama'],
          1972:['The Godfather','drama'],
          1973:['The Sting','comedy'],
          1977:['Annie Hall','comedy'],
          1982:['Gandhi','historical'],
          1986:['Platoon','action'],
          1990:['Dances with Wolves','western'],
          1992:['Unforgiven','western'],
          1994:['Forrest Gump','comedy'],
          1995:['Braveheart','historical'],
          1997:['Titanic','historical'],
          1998:['Shakespeare in Love','comedy'],
          2000:['Gladiator','action'],
          2001:['A Beautiful Mind','historical'],
          2002:['Chicago','musical'],
          2009:['The Hurt Locker','action'],
          2010:['The Kings Speech','historical'],
          2011:['The Artist','comedy'],
          2012:['Argo','historical'],
          2013:['12 Years a Slave','drama'],
          2014:['Birdman','comedy'],
          2016:['Moonlight','drama'],
          2017:['The Shape of Water','fantasy'],
          2020:['Parasite','drama']}

menu = """
        ----------------------------------------------------------------
            1 - display winning movie by year
            2 - display movie and category by year
            3 - add movie and category to list for an entered year
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

    clear()
    print(menu)
    option = str(input('Select one of the menu options above: '))

# Each 'if' statement corresponds to the option the user inputs and for each
# option, a different set of instructions follows. If the user input is '1',
# then ask the user to enter a year. If the year is valid, return the winning
# movie for said year. If not valid, print an error statement and ask the user
# if they would like to add a new entry.

    if option == '1':
      found1 = False
      year = int(input('\nEnter the year of the movie: '))
      year = validateYear(year)
      for y in movies:
        if year == y:
          print('\nThe winning movie for the year',year,'was',movies[y][0])
          found1 = True
          mainMenu()
          break
      if not found1:
        addMovie(year,categories)

# For option 2, the user is prompted to enter a year. The year is validated and
# returned back to main where it is used in the 'for' loop to see if it appears
# in the dictionary. If an instance is found, then the resulting year, title, and
# category are printed for the user's viewing. If the year is not found, a
# message displays that the year was not found and if the user would like to
# create a new entry. If yes, execute the addMovie function.

    elif option == '2':
      found2 = False
      year = int(input('\nEnter the year of the movie: '))
      year = validateYear(year)
      for y in movies:
          if year == y:
                print('\nThe winning movie for the year',year,'was',movies[y][0],'\nThe'
                      ' category of the film is',movies[y][1])
                found2 = True
                mainMenu()
                break
      if not found2:
        addMovie(year,categories)

# Option 3 checks to see if a year entered by the user is valid and in the list.
# If the year is not valid, re-prompt the user to enter a year until it is within
# the specified range. If the year is in the dictionary, display the movie title
# and category. Then, prompt the user if they would like to modify the existing
# film title and category for that year. If yes, then execute the modMovie
# function. If, however, the entered year is not in the dictionary, ask the user
# if they would like to create a new entry. If so, execute the addMovie function.

    elif option == '3':
        found3 = False
        year = int(input('Enter the year of the movie: '))
        year = validateYear(year)
        for m in movies:
            if year == m:
                print('\nThe year',m,'is already in the list.'
                        ' \nThe corresponsing film name is',movies[m][0],'and its category'
                        ' is',movies[m][1])
                found3 = True
                mod = input('\nWould you like to replace with new'
                            ' information? (Y/N): ')
                mod = mod.upper()
                if mod == 'Y':
                    modMovie(year,categories)
                    break
                else:
                    break
        if not found3:
            addMovie(year,categories)

# Option P simply takes the existing movie dictionary and prints it in a neat
# format, displaying the year, title, and category. If any modifications are made
# to the dictionary prior to option p being selected, then those will show up in
# the display as well.

    elif option == 'p':
        print('\n| Year | Winning Film For That Year | Film Category |\n--------------------'
              '---------------------------------')
        for i in sorted(movies.keys()):
            print('|',i,'|',movies[i][0],' '*(25-len(movies[i][0])),
                  '|',movies[i][1],' '*(12-len(movies[i][1])),'|')
        mainMenu()

# Option PC takes user input for category and checks through the movies dictionary
# to see if there are any corresponding movies that fit the category. If the user
# enters a category that is not in the 'categories' tuple, then an error message
# prints asking the user to re-enter the category until a correct response
# is submitted.

    elif option == 'pc':
        genre = input('Enter a movie category: ')
        if genre not in categories:
            print('Invalid category entered. Please try again.')
            continue
        else:
            print('\n| Year | Winning Film of the Category | \n'
              '---------------------------------------')
            for g in sorted(movies.keys()):
                if genre == movies[g][1]:
                    print('|',g,'|',movies[g][0])
            mainMenu()

# Finally, for option Q, the program simply ends. Any changes made to the
# dictionary during the program's execution is reset back to whatever the list
# was defined as at the beginning.

    elif option == 'q':
        sys.exit()

    else:
        print('\nInvalid option entered.')
        mainMenu()
        continue
