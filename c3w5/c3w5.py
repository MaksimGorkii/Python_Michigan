import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
print('Retrieving: ', url)
tree = ET.fromstring(html)
print(len(html), 'characters')

counts = tree.findall('comments/comment/count')
num = 0
sum = 0
for count in counts:
    #print(count)
    num = num + 1
    dig = int(count.text)
    sum = sum + dig
print('Count: ',num)
print('Sum:', sum)

