from run_raindrops import *

# This will run the app allowing user to decide what number to use and print the factorials
n = ''
while n != 'exit':
    n = int(input("Enter a number: "))
    print(print_all_factors(n))
    print(pling_plang_plong(n))