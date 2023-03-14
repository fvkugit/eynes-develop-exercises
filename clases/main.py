"""
    Escribir una clase en python llamada círculo que contenga un radio, con un método que
    devuelva el área y otro que devuelva el perímetro del círculo.
    Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
    usuario e impidiendo la instanciación.
    Si printeamos el objeto creado debe mostrarse una representación amigable.
    El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
    mostrar un error y no permitir modificación.
    Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
    multiplicado por n. No permitir la multiplicación por números <= 0
"""
import doctest

class Circulo:
    """ 
        Circle representation class
        Test:
            >>> c = Circulo(5)
            >>> c.radio
            5
            >>> c.getArea()
            78.53975
            >>> c.getPerimetro()
            31.4159
            >>> c.radio = 0
            Traceback (most recent call last):
                ...
            ValueError: El radio no puede ser menor o igual a cero.
            >>> c.radio = 7
            >>> c.getArea()
            153.93791
            >>> c.getPerimetro()
            43.98226
            >>> c2 = c * 0
            Traceback (most recent call last):
                ...
            ValueError: No se puede multiplicar el circulo por cero o menos
            >>> c2 = c * 2
            >>> c2.radio
            14
            >>> c2.getArea()
            615.75164
            >>> c2.getPerimetro()
            87.96452
    """

    def __init__(self, rad):
        """ 
            Initialize Circulo object with specified radius.

            Args: 
                rad (float): Circle radius.

            Raise:
                ValueError: If radius is <= 0
        """
        if rad <= 0:
            raise ValueError("El radio no puede ser menor o igual a cero.")
        self._rad = rad

    def getArea(self):
        """
            Calculate circle area.
            
            Returns:
                float: Circle area.
        """
        # Area = pi x r^2
        return round(3.14159 * (self._rad ** 2), 5)
    
    def getPerimetro(self):
        """
            Calculate circle perimeter.
            
            Returns:
                float: Circle perimeter.
        """
        # Perimetro = 2 x pi x r
        return round(2 * 3.14159 * self._rad, 5)
    
    def __repr__(self):
        """
            String as the object representation

            Returns:
                str: Circle object string representation.
        """
        return f"¡Un circulo con un radio de {self._rad}!"
    
    @property
    def radio(self):
        """ 
            Circle object radius attribute getter

            Returns:
                float: Circle object radius value.
        """
        return self._rad
    @radio.setter
    def radio(self, val):
        """
            Circle object radius attribute setter

            Args:
                val (float): New value for circle object radius 

            Raise: 
                ValueError: If new value is <= 0
        """
        if val <= 0:
            raise ValueError("El radio no puede ser menor o igual a cero.")
        self._rad = val

    def __mul__(self, m):
        """
            Multiply circle object radius with other value

            Args:
                m (float): Value to multiply the radius of circle object.

            Returns:
                Circulo (object): New object with the result of the multiplication as radius.

            Raise: 
                ValueError: If multiply value is <= 0
        """
        if m <= 0:
            raise ValueError("No se puede multiplicar el circulo por cero o menos")
        return Circulo(self._rad * m)
    
if __name__ == "__main__":
    doctest.testmod()