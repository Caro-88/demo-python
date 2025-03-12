from paquete1.moduloA import A

class B:
    
    def captura_mensaje(self):
        obj_a=A()
        return f"Hola desde la Clase B: {obj_a.saludo()}"
        
print(f"Hola soy el moduloB mi __name__ es {__name__}")
#El que se está ejecutando aparece con name main, el que se importa aparece con name nombre del archivo.
#Se muestran las dos formas de importar: en moduloA y moduloB