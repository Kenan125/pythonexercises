import re
ftext = input("Please enter text file name:")
fh = open(ftext)
cnum = list()
newlist = list()
sum = 0
for line in fh:
    line = line.rstrip()
    y = re.findall("[0-9]+", line)
    if len(y)> 0:
        cnum.append(y)

for sublist in cnum:
    for item in sublist:
        newlist.append(item)
for item in newlist:
    sum = sum + int(item)
print(sum)





