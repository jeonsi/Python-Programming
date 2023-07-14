class Cone:
    def __init__(self, radius = 20, height = 30):
        self.r = radius
        self.h = height

    def get_vol(self):
        return 1/3 * 3.14 * self.r ** 2 * self.h
    
    def get_surf(self):
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h

class pCone:
    def __init__(self, radius = 20, height = 30):
        if radius > 0 and height > 0:
            self.__r = radius
            self.__h = height

    def get_vol(self):
        return 1/3 * 3.14 * self.__r ** 2 * self.__h
    
    def get_surf(self):
        return 3.14 * self.__r ** 2 + 3.14 * self.__r * self.__h
    
    def get_radius(self):
        return self.__r
    
    def set_radius(self, radius):
        if radius > 0:
            self.__r = radius

cone = Cone()
cone.r = 1
print(cone.get_surf())

pcone = pCone()
pcone.__r = 1
print(pcone.get_surf())

pcone._pCone__r = 1
print(pcone.get_surf())
