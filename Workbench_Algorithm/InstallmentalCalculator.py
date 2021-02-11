purchase_amount = int(input('Enter the amount of total Purchase? '))

num_of_months = int(input('Enter amount of months? '))

per_amount = int(input('Enter percentage amount? '))
per_n_percent = per_amount / 100

per_purchase = purchase_amount * per_n_percent

total_purchase = per_purchase + purchase_amount

monthly_payment = total_purchase / num_of_months

print(f'The total amount of purchase is {round(total_purchase, 0)} and the price for each month will cost {round(monthly_payment, 2)} ')
