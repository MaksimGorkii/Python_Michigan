fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for w in line:
        if w not in lst:
            lst.append(w)



words = lst
words.sort()
print(words)




