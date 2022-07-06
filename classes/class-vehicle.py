class Vehicle:
    """Vehicle class"""
    def __init__(self, year, color, numberofWheels, capacity):
        self._year = year
        self._color = color
        self._numberofWheels = numberofWheels
        self._capacity = capacity

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color
    
    @property
    def numberofWheels(self):
        return self._numberofWheels

    @property
    def capacity(self):
        return self._capacity

    @year.setter
    def year(self, new_year):
        self. _year = new_year

    @color.setter
    def author(self, new_author):
        self._color = new_color

    @numberofWheels.setter
    def numberofWheels(self, new_numberofWheels):
        self._numberofWheels = new_numberofWheels

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity

    def start(self):
        print('Starting')
    
    def stop(self):
        print('Stopping')
    
    def move(self):
        print('Moving')