import itertools, random, re

initspace = [''.join(i) for i in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=2)]
initspace.remove("ZZ")

""" Simulating Reference Genome """
refseq = ">refseq\n|ZZ"
strref = ""
rlnt = 300
rcno = 6
rclnt = 50
for i in range(rcno):
	for j in range(rclnt):
		letter = random.choice(initspace)
		initspace.remove(letter)
		refseq += letter
		strref += letter
	refseq += "ZZ|ZZ"
refseq = refseq.rstrip("ZZ")

""" Simulating Query Genome """
qcno = random.randrange(4, 9)
strque = strref
for i in range(100):
	j = random.randrange(100)
	#Reduce Coverage
	if j in range(10, 15):
		pos = random.randrange(0, len(strque), 2)
		strque = strque[:pos] + strque[(pos + 2):]
	#Insert Mutations
	elif j in range(40, 45):
		letter = random.choice(initspace)
		initspace.remove(letter)
		pos = random.randrange(0, len(strque), 2)
		strque = strque[:pos] + letter + strque[pos:]
	#Simulate Transposition
	elif j in range(50, 55):
		pos = random.randrange(0, len(strque), 2)
		letter = strque[pos:(pos + 2)]
		strque = strque[:pos] + strque[(pos + 2):]
		pos = random.randrange(0, len(strque), 2)
		strque = strque[:pos] + letter + strque[pos:]
	#Invert marker blocks
	elif j in range(60, 65):
		lnt = random.randrange(10, 20, 2)
		pos = random.randrange(0, len(strque), 2)
		letter = strque[pos:(pos + lnt)]
		new = letter[::-1]
		strque.replace(letter, new)
queseq = ">queseq\n|ZZ"
qclnt = len(strque) / qcno
start = 0
end = qclnt
for end in range(qclnt, len(strque), qclnt):
	queseq += strque[start:end] + "ZZ|ZZ"
	start = end
queseq = queseq[:len(queseq)-2]
strque = re.sub("\|", "", queseq.split("\n")[1])

""" Simulating fragments """
frag = [strque]
scaf = []
scno = random.randrange(20, 26)
pos = 0
temp = ""
while len(scaf) < scno:
	chk = 0
	flnt = random.randrange(10, 41, 2)
	for item in frag:
		if flnt <= len(item):
			pos = random.randrange(0, len(item), 2)
			while (pos + flnt) > len(item):
				pos = random.randrange(0, len(item), 2)
			temp = item[pos:(pos + flnt)]
			scaf.append(temp)
			frag.append(item[:pos])
			frag.append(item[(pos + flnt):])
			frag.remove(item)
			break
	for item in frag:
		if len(item) >= 10:
			chk = 1
			break
	if chk == 0:
		break

count = 1
scfseq = ""
for item in scaf:
	scfseq += ">scaf" + str(count) + "\n" + item + "\n"
	count += 1

oFile = open("refseq.fa", "w")
oFile.write(refseq)
oFile.close()

oFile = open("queseq.fa", "w")
oFile.write(queseq)
oFile.close()

oFile = open("scfseq.fa", "w")
oFile.write(scfseq)
oFile.close()
