import statistics

def calcule_moyenne(ls_nombres):
    for nombre in ls_nombres:
        if type(nombre) not in (float, int):
            raise TypeError
        return statistics.mean(ls_nombres)


ls_nombres = []
while user_continue == "1":
    ls_nombres.append(int(input()))
ls_nombres.append(int(input("entrer un chiffre")))
print(ls_nombres)

calcule_moyenne(ls_nombres)

