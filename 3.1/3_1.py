hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h<=40:
    gross = h * r
else :
    ot = h-40
    gross = 40 * r + (r * ot * 1.5)
print(gross)