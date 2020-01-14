fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ('File cannot be opened', fname)
    quit()
count = 0
number = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        fl = line.find(':')
        fll = line[fl+1:]
        ffll = float(fll)
        number = number + ffll
avg = number / count
print('Average spam confidence:', avg)


