## This function is used to check if the given number is divisable by a modulus and will return true or false
def check_num(n, mod):
    return n % mod == 0

# This function is used to print out all the factors of the given number
def print_all_factors(n):
   print("The factors of",n,"are:")
   for i in range(1, n + 1):
       if n % i == 0:
           return i

# This function will determine if the given number outputs Pling Plang or Plong and the factors of that number
def pling_plang_plong(n):
    if check_num(n, 5) and check_num(n, 3) and check_num(n, 7):
        return ('PlingPlangPlong')
    elif check_num(n, 5) and check_num(n, 3):
        return ('PlingPlang')
    elif check_num(n, 5) and check_num(n, 7):
        return ('PlangPlong')
    elif check_num(n, 3) and check_num(n, 7):
        return ('PlingPlong')
    elif check_num(n, 3):
        return ('Pling')
    elif check_num(n, 5):
        return ('Plang')
    elif check_num(n, 7):
        return ('Plong')
    else:
        return n