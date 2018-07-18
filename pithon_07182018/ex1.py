def num_seq(fasta_file):
	i = 0
	f = open(fasta_file)
	line = f.readline()
	while line != '':
		if line[0] == '>' or line[0] == ';':
			i = i + 1
		line = f.readline()
	f.close()
	print(i)