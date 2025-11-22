class birra:
    def __init__(self, name, color, notas, ph, abv, ibu, stock, ratings):
        self.color = color
        self.notas = notas
        self.ph = ph
        self.abv = abv
        self.ibu = ibu
        self.stock = stock
        self.ratings = ratings
        self.name = name

    def pedir(self):
        if self.stock > 0:
            self.stock -=1
            print(f"Usted ha consumido una {self.name}")
        else:
            print(f"Lo sentimos pero no hay {self.name}")

    def catalogo(self, lista_cervezas):
        for cerveza in lista_cervezas:
            print(f'{cerveza.name} | Color: {cerveza.color}, Notas: {cerveza.notas}, PH: {cerveza.ph}, abv:  {cerveza.abv}, Stock: {cerveza.stock} y Rating: {cerveza.ratings}')
        
