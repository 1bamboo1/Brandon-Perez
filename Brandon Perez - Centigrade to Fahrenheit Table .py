temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")

start = in
end = in
increment = in

def main():   
    #create table headers
    print('The following table shows conversion of Celsius to Farenheit')
    print( 'between 0 and 20 degrees Celsius.')
    print('')
    print('Celsius\t   Farenheit')
    print('____________________')

    #convert celsius input to farenheit using loop
    for Celsius in range (start, end, increment):
        Farenheit = (9 / 5) * Celsius + 32
        print(Celsius, '\t', format(Farenheit, '.1f'))

main()