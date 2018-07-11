#3. Demonstrate inheritance by importing your class "Organism" from problem 2. 
#Use it to create a new class called "LongOrganism" which inherits "Organism" and 
#modifies it by adding any other attributes that may be significant about an organism 
#(ie ploidy, genome size, region). Write new methods which allow a user to see these values in informative ways.

class LongOrganism(Organism):
	def __init__(self, kingdom, phylum, Class, order, family, genus, species, name, ploidy, genome):
		Organism.__init__(self, kingdom, phylum, Class, order, family, genus, species, name)
		self.ploidy = ploidy
		self.genome = genome

	def description(self):
		print(
			'Kingdom: ', self.kingdom, '\n',
			'Phylum: ', self.phylum, '\n',
			'Class:' , self.Class, '\n',
			'Order: ', self.order, '\n',
			'Family: ', self.family, '\n',
			'Genus:' , self.genus, '\n',
			'Species: ', self.species, '\n',
			'Common name: ', self.name, '\n',
			'Ploidy: ', self.ploidy, '\n',
			'Genome size: ', self.genome)

At = LongOrganism('Plantae', 'Magnoliophyta', 'Pentapetalae', 'Brassicales', 'Brassicaceae', 'Arabidopsis', 'thaliana', 'thale cress', '2n', 
	'135 Mbp')

print(At.description())