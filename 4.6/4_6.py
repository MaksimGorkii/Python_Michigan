hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("enter digital value")
    quit()
def computepay(h,r):
    if h > 40:
        ot = (h-40) * 1.5 *r
        h=40
    else:
        ot=0
    return h * r + ot
print(computepay(h,r))
