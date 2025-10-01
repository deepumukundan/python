expenses = [10.50, 20.75, 30.00, 15.25, 5.00]

total_expenses = sum(expenses)
print("Total expenses1:", total_expenses)

sum = 0
for expense in expenses:
    sum += expense
print("You spent $", sum, sep='')