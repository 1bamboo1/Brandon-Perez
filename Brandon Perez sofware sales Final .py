PRICE_PER_PACKAGE = 99.00

number_of_packages = float(input('\nEnter # of packages purchased: '))

display_messge = ""

if number_of_packages < 0:
    display_message = "Error. # of packages must be greater than 0.\nRe-run program and try again."
else:
    discount_percentage = 0
    
    if number_of_packages < 10:
        discount_percentage = 0 
    elif number_of_packages >= 10 and number_of_packages <= 19:
        discount_percentage = .20 # 20
    elif number_of_packages >= 20 and number_of_packages <= 49:
        discount_percentage = .30 # 30%
    elif number_of_packages >= 50 and number_of_packages <= 99:
        discount_percentage = .40 # 40%
    elif number_of_packages >= 100:
        discount_percentage = .50 # 50%
        
    package_total = number_of_packages * PRICE_PER_PACKAGE
    discount_amount = (package_total) * discount_percentage
    grand_total = package_total - discount_amount
    display_messege = "package total + $" + format(package_total, '.2f') + \
                      "\nDiscount Percentage = " + format(discount_percentage, '.0%') + \
                      "\nDiscount amount = $" + format(discount_amount, ',.2f') + \
                      "\nGrand total = $" + format(grand_total, ',.2f')
        
    
print("\n" + display_messge + "\n")

# Python 3.7.9 (bundled)
# >>> %Run 'sofware sales.py'
# 
# Enter # of packages purchased: 22
# 
# 
# 
# >>> %Run 'sofware sales.py'
# 
# Enter # of packages purchased: 
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# Python 3.7.9 (bundled)
# >>> %Run 'sofware sales.py'
# 
# Enter # of packages purchased: 57
# 
# 
# 
# >>> 