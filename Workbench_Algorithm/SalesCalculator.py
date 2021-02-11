total_sales = int(input('What is the total sales? '))
sales_percentage = int(input('What is the total percent sales? '))
percentage_calculated  = sales_percentage / 100
annual_profit = total_sales * percentage_calculated
print(f'The total profit for the year is ${int(annual_profit)}')