item1 = int(input('Price of item1? '))
item2 = int(input('Price of item2? '))
item3 = int(input('Price of item3? '))
item4 = int(input('Price of item4? '))
item5 = int(input('Price of item5? '))
subtotal = item1 + item2 + item3 + item4 + item5
print(f'The total price of all item purchased ${subtotal} ')
Salestax = int(input('What is the sales tax price? '))
Salestax_calulated = Salestax / 100
print(f'The sales tax price is {Salestax_calulated} percent')
total_sales = subtotal * Salestax_calulated
print(f'The total sales is ${total_sales}')