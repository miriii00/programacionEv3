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
