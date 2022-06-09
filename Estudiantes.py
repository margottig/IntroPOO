#Esto es un comentario

estudiantes = [
    {
    'id':1,
    'nombre':"Mario",
    'apellido':"Bros",
    'calificaciones':10
    },
    {
    'id':2,
    'nombre':"Sonic",
    'apellido':"Sega",
    'calificaciones':9},
    {
    'id':3,
    'nombre':"Rick",
    'apellido':"Morty",
    'calificaciones':8},
    
]

#Crear una instancia de clase equivale a crear objeto

class Estudiante:
    
    listaEstudiantes = []
    numeroTotalEstudiantes = 0

    # def __init__(self, nombre, apellido,  calificaciones, id=0 ): #/Inicializador aka Constructor
    #     #Atributos
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.id = id
    #     self.calificaciones = calificaciones
    #     Estudiante.listaEstudiantes.append(self)

    def __init__(self, data):
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.id = data['id']
        self.calificaciones = data['calificaciones']
        Estudiante.listaEstudiantes.append(self)
        Estudiante.numeroTotalEstudiantes += 1

    @classmethod
    def totalEstudiantes(cls):
        print("El total de estudiantes es:", cls.numeroTotalEstudiantes )


    def nombreEstudiante(self):
        print(f'El nombre del estudiantes es:{self.nombre}')
        return self
        
    
    def apellidoEstudiante(self):
        print(f'El apellido del estudiantes es:{self.apellido}')
        return self
    
    @staticmethod
    def imprimirID(identificador):
        print(identificador)



# estudiante_1 = Estudiante("Yoshi", "Tortuga", 10, 12345)
# estudiante_2 = Estudiante("King", "Kong", 9, 12346)

estudiante_3 = {
    'id':12347,
    'nombre':"Rick",
    'apellido':"Morty",
    'calificaciones':8
    }

resultadoEstudiante_3 = Estudiante(estudiante_3)


# print(estudiante_1.__dict__, estudiante_2.__dict__)
# print(Estudiante.listaEstudiantes[1].nombre)
print(resultadoEstudiante_3.__dict__)


for estudiante in estudiantes:
    Estudiante(estudiante)

print(Estudiante.listaEstudiantes)

print("/*"*10)
# print(Estudiante.totalEstudiantes())
print(Estudiante.listaEstudiantes[2].nombreEstudiante().apellidoEstudiante().imprimirID(1))

print("Numero total de estudiantes: ", Estudiante.numeroTotalEstudiantes)    
