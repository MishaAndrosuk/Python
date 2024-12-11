class Airplane:
    def __init__(self, model, max_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.passengers = 0

    def __eq__(self, other):
        return isinstance(other, Airplane) and self.model == other.model

    def __add__(self, num_passengers):
        if self.passengers + num_passengers <= self.max_passengers:
            self.passengers += num_passengers
        else:
            print("Exceeded maximum passenger capacity")

    def __sub__(self, num_passengers):
        if self.passengers - num_passengers >= 0:
            self.passengers -= num_passengers
        else:   
            print("Cannot have negative number of passengers")

    def __iadd__(self, num_passengers):
        self.__add__(num_passengers)
        return self

    def __isub__(self, num_passengers):
        self.__sub__(num_passengers)
        return self

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __int__(self) -> int:
        return self.passengers

    def __str__(self) -> str:
        return self.model



airplane1 = Airplane("Boeing 747", 400)

airplane2 = Airplane("Boeing 723", 400)

print("Airplane1 > Airplane2:", airplane1 > airplane2)
print("Airplane1 < Airplane2:", airplane1 < airplane2)
print("Airplane1 >= Airplane2:", airplane1 >= airplane2)
print("Airplane1 <= Airplane2:", airplane1 <= airplane2)
print("Airplane1 == Airplane1:", airplane1 == airplane1)
