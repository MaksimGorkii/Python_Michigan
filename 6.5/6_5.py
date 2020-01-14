text = "X-DSPAM-Confidence:    0.8475";
nlet = text.find('0')
text1 = text[nlet:]
ftext1 = float(text1)
print(ftext1)