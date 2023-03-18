# import counter class from collections module
from collections import Counter
 
# Creation of a Counter Class object using
# string as an iterable data container
x = Counter("hELLO") # Type any ord you like in the inverted commas 
 
# printing the elements of counter object
for i in x.elements():
    print ( i, end = " ")