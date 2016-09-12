#10.2 Write a program to read through the mbox-short.txt and figure out the 
#distribution by hour of the day for each of the messages. You can pull the 
#hour out from the 'From ' line by finding the time and then splitting the 
#string a second time using a colon.
#                  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hrs_dict = dict()

for line in handle:
    words = line.split()
    if "From" in words:
        time = words[5]
        hrs = time[0:2]
        
        if hrs_dict.has_key(hrs):
            hrs_dict[hrs] = hrs_dict[hrs] + 1
        else:
            hrs_dict.setdefault(hrs, 1)
            
hrs_tuple = hrs_dict.items()
hrs_tuple.sort()

for tup in hrs_tuple:
    print tup[0], str(tup[1])
