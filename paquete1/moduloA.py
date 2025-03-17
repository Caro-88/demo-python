from . import version 
print(f"Version del paquete: {version}")

print(f"Hola soy el moduloA, mi __name__ es {__name__}")
class A:
    def saludo(self):
        return "Hola desde la Clase A"