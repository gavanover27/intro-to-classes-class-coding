class Vehicle:
    """Vehicle class"""
    def __init__(self, make, model, year, color, miles, mpg):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._miles = miles
        self._mpg = mpg

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color
    
    @property
    def miles(self):
        return self._miles

    @property
    def mpg(self):
        return self._mpg

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @model.setter
    def model(self, new_model):
        self._model = new_model

    @year.setter
    def year(self, new_year):
        self. _year = new_year

    @color.setter
    def author(self, new_author):
        self._color = new_color

    @miles.setter
    def miles(self, new_miles):
        self._miles = new_miles

    @mpg.setter
    def mpg(self, new_mpg):
        self._mpg = new_mpg

    def start(self):
        print('Starting')
    
    def stop(self):
        print('Stopping')
    
    def move(self):
        print('Moving')