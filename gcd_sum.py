from math import gcd
 
lines = [

    "18 24 30",
    "7,14,21",
    "9, 27, 81",
    "100 200 300",
    "5 10",
    "8,16,24,32",
    "-12 -18 -24",
    "11, 22, abc",
    "0 0 5"

]
 
total = 0
 
for line in lines:
 
    try:

        # Replace commas with spaces

        line = line.replace(",", " ")
 
        # Convert values to integers

        numbers = list(map(int, line.split()))
 
        # Check exactly 3 integers

        if len(numbers) == 3:
 
            current_gcd = gcd(numbers[0], gcd(numbers[1], numbers[2]))
 
            total = total + abs(current_gcd)
 
    except:

        continue
 
print(total)
 