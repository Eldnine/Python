import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter url: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    tree = ET.fromstring(data)
    counts = tree.find('comments').findall('comment')
    Sum = 0
    for i in range(len(counts)):
        count = counts[i].find('count').text
        Sum = Sum + int(count)
    print Sum
