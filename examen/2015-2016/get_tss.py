f = open("exons.txt")
tx_5p = dict()

for line in f:
	line = line.rstrip("\n")
	cols = line.split("\t")
	tx = cols[4]
	start = int(cols[1])
	end = int(cols[2])
	strand = cols[5]
	if strand == "+":
		if tx not in tx_5p:
			tx_5p[tx] = start
		else:
			if start < tx_5p[tx]:
				tx_5p[tx] = start
	else:
		if tx not in tx_5p:
			tx_5p[tx] = end
		else:
			if end > tx_5p[tx]:
				tx_5p[tx] = end
for tx in tx_5p:
	print(tx + "\t" + str(tx_5p[tx]))
