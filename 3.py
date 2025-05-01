# Implicit Type Conversion
# Python automatically converts one data type to another when necessary

# Adding an int and a float
x = 10
y = 20.5
result = x + y
print(result) # 30.5

a = 53.1
print(type(a))
b = int(a)           # int(a) converts the float to an int but it not changes the value of a
print(type(b))       

# Short hand Operator
x = 10
x += 5               # x = x + 5  applicable for all arithmetic operators
print(x)             

# x * = y -2  --->  x = x * (y - 2)   not  x = x * y - 2


# Logical Operators, Comparison Operators, Bitwise Operators are used to compare values and return a boolean value (True or False)

### Comparison Operators ###
# ==  equal to
# example:          
x = 10
y = 20
print(x == y)  # False

# !=  not equal to
# example:
x = 10  
y = 20
print(x != y)  # True

# >   greater than
# example:
x = 10      
y = 20
print(x > y)  # False

# <   less than
# example:
x = 10
y = 20
print(x < y)  # True

# >=  greater than or equal to  
# example:
x = 10
y = 20
print(x >= y)  # False

# <=  less than or equal to
# example:
x = 10
y = 20
print(x <= y)  # True

# 9>7>6     9>7  ---> True  and 7>6  ---> True  so 9>7>6  ---> True

# True = 1 
# False = 0

print(int(True))
print(bool(1))

print(int(False))
print(bool(0))

# bool(0) bool(0.0) bool(None) bool("") bool([]) bool({}) bool(()) are False otherthan that all values are True


### Logical Operators ###
# and   operator reutnrn false if any of the operand is false and true if all the operands are true
# example:
x = 10
y = 20
z = 30
print(x < y and y < z)  # True
print(x < y and y > z)  # False

# or    operator returns true if any of the operand is true and false if all the operands are false
# example:  
print(x < y or y > z)  # True
print(x > y or y > z)  # False

# not   operator returns true if the operand is false and false if the operand is true
# example:
print(not x < y)  # False
print(not x > y)  # True


### Bitwise Operators ###
# &   bitwise and        if both the bits are 1 then the result is 1 otherwise 0
# example:
x = 10  # 1010
y = 20  # 10100
print(x & y)  # 0

# |   bitwise or         if any of the bit is 1 then the result is 1 otherwise 0
# example:
x = 10  # 1010
y = 20  # 10100
print(x | y)  # 30

# ^   bitwise xor        same 0 different 1
# example:
x = 10  # 1010
y = 20  # 10100
print(x ^ y)  # 30

# ~   bitwise not         it is a unary operator and it is used to flip the bits of the number
# example:              
x = 10  # 1010
print(~x)  # -11          formula: ~x = -(x+1)

# <<  left shift        it is used to shift the bits of the number to the left
# example:
x = 10  # 1010
print(x << 1)  # 20       formula: x << y = x * (2^y)

# >>  right shift        it is used to shift the bits of the number to the right
# example:
x = 10  # 1010
print(x >> 1)  # 5        formula: x >> y = x // (2^y)


#### Conditional Statements ####
# if statement            if statement have atmost one else statement(optional) and else statement cannot be used without if statement
#  example: 
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
# example:
x = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

# if-elif-else statement
# example:
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# nested if statement
# example:
x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10:
        print("x is equal to 10")


### Short-Circuit Evaluation ###
# and operator
# example:
x = False
y = True
print(x and y )  # False    if x is false then y is not evaluated but if x is true then y is evaluated

# or operator
# example:
x = True
y = False
print(x or y)  # True     if x is true then y is not evaluated but if x is false then y is evaluated

# Q. 1 or 0 and 0 
# case 1: 1 or (0 and 0)  ---> 1 or 0  ---> 1    Right answer
# case 2: (1 or 0) and 0  ---> 1 and 0  ---> 0   Wrong answer
# because and operator has higher precedence than or operator






