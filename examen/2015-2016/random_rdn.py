01 for tx in tx_len:
02 tx_len = dict()
03     if tx_len[tx] > 200:
04     else:
05     ex_size = end - start
06     line = line.rstrip("\n")
07     cols = line.split("\t")
08     tx = cols[4]
09         tx_len[tx] = ex_size
010     start = int(cols[1])
011         tx_len[tx] =  tx_len[tx] + ex_size
012     if not tx in tx_len:
013 for line in f:
014 f = open("exons.txt")
015     end = int(cols[2])
016         print(tx + "\t" + str(tx_len[tx]))
