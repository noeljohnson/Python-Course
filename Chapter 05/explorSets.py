##GTG

s1 = {1, 2}
s2 = {3, 4}

s3 = s1.union(s2) #creates new sets
s4 = s1.intersection(s2) #creates new sets

s2.update(s3)
s2.update([5, 6])

isSubset = s2.issubset(range(1, 7))

#set comprehension

s5 = {i ** 2 for i in range(-5, 6)}

##TYJC
