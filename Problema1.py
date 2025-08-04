class NavegacionesWeb:
    def __init__(self):
        self.backStack = []
        self.forwardStack = []
        self.currentPage = None

    def loadPage(self, url):
        if self.currentPage:
            self.backStack.append(self.currentPage)
        self.currentPage = url
        self.forwardStack.clear()
        print(f"Cargando nueva pagina: {self.currentPage}")

    def goBack(self):
        if not self.backStack:
            print("No hay paginas anteriores...:(")
            return
        self.forwardStack.append(self.currentPage)
        self.currentPage = self.backStack.pop()
        print(f"Retrocediendo a: {self.currentPage}")

    def goForward(self):
        if not self.forwardStack:
            print("No hay paginas siguientes...:(")
            return
        self.backStack.append(self.currentPage)
        self.currentPage = self.forwardStack.pop()
        print(f"Avanzando a: {self.currentPage}")


navigator = NavegacionesWeb ()

navigator.loadPage("google.com")
navigator.loadPage("usergioarboleda.edu.co")
navigator.loadPage("teams.microsoft.com")
navigator.goBack()
navigator.goBack()
navigator.goBack()
navigator.goForward()
navigator.goForward()
navigator.loadPage("youtube.com")
navigator.goBack()   
navigator.goForward()  
navigator.goForward()  
