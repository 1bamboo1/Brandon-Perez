def main():
    
    charge_account = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 8080152, 4562555, 5552012, 5050552, 7825877, 1250255, 1005231, 6545231, 3852085, 7576651, 7881200, 4581002]
        accountfile = open('charge_account.txt', 'r')

    again = 'y'

  
    while again == 'y':
        
        account_number = int(input('Enter charge account number:'))

        
        charge_account.append(account_number)

     
        for account_number in charge_account:
            print(account_number)
   
    search = input('Enter a charge account number to search for:')
    if search not in charge_account:
        print(search, 'Is Invalid')
    else:
        print(search, 'Is valid')

    accountfile.close()


main()