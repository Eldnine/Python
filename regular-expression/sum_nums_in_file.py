import re

filename = raw_input("Enter file name: ")
if len(filename) < 1:
    filename = "default_file.txt"
    
x = open(filename).read()
nums = re.findall('[0-9]+', x)

sum = 0
for num in nums:
    sum = sum + int(num)

print sum
