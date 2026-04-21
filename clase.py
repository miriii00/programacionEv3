class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__peso = peso
    def get_nombre(self):
        return self.__nombre

    def get_especie(self):
        return self.__especie

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso
    
    def set_nombre(self,nombre):
        self.__nombre=nombre

    def set_especie(self,especie):
        self.__especie=especie

    def set_edad(self,edad):
        self.__edad=edad

    def set_peso(self,peso):
        self.__peso=peso
    
    def es_adulta(self):
     if self.__edad>=2:
        return "La mascota es adulta"
     else:
        return "La mascota es joven"


