##GTG

# A program to explore numbers

a = 1
b = 3

num = a / b

str1 = "%e" % num
str2 = "%4.2f" % num
str3 = "{0:4.2f}".format(num)

bool_res1 = a < b > num ## is same as a < b and b > num
bool_res2 = 1.1 + 2.2 ==  3.3 # gives false, due to numerical limitedness

num1 = -a // b # does floor division, similar to truncation for +ve values 
  # and trunc -1 for negative values

# converting to other bases using string formating 

str4  = "%d; %o; %x" % (13, 13, 13)

##TYJC
