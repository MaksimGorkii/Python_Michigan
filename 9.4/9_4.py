fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
counts = dict()
email = list()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    email1 = email.split()
    for word in email1:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)










