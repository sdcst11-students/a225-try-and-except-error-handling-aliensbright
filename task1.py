#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value

#number = int(number)

while True:
    num = input("Please enter in an integer value:")
    try:
        num=int(num)
        print('You have successfully inputted an integer!')
        break
    except:
        print("There was an error. Please try again\n")
