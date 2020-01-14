import re
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
numlist = list()
a = 0
for line in fh:
    line = line.rstrip()
    numbers = re.findall('([0-9]+)', line)
    if len(numbers) < 1:
        continue
    for i in numbers:
        x = int(i)
        a = a + x
print(a)









