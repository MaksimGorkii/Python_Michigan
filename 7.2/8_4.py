fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
i = 0
lst = list()
for line in fh:
    line = line.rstrip()
    etc = line.split()
    if i != 0:
        i = i +1
    word = etc[i]
    if etc[i] in not in 








