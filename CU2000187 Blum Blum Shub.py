################### Blum Blum Shub random number generator ###################
# Formula = xn+1=xn**2(modM).

# Importing time to use it in the seed.
import time

rangee= ["Integer","integer","I","i","Time","time","T","t","File","file","F","f"]
mode = input ("Do You want to enter 'Integer', 'File' or 'Time' mode: ")
seed = 0
a = 3  # a is a selected prime number.
c = 997 # c is a selected prime number.
m = a * c #  m in the rule is equal to the multiplication of the two prime numbers(a and c).

# The time on the machine is used to make the seed more random.
if mode not in rangee:
    print("Please input an answer only from the question. ")   
elif mode == "Integer" or mode == "integer" or mode == "I" or mode == "i" :
    seed = int(input("please enter the seed number: "))
elif mode == "Time" or mode == "time" or mode == "T" or mode == "t" :
    seed = int(round(time.time()))
elif mode == "File" or mode == "file" or mode == "F" or mode == "f" :
    file = open('file test.txt','r')
    seed = file.read()
    file.close()
    
# Giving the option to the user of how many random numbers does he want.
howmany = int(input("How many random numbers do you want?: "))

# Function to calculate the formula using numbers in a specific range;
# Which is used a for loop to get that range from the number the user entered;
# But in every loop it decrease the howmany by 1 untill it gets to 0;
# And x is printed before it is equaled to the previous seed.
def random():
    num_base = seed
    for i in range(howmany, 0, -1):
        x = (num_base**2) % m
        print(x)
        num_base = x
random() # The function must be called in order to run.