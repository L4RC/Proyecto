class Carro: 
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro: 
            carro = self.session["carro"]={}
#        else:
        self.carro = carro

    def agregar(self,Curso):
        if(str(Curso.id) not in self.carro.keys()):
            self.carro[Curso.id] = {
                "Curso_id":Curso.id,
            }
        else:
            for key, value in self.carro.items():
                if key == str(Curso.id):
                #    value["cantidad"] = value["cantidad"+1]
                #    print("Estos son tus cursos")
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True

    def eliminar(self, Curso):
        Curso.id = str(Curso.id)
        if Curso.id in self.carro:
            del self.carro[Curso.id]
            self.guardar_carro()
"""    
from django.db import connection

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.obtener_carro()

    def obtener_carro(self):
        # Utiliza la conexión a la base de datos configurada en settings.py
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS carro (Curso_id TEXT PRIMARY KEY)")
            cursor.execute("SELECT Curso_id FROM carro")
            rows = cursor.fetchall()

        # Procesa los resultados y crea el diccionario del carro
        carro = {}
        for row in rows:
            carro[row[0]] = {"Curso_id": row[0]}

        return carro

    def agregar(self, Curso):
        if str(Curso.id) not in self.carro:
            self.carro[str(Curso.id)] = {"Curso_id": str(Curso.id)}
            self.guardar_carro()

    def guardar_carro(self):
        # Utiliza la conexión a la base de datos configurada en settings.py
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS carro (Curso_id TEXT PRIMARY KEY)")
            for Curso_id, data in self.carro.items():
                cursor.execute("INSERT INTO carro (Curso_id) VALUES (%s) ON CONFLICT (Curso_id) DO NOTHING", (Curso_id,))

    def eliminar(self, Curso):
        Curso_id = str(Curso.id)
        if Curso_id in self.carro:
            del self.carro[Curso_id]
            self.guardar_carro()
"""