def main():
    outfile = open ('1scores.txt','w')
    
    name1 = input('player name and score #1:')
    name2 = input('player name and score #2:')
    name3 = input('player name and score #3:')
    
    outfile.write(str(name1) + '\n')
    outfile.write(str(name2) + '\n')
    outfile.write(str(name3) + '\n')
    
    outfile.close()
    print('data written to 1scores.txt')
main()