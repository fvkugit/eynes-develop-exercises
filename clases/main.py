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

class Circulo:
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
        return 3.14159 * (self._rad ** 2)
    
    def getPerimetro(self):
        """
            Calculate circle perimeter.
            
            Returns:
                float: Circle perimeter.
        """
        # Perimetro = 2 x pi x r
        return 2 * 3.14159 * self._rad
    
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
    
circ = Circulo(5)
print(circ)
circ.radio = 3
print(circ)

circ2 = circ*10
print(circ2)
print(circ2.getPerimetro())