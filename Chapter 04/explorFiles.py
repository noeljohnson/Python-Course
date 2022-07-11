##GTG

# program to explore file operations


f = open("data.txt", "w") #opening in write mode
f.write("Hello\n")
f.write("World\n")
f.close()

f = open("data.txt") #opens in read mode by default
print(f.read()) # use iterators instead for larger files
f.close() 

f = open("data.txt")
for lines in f:print(lines) #using iterators
f.close()

#using unicode data

f = open("unidata.txt", 'w', encoding="utf-8")
f.write("sp\xc4m")
f.close()

#reading raw
raw = open("unidata.txt", "rb").read()
##TYJC
