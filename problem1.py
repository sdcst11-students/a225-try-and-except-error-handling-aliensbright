#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
#import os
#os.system('cls')
import math

print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")
while True:
  a=input('Enter the "a" value:')
  b=input('Enter the "b" value:')
  c=input('Enter the "c" value:')
  try:
    a=float(a)
    b=float(b)
    c=float(c)
    dis = b**2 - 4 * a * c
    try:
      sqrt=math.sqrt(dis)
      root1=(-b+sqrt)/(2*a)
      root1=round(root1,2)
      root2=(-b-sqrt)/(2*a)
      root2=round(root2,2)
      print(f'The roots of the equation are {root1} and {root2}')
    except:
      print('There are no real roots to the equation.')
  except:
    print('These are not valid values for a, b or c.')
