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
    
    def limpiar(self):
        self.session["carro"]={}
        self.session.modified = True