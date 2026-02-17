# !!! p, q, e, d pas trop grands sinon temps calcul trop long

p = int(input("p ?"))
q = int(input("q ?"))
n , f = ...     # f joue le rôle de phi(n)
print('n:',n,' f:',f)

e = f   # initialisation par défaut
while e >= f:   # on oblige l'utilisateur à choisir e < f
    e = int(input("e 1er avec f ?"))

# calcul de la clé privée :
d = 1
while ...
    d += 1
print('d',d)

# Vérification :
m1 = int(input("m (inférieur à n) ?"))  # message d'origine
c = ...     # message chiffré par clé publique
m2 = ...    # message déchiffré par clé privée
print(c, m2)    # on doit avoir m2 = m1, message d'origine
