### BONJOUR NICHOLAS, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

#Tentative 1 ### ICI, ET DANS TA TENTATIVE #2, LE PROBLÈME EST QUE TU ESSAIES DE CONCATÉNER DU TEXTE ("STRING") AVEC UNE LISTE.

# f1 = "https://montrealcampus.ca/?p="
# f2 = list(range(20000, 30150))
# f3 = f1+f2
# print(f3)

#TENTATIVE 2
# f1 = "https://montrealcampus.ca/?p="
# f2 = str(list(range(20000, 30151)))
# f3 = f1+f2
# print(f3)

#TENTATIVE 3
# f1 = str(list(range(20000, 30151)))
# print(f1)

# n = 0
# for list in f1: ### TU TE RAPPROCHES DU BUT!
#     n += 1
#     print(f1) ### ICI, TU IMPRIMES 10150 FOIS 10150 NOMBRES, DONC 103 022 500 NOMBRES!!!

#TENTATIVE 4 ### ICI, IL MANQUE TA BOUCLE... ENTRE AUTRES :)
# f1 = ["https://montrealcampus.ca/?p=20000", "https://montrealcampus.ca/?p=20001", "https://montrealcampus.ca/?p=20002", "https://montrealcampus.ca/?p=20003"]
# f1.append("https://montrealcampus.ca/?p=" + str(list(range(20000, 30151))))
# print(f1)

#TENTATIVE 5

### IL EST TRÈS INTÉRESSANT DE VOIR TES DIFFÉRENTES TENTATIVES! BRAVO!
### TA 5E EST TOUT PRÈS DU BUT RECHERCHÉ!
### IL NE MANQUE QUE DE CRÉER UNE LISTE VIDE DANS LAQUELLE TU PLACERAS TOUS LES URLS CRÉÉS PAR TA BOUCLE:

vide = []

f1 = list(range(20000, 30151))

n = 0
for articles in f1:
    n += 1
    print(n)
    print("https://montrealcampus.ca/?p=" + str(articles))

    ### ENSUITE, IL SUFFIT DE PLACER CHAQUE URL DANS TA LISTE "vide":

    vide.append("https://montrealcampus.ca/?p=" + str(articles))

### PUIS, À LA FIN, POUR VÉRIFIER, TU PEUX AFFICHER LE CONTENU DE CETTE LISTE ET SA LONGUEUR:
print(vide,len(vide))