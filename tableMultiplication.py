responseUser = "o"
multiple = range(1, 11)
while responseUser == 'o':
    nombre = input("choisissez un nombre dont vous voulez la table : ")
    for i in multiple:
        print('{0} x {1} = {2} '.format(nombre, i, int(nombre)*i))
    
    responseUser = raw_input("voulez vous continuez ? o/n ")
print("script terminer.")
    