import json
import urllib

url = raw_input('Enter url: ')
data = urllib.urlopen(url).read()

info = json.loads(data)
#print 'User count:', len(info)

#print json.dumps(info, indent = 2)
sum = 0
for i in range(len(info['comments'])):
    sum = sum + int(info['comments'][i]['count'])

print sum

