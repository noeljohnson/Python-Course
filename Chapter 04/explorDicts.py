##GTG

# A program to explore python dictionaries

#initializing a list using literal
d = {"name" : "John Doe", "age" : 36, "gender" : "male"}

#using assignment
d1 = {}
d1["name"] = "John Doe"
d1["age"] = 36
d1["gender"] = "male"

#using calls
d2 = dict(name = "John Doe", age = 36, gender = "male")

#using zips
d3 = dict(zip(["name", "age", "gender"], ["John Doe", 36, "male"]))

# to check if a given key is there in the dictionary
val = d['x'] if 'x' in d else 0
val1 = d.get('x', 0)

#traversing through a dictionary based on sorted keys

for ks in sorted(d):
  print(ks, '=>', d[ks])

##TYJC
