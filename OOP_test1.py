class book(object):


    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def read(self, p):
        if p > self.pages:
            print("No hay suficientes paginas para leer")
        else:
            print("Reading...")

book1 = book("Libro1", "Juan", 200)
book1.read(300)

book2 = book("Libro2", "Maria", 150)
book2.read(150)