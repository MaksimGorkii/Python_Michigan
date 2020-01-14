import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
print("Retrieving ", url)
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
num = 0

for comment in json_obj["comments"]:
    sum = sum + int(comment["count"])
    num = num + 1

print('Count:', num)
print('Sum:', sum)
