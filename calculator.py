# estimated yearly interest

print('How many years do you plan on saving?')
years = int(input('Enter years: '))

print('How much money is currently in your account?')
principal = float(input('Enter amount: '))

print('How much do you plan on investing monthly?')
monthly_invest = float(input('Enter amount: '))

print('What do you estimate is the yearly interest of this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1):'))

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years): 
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest) 

    final_amount = round(final_amount, 2)

print('This is how much money you would have in your account after {} years: '.format(years) + str(final_amount))