Longest_No_Prime_Series = 0                        # set longest 
Primelist = []                                     # make list to store primes
num = 2                                            # start at 2 because everything below 2 aint no prime
pos = 1                                            # set pos to 1, pos is used to scroll through the no prime list

for numbers in range (5000):                       # find all primes under 10.000, loops 5000 times because we skip even numbers      
    Prime = True                                   # make sure prime is set to true else it wont detect primes

    for x in range (2, num):                       # forloop to check for pime, starts at 2 (because everything is divisible by 1) and ends 1 before the input number (num)  
        result = num%x                             # uses modulus to check if result is whole number
        if result == 0:                            # if output from modulus is 0, it is no prime
            Prime = False                          # set prime to false
    if Prime == True:                              # if prime wasn't set to false in the for loop, this means the number is a prime
        Primelist.append(num)                      # add number to Primelist
    if num >=3:                                    # skip even numbers
        num +=2                             
    else:                                          # but dont skip 2
        num +=1         

Lenght_list = len(Primelist)                                # find lenth of Primelist
for x in range (Lenght_list-1):                             # range lenght_list-1 to make sure it doesnt go out of range
    No_Prime_Series = Primelist[pos] - Primelist[pos-1]     # subtract two following primes to find lengt of No_Prime_Series 
    if No_Prime_Series > Longest_No_Prime_Series:           # check if series is longer than longest series
        Longest_No_Prime_Series = No_Prime_Series           # save the longest No_Prime_Series
        Starting_number = Primelist[pos-1]                  # save starting point
        Ending_number = Primelist[pos]                      # save ending point
    pos += 1                                                # pos++

# print output, Stating_number and Ending_numbers are primes at the moment, so the output will be
# stating number plus 1 and ending number minus 1
print("De langste reeks niet-priemgetallen onder de 10.000 begint op",Starting_number+1 ,"en eindigt bij",Ending_number-1,)
print("De reeks is",Longest_No_Prime_Series-1,"lang.")


