import urllib.request

def num_seq(url_file):
	f = urllib.request.urlopen(url_file)
	fasta = f.read().decode('utf-8', 'ignore')
	fasta = fasta.splitlines()
	i = 0
	for line in fasta:
		if line[0] == '>' or line[0] == ';' or line[0] == '@':
			i = i + 1
	f.close()
	print(i)
