from operator import itemgetter

f = open('part-00000')
i=0
lineset = []

for line in f:
	lines = []
	line = line.strip()
	line1,line2 = line.split('\t')
	lines.append(line1)
	lines.append(int(line2))
	lineset.append(lines)


lineset.sort(key=itemgetter(1),reverse = True)

while(i < 10):
	print (lineset[i])
	i +=1