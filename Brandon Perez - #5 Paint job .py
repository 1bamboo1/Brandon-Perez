# Chapter.5
# 08. Paint Job Estimator

area = float(input('Enter the square feet of wall space to be painted: '))
price_of_paint = float(input('Enter the price of the paint per gallon: $'))

def calculate(area, price_of_paint):
    print('The number of gallons of paint required is', format(area / 112,
                                                               '.2f'))
    print('The hours of labor required is', format(area / 112 * 8, '.2f'))
    print('The cost of the paint is $', format(area / 112 * price_of_paint,
                                             '.2f'), sep='')
    print('The labor charges is $', format(area / 112 * 8 * 35, '.2f'), sep='')
    print('The total cost of the paint job is $',
          format(area / 112 * price_of_paint + area / 112 * 8 * 35, '.2f'),
          sep='')

calculate(area, price_of_paint)

# >>> %Run 'Paint job .py'
# Enter the square feet of wall space to be painted: 3500
# Enter the price of the paint per gallon: $40
# The number of gallons of paint required is 31.25
# The hours of labor required is 250.00
# The cost of the paint is $1250.00
# The labor charges is $8750.00
# The total cost of the paint job is $10000.00
# >>> 