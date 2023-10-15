class Asignar: 
    def __init__(self, request):
        self.request = request 
        self.session = request.session
        asignar = self.session.get("Asignar")

        if not asignar:
            asignar = self.session["asignar"] = {}
        else:
            self.asignar = asignar 

    def agregar(self, seleccion): #para agregar
        if(str(seleccion.id) not in self.asignar.keys()):
            self.asignar[seleccion.id] = {
                "seleccion_id":seleccion.id,
                "nombre":seleccion.nombre,
                "precio":seleccion.precio,
                "cantidad": 1
            }
        else:
            for key, value in self.asignar.items():
                if key == str(seleccion.id):
                    value["cantidad"] = value["cantidad"]+1
                    break 
                
        self.guardar_asignar()

    def guardar_asignar(self):#guardar si sale o cambia de pestaña
        self.session["asignar"] = self.carro
        self.session.modified = True

    def eliminar(self, seleccion):
        seleccion.id = str(seleccion.id)
        if seleccion.id in self.asignar:
            del self.asignar[seleccion.id]
            self.guardar_asignar()

    def restar_seleccion(self, seleccion):
        for key, value in self.asignar.items():
            if key == str(seleccion.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.eliminar(seleccion)
                break        
        self.guardar_asignar()

    def limpiar_asignar(self):
        self.session["asignar"] = {}
        self.session.modified = True