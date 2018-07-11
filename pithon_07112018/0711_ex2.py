#07/10/2018 Exercise 2
#2. Write a class called "Organism". Have the class initialize with the organism's complete taxonomic lineage (KPCOFGS) and common name. Write methods which allow a user to see these values in informative ways.

class Organism:
	def __init__(self, kingdom, phylum, Class, order, family, genus, species, name):
		self.kingdom = kingdom
		self.phylum = phylum
		self.Class = Class
		self.order = order
		self.family = family
		self.genus = genus
		self.species = species
		self.name = name

	def description(self):
		print(
			'Kingdom: ', self.kingdom, '\n',
			'Phylum: ', self.phylum, '\n',
			'Class:' , self.Class, '\n',
			'Order: ', self.order, '\n',
			'Family: ', self.family, '\n',
			'Genus:' , self.genus, '\n',
			'Species: ', self.species, '\n',
			'Common name: ', self.name)

At = Organism('Plantae', 'Magnoliophyta', 'Pentapetalae', 'Brassicales', 'Brassicaceae', 'Arabidopsis', 'thaliana', 'thale cress')

print(At.description())