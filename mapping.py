import re

def extSeq(name):
	iFile = open(name, "r")
	seq = {}
	header = ""
	for line in iFile:
		if re.match(">", line):
			header = line.strip(">\n")
		else:
			seq[header] = line.rstrip("\n")
	iFile.close()
	return seq

def findMax(d, l, u):
	if d >= l and d >= u and d > 0:
		return d, 0
	elif l > d and l > u and l > 0:
		return l, 1
	elif u > d and u > l and u > 0:
		return u, 2
	else:
		return 0, -1

def defMat(f, g):
	if f == g:
		return 1
	else:
		return -1

def alnSeq(ref, scf):
	matrix = [[0 for i in range((len(scf)/2)+1)] for i in range((len(ref)/2)+1)]
	traceback = [[0 for i in range((len(scf)/2))] for i in range((len(ref)/2))]
	msco = 0
	mi = 0
	mj = 0
	for i in range((len(ref)/2)+1):
		for j in range((len(scf)/2)+1):
			if i == 0:
				matrix[i][j] = 0
			else:
				if j == 0:
					matrix[i][j] = 0
				else:
					d = matrix[i-1][j-1] + defMat(ref[((i-1)*2):(((i-1)*2)+2)], scf[((j-1)*2):(((j-1)*2)+2)])
					l = matrix[i][j-1] - 1
					u = matrix[i-1][j] - 1
					matrix[i][j], traceback[i-1][j-1] = findMax(d, l, u)
					if matrix[i][j] > msco:
						msco = matrix[i][j]
						mi = i-1
						mj = j-1
	s = traceback[mi][mj]
	s1 = ""
	r2 = ""
	
	while s != -1:
		if s == 0:
			s1 += scf[(mj*2):((mj*2)+2)][::-1]
			r2 += ref[(mi*2):((mi*2)+2)][::-1]
			mi -= 1
			mj -= 1
		elif s == 1:
			s1 += scf[(mj*2):((mj*2)+2)][::-1]
			r2 += "--"
			mj -= 1
		elif s == 2:
			s1 += "--"
			r2 += ref[(mi*2):((mi*2)+2)][::-1]
			mi -= 1
		s = traceback[mi][mj]

	s1 = s1[::-1]
	r2 = r2[::-1]
	
	count = 0
	if re.search("ZZZZ", s1):
		ind = s1.find("ZZZZ")
		if not re.search("ZZZZ", r2[ind:ind+4]):
			count += 1
	if re.search("ZZZZ", r2):
		ind = r2.find("ZZZZ")
		if not re.search("ZZZZ", s1[ind:ind+4]):
			count -= 1
	
	return count


def main():
	refseq = extSeq("refseq.fa")
	queseq = extSeq("queseq.fa")
	scfseq = extSeq("scfseq.fa")
	refseq["refseq"] = re.sub("\|", "", refseq["refseq"])
	
	count = 6
	scflnt = 0
	for key in scfseq:
		scflnt += len(scfseq[key])
		count += alnSeq(refseq["refseq"], scfseq[key])
	
	cov = ((len(refseq["refseq"]) - scflnt) * 100) / float(len(refseq["refseq"]))

	print str(count) + "," + str(cov)
	
main()
