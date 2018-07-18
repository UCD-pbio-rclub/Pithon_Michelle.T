def num_seq(fastq_file):
	i = 0
	f = open(fastq_file)
	line = f.readline()
	while line != '':
		if line[0] == '@':
			i = i + 1
		line = f.readline()
	f.close()
	print(i)