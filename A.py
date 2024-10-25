
class A:

    def __init__(self, a1: int, a2: float):
        self.a1 = a1
        self.a2 = a2

    @property
    def a1(self) -> int:
        return self.__a1
    
    @property
    def a2(self) -> float:
        return self.__a2
    
    @a1.setter
    def a1(self, value: int) -> None:
        if type(value) == int:
            self.__a1 = value

    @a2.setter
    def a2(self, value: float) -> None:
        if type(value) == float:
            self.__a2 = value

    def ma1(self) -> None:
        print("Método MA1")

    def ma2(self) -> None:
        print("Método MA2")