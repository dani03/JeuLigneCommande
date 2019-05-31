import random as rand
# pour importer juste la function randint sans le rand on l'importe comme si dessous
from random import randint
limit_nombre = input('entrez la limite a laquelle vous voulez trouvez un nombre ')
nombre_a_deviner = rand.randint(1, limit_nombre)
# print(nombre_a_deviner)
nombre_de_chance = input(' en combien d\'essai pouvez vous trouvez le nombre exact ? ')
nombre_essai = range(nombre_de_chance)
for i in nombre_essai:

    nombreUser = input("entrez votre nombre: essai {0} ".format(i+1))
    if(nombreUser > limit_nombre):
        print('choisissez un nombre entre 1 et {1}... vous avez gaspille votre essai {0} '.format(i+1, limit_nombre))
    elif nombre_a_deviner == nombreUser:
        print("bravo vous avez trouve le nombre exact en {0} essai(s)".format(i+1))
        break
    elif nombre_a_deviner < nombreUser:
        print("le nombre a deviner est plus petit que {0}".format(nombreUser))
    elif nombre_a_deviner > nombreUser:
        print('le nombre a deviner est plus grand que {0}'.format(nombreUser))
    
if(nombreUser != nombre_a_deviner):
    print('vous avez perdu le nombre a deviner etait le {0}'.format(nombre_a_deviner))
print('fin du jeu')
    

    

