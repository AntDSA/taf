### Exercices 2 :
## Question 1 : 
# 1. 2 vers le bas 
# 2. 
## Question 2 : 
# 4 1 1 3 1 1 = 11
# 4 1 1 2 1 1 = 10
# 4 1 0 2 1 1 = 9 
# 4 2 0 2 1 1 = 10 

# 4 1 1 2 5 1 = 14
# 4 1 0 2 5 1 = 13 
# 4 2 0 2 5 1 = 14
# 4 2 3 1 5 1 = 16

# 4 1 0 1 5 1 = 12
# 4 2 0 1 5 1 = 13

## Question 5 : 
T = [[4, 1, 1, 4], [2, 0, 2, 1], [3, 1, 5, 1]]
    
def somme_max (T, i, j):
    if i == 0 and j == 0 : 
        return T[0][0]
    if i == 0:
        return T[0][j] + somme_max(T, 0, j-1)
    if j == 0:
        return T[i][0] + somme_max(T, i-1, 0) 
    
    haut = somme_max(T, i - 1, j)
    gauche = somme_max(T, i, j - 1)
    if haut >= gauche:
        return T[i][j] + haut
    else:
        return T[i][j] + gauche

print(somme_max(T, 2,3))

