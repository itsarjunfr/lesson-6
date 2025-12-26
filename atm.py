balance = 500
print('Your balance is: ', balance, 'dollars.')
money = int(input('Enter sum of money to be withdrawn: '))
if money<balance and money>0:
    print(money, 'dollars will now be withdrawn.')
    print(balance-money, 'dollars now remain in you account.')
elif money<0:
    print('Amount of money to be withdrawn is invalid.')
else:
    print('Your account has an insufficient amount of money.')
