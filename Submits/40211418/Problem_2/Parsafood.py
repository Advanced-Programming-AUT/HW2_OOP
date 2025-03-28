from abc import ABC, abstractmethod

class Food(ABC):

    food_id = 1

    @abstractmethod
    def __init__(self):
        self.id = Food.food_id
        Food.food_id += 1
    
    @abstractmethod
    def calculate_price(self)-> float:
        ...

    @abstractmethod
    def __add__(self, x):
        ...

class Pizza(Food):
    
    def __init__(self, size, kind, additive=None):
        super().__init__()
        self.size = size
        self._kind = kind
        self._additive = additive

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value == 'Yes':
            self._size = value
        else:
            print('couldnt set')

    @property
    def kind(self):
        return self._kind
    
    @property
    def additive(self):
        return self._additive
    
    def calculate_price(self):
        pass
        

    def __add__(self, x):
        pass
pizza = Pizza('svjkhbshjk','fssvscv')