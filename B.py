
class B:

    def __init__(self, b1: int, b2: float):
        self.__b1 = b1
        self.__b2 = b2

    @property
    def b1(self) -> int:
        return self.__b1
    
    @property
    def b2(self) -> float:
        return self.__b2
    
    @b1.setter
    def b1(self, value: int) -> None:
        if type(value) == int:
            self.__b1 = value

    @b2.setter
    def b2(self, value: float) -> None:
        if type(value) == float:
            self.__b2 = value

    def mb1(self) -> None:
        print("Método MB1")

    def mb2(self) -> None:
        print("Método MB2")

    def mb3(self) -> None:
        print("Método MB3")