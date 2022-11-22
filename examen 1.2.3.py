import random

mytable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(mytable)-1):
    mytable[i] = random.randint(0, 100)

sauvegardeduscore = 0

print(mytable)
for n in range(len(mytable)-1):
    for i in range(len(mytable)-1):
        if(mytable[i] > mytable [i+1]):
            sauvegardeduscore = mytable[i]
            print (sauvegardeduscore) #pour afficher le parcours du tableau
            mytable[i] = mytable[i+1]
            mytable[i+1] = sauvegardeduscore

print(mytable)

#le tri à bulle est lent car le syteme analyse à chaque boucle le chiffre suivant du tableau et repére le plus grand chiffre 
# il doit ensuite recommencer une boucle pour analyser de nouveau le tableau pour trouvé le second plus grand chiffre et vice-versa