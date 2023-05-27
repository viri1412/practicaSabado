class perro:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def ladrar(self):
        print('Wooff!!!')

    def datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")    


nuevo_perro = perro('nina',2)      
nuevo_perro.datos()   
nuevo_perro.ladrar()

nuevo_perro2 = perro('perro2',10)      
nuevo_perro2.datos()   
nuevo_perro2.ladrar()