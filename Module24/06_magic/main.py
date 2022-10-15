class Water():
    name = 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Ground):
            return Dict()

class Air():
    name = 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Ground):
            return Dust()

class Fire():
    name = 'Fire'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()

class Storm():
    name = 'Storm'

class Ground():
    name = 'Ground'

class Lightning():
    name = 'Lightning'

class Dust():
    name = 'Dust'

class Lava():
    name = 'Lava'

class Steam():
    name = 'Steam'

class Dict():
    name = 'Dict'

a = Water()
b = Air()
c = a + b
print(c.name)