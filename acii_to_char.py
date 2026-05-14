input_str = "72-101-108-108-111"
ascii_list = input_str.split("-")

for ascii_code in ascii_list:
    print(chr(int(ascii_code)), end="")
 
 
print()