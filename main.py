class birra:
    def __init__(self, name, color, notas, abv, stock, ratings, strong):
        self.color = color
        self.notas = notas
        self.abv = abv
        self.stock = stock
        self.ratings = ratings
        self.name = name
        self.strong = strong
    def pedir(self):
        if self.stock > 0:
            self.stock -=1
            print(f"Usted ha consumido una {self.name}")
        else:
            print(f"Lo sentimos pero no hay {self.name}")

    def catalogo(self, lista_cervezas):
        for cerveza in lista_cervezas:
            print(f'{cerveza.name} | Color: {cerveza.color}, Notas: {cerveza.notas}, abv:  {cerveza.abv}, Stock: {cerveza.stock} y Rating: {cerveza.ratings}')

    def rating(self):
        while True:
            rating_usuario = int(input("Que calificacion le pone a este birra?: "))
            if rating_usuario in range(0,6):
                self.ratings.append(rating_usuario)
                print(f"Gracias por su calificacion")
                break
            else:
                print('Por favor digite un numero del 0 al 5.')       
    
    def average(self):
        if  self.ratings:
            return sum(self.ratings)/len(self.ratings)
        return 0

    def reponer_stock(self):
        solicitud = int(input("Cuantas cervezas quiere reponer al inventario"))
        self.stock += solicitud
        print(f"Ahora hay {self.stock}, de {self.name}")

    def es_fuerte(self):
        return self.abv >= 6.5

b1 = birra("Madame Raccoon", "Ebano", "Whiskey y Madera", 7.0, 12, [],False)
b2 = birra("Pajaro Azul", "clara", "Albahaca", 3.8, 25, [],False)
b3 = birra("Mango", "Rubia", "Tropicales", 4.0, 50, [],False)
b4 = birra("Honey", "Clara", "Ligeras a miel", 4.0, 30, [],False)
b5 = birra("Golden", "Dorado", "frutos tropicales", 5.0, 20, [],False)
b6 = birra("Bad Raccoon", "ambar", "lupulos fuertes", 6.0, 50, [],False)
b7 = birra("Porter", "Oscura", "Chocolate y cafe", 6.0, 11, [],False)

lista_cervezas = [b1, b2, b3, b4, b5, b6, b7]

while True:
    print(
        "1. Menu\n2.Pedir Cerveza\n3.Hacer critica.\n4.ver el promedio de rating de una cerveza\n5.Hacer reestock\n6.salir."
    )
