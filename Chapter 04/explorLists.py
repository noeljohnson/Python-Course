##GTG

# A program to explore the list data structure

l = [1, '2'] # a list can have elements with diffrent datatype
l.append(3) # adds to the end of the list
l.append(True)

l.pop(2) # removes the third element 

len(l) # for finding the length of lists
l = [[1, 2, 3], [4, 5]] #lists can have arbitary nesting

# list comprehension
l1 = [row[0] for row in l] # gets the first column
l1 = [row[1] for row in l if row[1] % 2 == 0] # can be used to filter out

#comprehensions in other data structure

word = "sspaam"

s1 = {i for i in word} #sets
d1 = {i:ord(i) for i in word} #dictionaries
g1 = (ord(i) for i in word) # generators
##TYJC
