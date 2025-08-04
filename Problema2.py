class SistemaClientes:
    def __init__(self, max_size=None):
        self.queue = []
        self.max_size = max_size

    def addCustomer(self, name):
        if self.max_size is not None and len(self.queue) >= self.max_size:
            print(f"No se puede agregar {name}, la cola esta llena")
        else:
            self.queue.append(name)
            print(f"Cliente agregado: {name}")

    def serveCustomer(self):
        if not self.queue:
            print("No hay clientes para atender")
        else:
            served = self.queue.pop(0)
            print(f"Cliente atendido: {served}")

system = SistemaClientes(max_size=3)

system.addCustomer("Juan")
system.addCustomer("Sebastian")
system.addCustomer("Sofia")
system.addCustomer("Pedro")  
system.serveCustomer()
system.serveCustomer()
system.serveCustomer()
system.serveCustomer()      
