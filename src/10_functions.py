# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(i):
    if i % 2 == 0:
        print('*****************')
        print('true')
    else:
        print('*****************')
        print('false')
is_even(2)
is_even(23)
is_even(25)
is_even(26)

# Read a number from the keyboard
print('*****************')
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_it_even(i):
    if i % 2 == 0:
        print('*****************')
        print('Even!')
    else:
        print('*****************')
        print('Odd')

is_it_even(num)
print('*****************')
