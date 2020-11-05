class Array:
    def __init__(self,tam):
        self.__info = [0 for x in range(tam) ]

    def get_item(self,posicion):
        dato = -1
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("error de posicion")
            dato = "error"
        return dato

    def set_item(self,indice,posicion):
        try:
            self.__info[posicion]
        except Exception as e:
            print("error de posicion")
    def get_length(self):
        return len(self.__info)

    def __iter__(self):
        return _IteradorArreglo(self.__info)

    def Clear(self,dato):
        self.__info=[dato for x in range(len(self.__info))]

class _IteradorArreglo():

    def __init__(self,arr):
        self.__arr = arr
        self.__indice = 0

    def __iter__(self):
        return self


    def __next__(self):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else :
            raise StopIteration


algo = Array(10)
print(algo.get_item(3656))
print(algo.get_item(3))
print(f"el arreglo tiene {algo.get_length()} elementos ")
algo.Clear(777)
print(algo.get_item(3))
print("---------------------")
for x in algo:
    print(x)
