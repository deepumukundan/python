# Get details of loan
money_owed = float(input("Enter the amount of money owed: ")) # $50,000
apr = float(input("Enter the annual percentage rate (APR): ")) # 3%
payment = float(input("How much do you want to pay each month? ")) # $1000
months = int(input("How many months do you want to see the resuts for? ")) # 24

for i in range(months):
    print('Month', i + 1, end=' ')
    # Calculate interest and update money owed
    # Convert APR to monthly rate
    monthly_rate = apr / 100 / 12
    interest_paid = money_owed * monthly_rate
    money_owed += interest_paid

    if money_owed - payment < 0:
        print('The last payment is', money_owed)
        print('You paid off the loan in', i + 1, 'months')
        break

    #Make payment
    money_owed -= payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('You now owe', money_owed)