#stock quanitity input from usert declared and asigned to variable name stock_quantity
stock_quantity = int(input('How many ice_cream would you like to buy? '))
#Quantity of Stock avaliable for purchase
stock_avaliable = 10
#stock initialization
i = 1
#checking and comparing the variable i  with stock quanity from user input
while i<=stock_quantity:
    #condition statement to check if user wants is more than what avaliable in stock for purchase
    if i>stock_avaliable:
        #message to the user
        print('Out of Stock, Kindly check back')
        #stop the transaction
        break
    #output of stock to the user
    print('ice_cream')
    #increment value of positive value of 1 
    i+=1
#Greeting message to the user
print('Thanks for shopping with us, please do come again')