"""
Nicolas est un bon ami. Il va aller faire la file pour acheter les nouveaux souliers que vous désirez tant. 
Sa seule condition est que vous lui disiez exactement combien de temps il va devoir attendre. 

Chaque personne peut acheter seulement une paire à la fois et la transaction dure exactement une minute. 
Ensuite, si elle en veut plus, elle retourne au bout de la ligne. Si elle a tout ce qu’elle désire, elle quitte la file tout simplement.

Important :
Votre application va toujours recevoir une liste qui contient la file d’attente complète avec le nombre de personnes 
et le nombre de paires de souliers qu’ils veulent acheter et la position de votre ami.

Exemple : 
Si vous recevez la liste initiale [2, 5, 3, 4, 6] et que vous savez que votre ami est le 3e dans la file (index 2), 
la première personne achète une paire et s’en retourne au bout de la file pour donner ce résultat : [5, 3, 4, 6, 1]. 
Le tout se poursuit avec [3, 4, 5, 1, 4] et ainsi de suite jusqu’à ce que notre ami est acheté 3 paires de souliers et attendu exactement 12 minutes.

Construisez cette application en sachant que la liste sera toujours remplie d’entier positif et que la position de votre ami sera valide. 
Soyez prêt, par contre, à certaines très longues files d’attente
"""


def main():
    # Files à calculer.
    ls_files_attente = [
        ([2, 5, 3, 6, 4], 0),
        ([2, 5, 3, 6, 4], 1),
        ([2, 5, 3, 6, 4], 2),
        ([2, 5, 3, 6, 4], 3),
        ([2, 5, 3, 6, 4], 4)
    ]
    ls_reponses_prof = [6, 18, 12, 20, 17]

    # Insérer code ici
    pass


if __name__ == '__main__':
    main()

