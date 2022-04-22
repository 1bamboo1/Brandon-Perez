days = int(input("enter the number of days:"))
total = 0

for x in range(days):
    pay = 2**x
    total += pay
    print(x+1,"\t", pay)
total_pay = total / 100


print("The total earning were", format(total_pay, '.2f'))

# >>> %Run pennies.py
# enter the number of days:22
# 1 	 1
# 2 	 2
# 3 	 4
# 4 	 8
# 5 	 16
# 6 	 32
# 7 	 64
# 8 	 128
# 9 	 256
# 10 	 512
# 11 	 1024
# 12 	 2048
# 13 	 4096
# 14 	 8192
# 15 	 16384
# 16 	 32768
# 17 	 65536
# 18 	 131072
# 19 	 262144
# 20 	 524288
# 21 	 1048576
# 22 	 2097152
# The total earning were 41943.03
# >>> 