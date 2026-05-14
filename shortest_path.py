from math import factorial
 
start = "AAAA"

end = "BBBB"
 
length = 0
 
for i in range(len(start)):

    if start[i] != end[i]:

        length += 1
 
paths = factorial(length)
 
print("Length:", length)

print("Paths:", paths)
 