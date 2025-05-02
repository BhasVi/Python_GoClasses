### String in python ###

str = "bhaskar"
print(str)

print(str[0])
print(str[4])
print(str[-1])

s =       "abc"
# index    012
# index   -3-2-1       
# always start from 0 and go to n-1

# string length
name = "ravishankar"
print(len(name))
print(name[0])
print(name[len(name)-1])

# sring concatenation
s1 = "bhaskar"
s2 = "kumar"
print( s1 + s2 + "is a good boy")

# repetition
s = "bhaskar"
print(s*4)
print(4*s)

# in and not in   
# example
sentence = "bhaskar is a good boy"
print("bhaskar" in sentence)
print("ood" in sentence)
print("bhaskar" not in sentence)

# comparing strings
"abc"< "abcd"
"abcd" <= "abc"

print("abc" < "abcd")        # True
print("abcd" <= "abc")       # False
print("Paul Jones" < "Paul Smith")    # True
print("Paul Smith" < "Paul Smithson") # True
print("Paula Smith" < "Paul Smith")   # False

### Slicing ###
# syntax
# string[start:end]               where end indexis not included
# string[start:end:step]          where step is the number of characters to skip and step is optional by default it is 1

s = "bhaskar"
print(s[0:4])
print(s[0:4:2])

print(s[:4])
print(s[4:])
print(s[0:6:2])

print(s[2:len(s)])
print(s[2:len(s)-1])

print(s[-7:-3]) # -7 is the start index and -3 is the end index
print(s[-3:-7]) # empty string because -3 is greater than -7
print(s[7:3])   # empty string because 7 is greater than 3

s = "bhaskar"
print(s[4:0:-1])

print(s[1:4:-1])  # empty string because step is negative

#string[a:b:c] a b values defines by the value of c 
# if c is positive it goes left to right 
# if c is negative it goes right to left 
# according to the value of c the value of a and b are defined

# More slicing examples with HelloWorld
s = "HelloWorld"
print(s[5::-1])    # Output: 'olleH'
print(s[:3:-1])    # Output: 'dlroWo'
print(s[5:0:-1])   # Output: 'olleH'

# The above examples demonstrate:
# 1. s[5::-1] - starts from index 5, goes backwards to start
# 2. s[:3:-1] - starts from end, goes backwards until index 3
# 3. s[5:0:-1] - starts from index 5, goes backwards until index 0

s = "HelloWorld"
print(s[::-1])        # popular syntax for reversing a string

print(s[::-2])

print(s[:len(s):-1])


# stripping 
s = "   bhaskar   "
print(s.strip())

print("   bhaskar   ".strip())

print(s.lstrip())
print(s.rstrip())

s = "bhaskar"
print(s.lstrip("b"))
print(s.rstrip("r"))

# string methods
s = "bhaskar"
print(s.upper())
print(s.lower())

# string is immutable
str = 'abc'
str[1] = 'z'
str = 'xyz'
print(str)

# s.() any function returns a new string 
# whenver you concatentate two strings or append something to a string, you create a new string
