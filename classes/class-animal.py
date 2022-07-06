class Animal:
    """Animal class"""
    def __init__(self, species, age):
        self._species = species
        self._age = age

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age
    
    @species.setter
    def species(self, new_species):
        self._species = new_species

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def move(self):
        print('Moving')
    
    def eat(self):
        print('Eating')
    
    def die(self):
        print('Dying')