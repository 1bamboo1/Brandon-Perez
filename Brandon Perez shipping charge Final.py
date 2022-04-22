weight_of_package = float(input("enter weight of package: "))
shipping_charges = 0.0

messege = "shipping charges = "

if weight_of_package <= 2:
    shipping_charges = weight_of_package * 1.10
elif weight_of_package > 2 and weight_of_package <= 6:
    shipping_charges = weight_of_package * 2.20
elif weight_of_package > 6 and weight_of_package <=10:
    Shipping_charges = weight_of_package * 3.70
elif weight_of_package >10:
     shipping_charges = weight_of_package * 3.80
     
messege += "$" + format(shipping_charges, ',.2f')

print(messege)

 
# >>> %Run 'shippingggg charges.py'
# enter weight of package: 5.5
# shipping charges = $12.10
# >>> %Run 'shippingggg charges.py'
# enter weight of package: 12.2
# shipping charges = $46.36
# >>> 