def check_num(n, mod):
    return n % mod == 0

def print_all_factors(n):
   print("The factors of",n,"are:")
   for i in range(1, n + 1):
       if n % i == 0:
           print(i)


def pling_plang_plong(n):
    print_all_factors(n)
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
    elif check_num(n, 9):
        return ('Plong')
    else:
        return n