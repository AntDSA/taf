# n = 91
# e = 23

# message = [1, 4, 9, 2]

# def puissance_modulaire(m, e, n):
#     rep = 1
#     for i in range(e):
#         rep= (rep * m) % n
#     return rep

# message_chiffre = []

# for m in message:
#     c = puissance_modulaire(m, e, n)
#     message_chiffre.append(c)

# print("Message chiffré à envoyer :", message_chiffre)




p = 809
q = 787
e = 389
d = 76733

n = p * q
phi = (p - 1) * (q - 1)

while (e * d) % phi != 1:
    d += 1

def puissance_modulaire(a, exp, mod):
    resultat = 1
    for i in range(exp):
        resultat = (resultat * a) % mod
    return resultat

print("Clé publique  :", (n, e))
print("Clé privée    :", (n, d))

message_chiffre = [1, 154154, 363550, 154154]
message_dechiffre = []

for c in message_chiffre:
    m = puissance_modulaire(c, d, n)
    message_dechiffre.append(m)


print("Message chiffré reçu :", message_chiffre)
print("Message déchiffré    :", message_dechiffre)



for i in range(2, n):
    if n % i == 0:
        p = i
        q = n // i
        break

print("p trouvé :", p)
print("q trouvé :", q)