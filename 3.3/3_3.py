sc = input ("Enter the score: ")
try:
    score = float(sc)
except:
    print ("Enter digits")
    quit()
if score > 1.0 or score < 0.0:
    print("The value is out of range")
    quit()
elif score >= 0.9:
    lscore = "A"
elif score >= 0.8:
    lscore = "B"
elif score >= 0.7:
    lscore = "C"
elif score >= 0.6:
    lscore = "D"
else:
    lscore = "F"
print(lscore)
