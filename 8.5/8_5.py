fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
email = list()
words = list()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    count = count +1
    print(email)
print('There were', count, 'lines in the file with From as the first word')


