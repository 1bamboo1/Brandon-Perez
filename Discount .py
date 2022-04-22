# This program uses functions and variables

# the main function
def main():
    print('Welcome to the variable program')
    print()   # prints a blank line
    
    name = inputName()
    print('Hello', name)

# this function inputs data
def inputName():
    name = input('Enter your name: ')
    return name

# calls main
main()

# This program uses functions and variables

# the main function
def main():
    print('Welcome to the meal calculator program')
    print()   #prints a blank line
        mealprice = input_meal()
            mealprice = input('enter the meal price $')
            mealprice = float(mealprice)
            return mealprice
        tip = calc-tip(mealprice)
            def calc_tip(mealprice):
                tip = mealprice * .20
            return tip
        tax = calc_tax(mealprice)
            def calc_tax(mealprice):
                tax = mealprice * .06
            return tax
        total = calc_total(mealprice, tip, tax)
            def calc_total(mealprice, tip, tax):
                total = mealprice + tip + tax
            return total
        print_info(mealprice, tip, tax, total)
             def print_info(mealprice, tip, tax, total):
                print 'The meal price is $', mealprice
                print 'The tip is $', tip
                print 'The tax is $', tax
                print 'The total is $', total