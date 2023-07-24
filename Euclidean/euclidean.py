print("euclidean")

f = open("input.txt")
pairs = f.read()
f.close
ans = open("answer.txt","w")
ans.write("The answers from points given from 'ed.txt'.\n")
ans.write("['p1','p2']\t-\teuclidean distance\n")

pair = pairs.split('\n')
pair.pop()
pair.pop()

def edist(p1,p2):
	xv = int(p2[0]) - int(p1[0])
	yv = int(p2[-1]) - int(p1[-1])
	esum = (xv ** 2) + (yv ** 2)
	dist = esum ** (1/2)
	return dist

for i in pair:
	points = i.split(' ')
	print(points, end='\t- ')
	edis = edist(points[0],points[1])
	edis = round(edis,4)
	stri = str(points) + '\t-\t' + str(edis) + '\n'
	ans.write(stri)
	print(edis)

ans.close()
