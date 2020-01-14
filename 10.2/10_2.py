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
    time = words[5]
    hour = time[:2]
    time1 = hour.split()
    for word in time1:
        counts[word] = counts.get(word,0) + 1


    num = list()
    for k, v in counts.items():
        num.append((k,v))
        num = sorted(num)
for k, v in num:
    print(k,v)

