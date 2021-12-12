s1 = "jeff is doing a. String practise functions practise"
print(s1.capitalize())  # capitalizes first letter of the string
print(s1.split(sep="."))  # splits the sentence depending on the separation used.Space is the default
print(s1.replace("practise", "training", 1))  # replaces assigned word
s2 = "JEFF IS DOING STRING FUNCTIONS PRACTICE"
print(s2.casefold())  # converts string to lower case
print(s2.center(1, "J"))  # to be revisited
print(s2.endswith("G"))  # returns True or False
print(s2.startswith("S", 0, 13))  # returns True or False
s3 = "jeff"
print(s3.isalpha())  # checks if its an alphabetic string
print(s3.islower())  # checks if string is in lower case....can use upper to check the opposite
s = "123"
print(s.isdigit())  # to check if a string is composed of digits only
print(s3.isidentifier())  # check if a string is an identifier
print(s2.join("i"))
for i in s2:
    print(i, end=" ")
""" note the differences """
# partition joins the rest of the characters while split does not
print(s2.rpartition("N"))  # partition from behind
print(s2.partition("N"))  # partition from front
print(s2.split())
""" f-string"""
from lists import l1  # imported list
s4 = "jeff"
s5 = "coding"
s6 = "Python"
print(f"{s4.title()} is doing some {s5.title()} practises in {s6.upper()}")
print(f"{s4.title()} is recalling a list {l1}")  # using the imported list
