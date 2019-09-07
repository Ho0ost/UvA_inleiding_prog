from random import *

def make_prime_list():
    primelist_return = []                                     # make list to store primes
    num = 2                                            # start at 2 because everything below 2 aint no prime

    for x in range (5000):                       # find all primes under 10000, loops 5000 times because we skip even numbers      
        Prime = True                                   # make sure prime is set to true else it wont detect primes

        for x in range (2, num):                       # forloop to check for pime, starts at 2 (because everything is divisible by 1) and ends 1 before the input number (num)  
            result = num%x                             # uses modulus to check if result is whole number
            if result == 0:                            # if output from modulus is 0, it is no prime
                Prime = False                          # set prime to false
        if Prime == True:                              # if prime wasn't set to false in the for loop, this means the number is a prime
            primelist_return.append(num)                      # add number to Primelist
            #print(num)
        if num >=3:                                    # skip even numbers
            num +=2                             
        else:                                          # but dont skip 2
            num +=1         

    return(primelist_return)

def prime_factors(input_value,primelist):
    NOT_ONE = True
    n=2
    prime_factor_list = []
    while(NOT_ONE):
        if (input_value%n == 0):
            division_ans = input_value / n 
            if (division_ans == 1):
                NOT_ONE = False
                prime_factor_list.append(input_value)
            elif division_ans in primelist:
                prime_factor_list.append(division_ans)
                input_value = input_value / division_ans
                n=1
            
                
                    
        n +=1
    return (prime_factor_list)

def request_input():
    input_value = int(input(""))
    while (input_value <=1):
        print("invalid input, please try again")
        input_value = int(input("insert value\n"))
    while (input_value in primelist):
        print("number is already a prime, please try again")
        input_value = int(input("insert value\n"))
    return input_value

def dividers(list1,list2):
    pos1 = 0
    len1 = len(list1)
    while(pos1 < len1):
        if (list1[pos1] in list2):
            return True
        else:
            pos1 += 1

def riemann_zeta(n_checks):
    riemann = 0
    for x in range (2,n_checks):
        riemann = riemann + (1/pow(x,2))
    return riemann

div = 0
nodiv = 0

# Generate prime list
print("generating prime list ...")
primelist = make_prime_list()           # Get first 10000 primes
print("list generated")
random_checks = 100000

for x in range (random_checks):

    ### Request for input value ###
    #print("insert first value:")
    #first_value = request_input()
    first_value = randint(10000, 100000)
    #print("insert second value:")
    #second_value = request_input()
    second_value = randint(10000, 100000)


    # Find prime factors
    prime_factor_list_first = prime_factors(first_value, primelist)
    #print(prime_factor_list_first)
    prime_factor_list_second = prime_factors(second_value, primelist)
    #print(prime_factor_list_second)

    if (dividers(prime_factor_list_first, prime_factor_list_second)):
        #print("common dividers")
        div +=1

    else:
        #print("no common dividers")
        nodiv += 1
    print("progress: ",round(((x/random_checks)*100),1),"%")

print ("dividers: ",div)
print ("no dividers: ", nodiv)
print ("chance of no common dividers = ", (nodiv/x))
print ("riemann: ", riemann_zeta(random_checks))