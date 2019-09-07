# This code is used to check if goldbach's theory was right
# His theory is that every even number bigger than 2 can be written in two primes
def make_prime_list():
    primelist_return = []                                     # make list to store primes
    num = 2                                            # start at 2 because everything below 2 aint no prime

    for x in range (500):                       # find all primes under 1000, loops 500 times because we skip even numbers      
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

even_number = 4                         # Start checking the theory at 4 (first even number after 2)
pos1 = 0                                # Position 1 for the primelist list
pos2 = 0                                # Position 2 for the primelist list
NOT_DONE = True                         # Boolean to check if code is done

primelist = make_prime_list()           # Get first 1000 primes
#print (primelist)                      # Dont print because checkpy doesnt understand

while (NOT_DONE):
    primesum = int(primelist[pos1]+primelist[pos2])                     # Make sum of two primes
    if (primesum == even_number):                                       # If goldbach was right, print the output
        print(even_number,"=",primelist[pos1],"+",primelist[pos2],)
        even_number +=2                                                 # Goto the next even number
        pos1 = 0                                                        # Reset positions
        pos2 = 0
    else:                                                               # else go to the next position
        if pos1 < even_number:
            pos1 +=1
            if pos1 > 167:
                pos1=0
                pos2 +=1
        elif pos1 >= even_number:
            pos2 +=1
            pos1 = 0
            if (pos2 >= even_number):
                print("BINGO")                                              # goldbach was wrong!!!
                NOT_DONE = False

    if(even_number > 1000):                                               # end code if last value was found
        NOT_DONE = False