class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True
    def information(self):
        return "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\n"\
               "DNA: {}\nOrigin: {}\nCarbon Based: {}"\
               .format(self.name, self.species, self.legs,\
                       self.arms, self.dna, self.origin,\
                       self.carbon_based)

class Human(Organism): # use another class as parent
    name = "Joe"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"
    def ingenuity(self):
        return "Does some homosapien stuff\n"

class Dog(Organism):
    name = "Harley"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"
    def wag(self):
        return "We prefer dogs that wag.\n"

class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    orign = "Mars"
    def replication(self):
        return "The cells divide into multiple organisms.\n"
    
    

if __name__ == "__main__":
    human = Human()
    print( human.information() )
    print( human.ingenuity() )

    dog = Dog()
    print( dog.information() )
    print( dog.wag() )

    bacteria = Bacterium()
    print( bacteria.information() )
    print( bacteria.replication() )
