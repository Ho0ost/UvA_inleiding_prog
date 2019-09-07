# This code multiplies two user input values and returns the results
First_val = input("insert first value \n")      # Request for first value
Second_val = input("insert second value \n")    # Request for second value
First_val = int (First_val)                     # Cast str to int
Second_val = int (Second_val)                   # Cast str to int
result = First_val*Second_val                   # multiply values
print ("result of",First_val, "times", Second_val, "=", result,"\n")   # Print result
