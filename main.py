# Programmed by John Elehwany and Rayan Haq
# Loyola CS151, Professor Zee
# Due Date: October 9, 2024
# Lab Assignment: 04

# This program determines the price and GB provided, depending on what package plan the user chooses, how much GB the user has used, and if the user has a coupon or not.

print("""
Package Plan Calculator
""")

# Asks user for input of package

package = input('Enter the desired package plan (green, blue, or purple): ')

# Checks for a correct input of package
while package not in ['green', 'blue', 'purple']:
    print('Invalid answer. Please input a valid package.')
    package = input('Enter the desired package plan (green, blue, or purple): ')

if package == 'green': # Outcomes if Package Green is selected
    price = 49.99
    gb = 2
    while True: # Checks if extra_gb answer is a number
        try:
            extra_gb = float(input('How much extra GB have you used? ')) # Asks for extra GB
            break
        except ValueError:
            print('Invalid answer. Please input a number.')

    if extra_gb > gb:
        extra_charge = (extra_gb - gb) * 15
        price = price + extra_charge

    coupon = input('Do you have a coupon for this package? (yes or no) ')

    while coupon not in ['yes', 'no']:
        print('Invalid answer. Please only answer yes or no.')
        coupon = input('Do you have a coupon for this package? (yes or no) ')

    if coupon == 'yes' and price >= 75:
        price = price - 25
    elif coupon == 'no':
        price = price
    else:
        price = price

    print(f"""
    Total cost: ${price:.2f}
    Total GB: {extra_gb + gb}""")

elif package == 'blue': # Outcomes if Package Blue is selected
    price = 70
    gb = 4
    while True: # Checks if extra_gb input is a number
       try:
            extra_gb = float(input('How much extra GB have you used? '))  # Asks for extra GB
            break
       except ValueError:
           print('Invalid answer. Please input a number.')

    if extra_gb > gb:
        extra_charge = (extra_gb - gb) * 10
        price = price + extra_charge
    # Prints total value
    print(f"""
    Total cost: {price:.2f}
    Total GB: {extra_gb + gb}""")

elif package == 'purple': # Outcomes if Package Purple is selected
    price = 99.95
    gb = 'unlimited'

    print(f"""
    Total price: {price:.2f}
    Total GB: {gb}""")