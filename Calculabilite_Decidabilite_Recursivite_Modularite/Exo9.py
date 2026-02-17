## Exo 6 :
# def serie (n,a,b):
#     if n == 0 : 
#         return a 
#     elif n == 1: 
#         return b 
#     else :
#         rep = 3*serie(n-1, a, b)+2*serie(n-2, a, b)+5
#         return rep

# rep = serie(5,1,2)
# print(rep)

## Exo 7 :
# from turtle import *

# def koch (n, longeur): 
#     if n == 0: 
#         forward(longeur)
#     else: 
#         longeur /= 3
#         koch(n-1, longeur)
#         left(60)
#         koch(n-1, longeur)
#         right(120)
#         koch(n-1, longeur)
#         left(60)
#         koch(n-1, longeur)
# window = Screen()
# t = Turtle()
# t.speed(0)
# t.pendown()


# koch(5, 900)

# done()

## Exo 8 : 
# from turtle import * 
# couleurs = ["blue", "green", "yellow", "orange", "red", "purple"] 
# bgcolor("black") 

# def dessin(i): 
#     if i < 180: 
#         color(couleurs[i%6]) 
#         forward(i) 
#         right(59)
#         dessin(i+1)

# dessin(0)
# mainloop()

# Exo 9: 
# import Stats

# test = [1, 2, 3, 4]

# print(Stats.moyenne(test))
# print(Stats.somme(test))

# # Exo 10 : 
# from turtle import *
# import figures as f 
# up()
# goto(50, -60)
# down()
# f.rectangle(100, 75, 'red')

# up()
# goto(-80, -20)
# down()
# f.triangle(85, 'blue')

# up()
# goto(20, 60)
# down()
# f.cercle(60, 'green')

# Exo 12 : 
