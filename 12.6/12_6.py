
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
b=0
url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('tr')
for tag in tags:
    words = tag.decode()
    words = words.rstrip()
    numbers = re.findall('>([0-9]+)<', words)
    if len(numbers) < 1:
        continue
    for i in numbers:
        x = int(i)
        b = b + x
print(b)
