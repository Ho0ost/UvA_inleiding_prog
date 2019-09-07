# This program is used to find prime numbers

User_input = input ("Insert number\n")      # user input
User_input = int (User_input)               # Cast User_input from str to int
if User_input <= 0:                         # Check if input is forbidden (0 and negative numbers are forbidden)
    while User_input <= 0:                  # Loop while input is forbidden
        #print("Wrong input, please try again")     # Not used because checkpy cant handel it
        User_input = input ("Insert number\n")      # Re-enter user input
        User_input = int (User_input)               # cast User_input from str to int

num = 2                                     # start at 2 because 1 is no prime
while User_input > 0:                       # program keeps looping until the requested number is found
    Prime = True

    for x in range (2, num):                # forloop to check for pime, starts at 2 (because everything is divisible by 1) and ends 1 before the input number (num)
        result = num%x                      # uses modulus to check if the results is a whole number
        if result == 0:                     # if result is whole number, it is no prime
            Prime = False
    if Prime == True:                       # else number is prime
        #print("the number ",num, "is prime\n")
        User_input -=1                      # if prime number is found, User_input--
        New_prime = num                     # put prime number in New_prime
    if num >=3:                             # if 2 has been checked, start skipping even numbers, even numbers are never primes (only 2)
        num +=2                             # if num wasn't put in New_prime, the output would num would have changed here
    else: 
        num +=1      

print (New_prime)                            # print requested number
