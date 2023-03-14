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
        if rad <= 0:
            raise ValueError("El radio no puede ser menor o igual a cero.")
        self._rad = rad

    def getArea(self):
        # Area = pi x r^2
        return 3.14159 * (self._rad ** 2)
    
    def getPerimetro(self):
        # Perimetro = 2 x pi x r
        return 2 * 3.14159 * self._radio