print('Welcome to PyPassword Generator!')

import random
letters = [ 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z'
    ]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

l_keyword= int(input('How many letters would you like in your password? '))
s_keywords= int(input('How many symbols would you like? '))
n_keywords = int(input('How many numbers would you like? '))


