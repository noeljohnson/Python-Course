##GTG

# a program to demonstrate variable assignments

a = 2 # variable dont have types, objects do variable gets linked to objects

# variable have header information and keeps track of how many variable names have shared access to it

b = a # variables cant point to variables, they can only point to objects, so now 2 has 2 references to
# itself

a = a + 2 # the RHS creates a new object as integers are immutable and arent changed in place

# so now a and b point to diffrent objects 2 now has a reference counter of 1 and 4 has a reference counter of 1

# whenever the reference counter of an object becomes 0, it is mostly recliamed by the garbage collector unless the object is cached (as happens with small numbers and commonly used expressions)

# now let us consider some mutable types

a = [1, 3, 5]
b = a

# b and a point to [1, 3, 5]

b[1] = 2 # now b and a point to [1, 2, 5] as this list operation is mutable

#if we didnt want this side effect to happen, we could use b = a[:], b = list(a), b = a.copy() or import copy and then b = copy.copy(a)

#to test if 2 objects are pointing to same object

isSameObj = b is a

# to get the reference count of an object we can do it as so

import sys

numRefCount = sys.getrefcount(1)

##TYJC
