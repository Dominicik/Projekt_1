"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dominik Brychta
email: dominic.Brychta@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
line = '–' * 50
TEXTS_replace = [TEXTS[0].replace(',', '').replace('.', ''), 
                 TEXTS[1].replace(',', '').replace('.', ''), 
                 TEXTS[2].replace(',', '').replace('.', '')]
TEXTS_split = (TEXTS_replace[0].split(), 
               TEXTS_replace[1].split(), 
               TEXTS_replace[2].split())

login_username = input('user name:')

if login_username in users:
    login_password = input('password:')
    password_control = users.get(login_username)

    if login_password == password_control:
        print(f'username: {login_username} \npassword: {login_password} \n{line}')
        print(f'Welcome to the app, {login_username.title()}')
        print('We have 3 texts to be analyzed')
        print(line)

        number_analysis = (input('Enter a number btw. 1 and 3 to select'))

        if number_analysis.isnumeric() and int(number_analysis) in range(1,4):
            print (f'Enter a number btw. 1 and 3 to select: {number_analysis}')
            print(line)

            word_count = 0
            titlecase_count = 0
            uppercase_count = 0
            lowercase_count = 0
            sum_of_numbers = 0
            numeric_strings_count = 0


            for word in TEXTS_split[int(number_analysis) - 1]:
                word_count += 1
                if word.istitle():
                     titlecase_count += 1           
                if word.isupper():
                     uppercase_count += 1            
                if word.islower():
                     lowercase_count += 1            
                if word.isnumeric():
                     numeric_strings_count += 1
                     sum_of_numbers += int(word)
                
            print(f'There are {word_count} words in the selected text.')
            print(f'There are {titlecase_count} titlecase words.')
            print(f'There are {uppercase_count} uppercase words.')
            print(f'There are {lowercase_count} lowercase words.')
            print(f'There are {numeric_strings_count} numeric strings.')
            print(f'The sum of all the numbers {sum_of_numbers}')

            
            word_length = []
            for word in TEXTS_split[int(number_analysis) - 1]:
                word_length.append(len(word))
            
            from collections import Counter
            word_length_counted = Counter(word_length)




            print(f'{line}\nLEN| \t OCCURENCES \t |NR.\n{line}')
            for length, count in sorted(word_length_counted.items()):
                print(f'{length:4}|{"*" * count:20}|{count}')


        else:
            print('Incorrect value, terminating the program...')

    else:
        print('Unregistered user, terminating the program...')     

else:
    print('Unregistered user, terminating the program...')