# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

# If either input is an empty string, consider it as zero.

# code
def sum_str(a, b):
    if not a:
        a = "0"
    if not b:
        b = "0"
    return str( int(a) + int(b) )
    pass

test = sum_str("5", "10")
print(test)