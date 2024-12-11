from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def add_ship(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def delete_ship(self):
        self.name = None
        self.length = None
        self.width = None

    def update_ship(self, name=None, length=None, width=None):
        if name:
            self.name = name
        if length:
            self.length = length
        if width:
            self.width = width        

    @abstractmethod
    def get_info(self):
        pass

    def get_info(self):
        return f"Ship name: {self.name}, Length: {self.length}, Width: {self.width}"

class Frigate(Ship):
    def __init__(self, name, length, width, missile_capacity):
        super().__init__(name, length, width)
        self.missile_capacity = missile_capacity    


    def add_frigate(self, name, length, width, missile_capacity):
        self.add_ship(name, length, width)
        self.missile_capacity = missile_capacity

    def delete_frigate(self):
        self.delete_ship()
        self.missile_capacity = None

    def update_frgate(self, name=None, length=None, width=None, missile_capacity=None):
        self.update_ship(name, length, width)
        if missile_capacity:
            self.missile_capacity = missile_capacity    

    def get_info(self):
        return f"Frigate: {self.name}, Length: {self.length}, Width: {self.width}, Missile Capacity: {self.missile_capacity}"
    

class Destroyer(Ship):
    def __init__(self, name, length, width, gun_caliber):
        super().__init__(name, length, width)
        self.gun_caliber = gun_caliber

    def add_destroyer(self, name, length, width, gun_caliber): 
        self.add_ship(name, length, width)
        self.gun_caliber = gun_caliber

    def delete_destroyer(self):
        self.delete_ship()
        self.gun_caliber = None

    def update_destroyer(self, name=None, length=None, width=None, gun_caliber=None):
        self.update_ship(name, length, width)
        if gun_caliber:
            self.gun_caliber = gun_caliber        

    def get_info(self):
        return f"Destroyer: {self.name}, Length: {self.length}, Width: {self.width}, Gun Caliber: {self.gun_caliber}"

class Cruiser(Ship):
    def __init__(self, name, length, width, missile_capacity, gun_caliber):
        super().__init__(name, length, width)
        self.missile_capacity = missile_capacity
        self.gun_caliber = gun_caliber

    def add_cruiser(self, name, length, width, missile_capacity, gun_caliber):
        self.add_ship(name, length, width)
        self.missile_capacity = missile_capacity
        self.gun_caliber = gun_caliber

    def delete_cruiser(self):
        self.delete_ship()
        self.missile_capacity = None
        self.gun_caliber = None

    def update_cruiser(self, name=None, length=None, width=None, missile_capacity=None, gun_caliber=None):
        self.update_ship(name, length, width)
        if missile_capacity:
            self.missile_capacity = missile_capacity
        if gun_caliber:
            self.gun_caliber = gun_caliber        

    def get_info(self):
        return f"Cruiser: {self.name}, Length: {self.length}, Width: {self.width}, Missile Capacity: {self.missile_capacity}, Gun Caliber: {self.gun_caliber}"


ship = Ship("Ship", 100, 20)
print(ship.get_info())

frigate = Frigate("Frigate", 50, 10, 100)
print(frigate.get_info())

destroyer = Destroyer("Destroyer", 70, 15, 200)
print(destroyer.get_info())

cruiser = Cruiser("Cruiser", 80, 18, 150, 250)
print(cruiser.get_info())