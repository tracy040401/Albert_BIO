# Fonction qui renvoie un vecteur contenant toutes les étiquettes possibles
def extract_label(chemin_fichier):
    liste_etiquettes = []
    with open(chemin_fichier, 'r') as fichier:
        for ligne in fichier:
            if ligne.strip(): # Ignore les lignes vides
                mots = ligne.strip().split('\t')  # Sépare les 2 mots de la ligne
                if len(mots) == 2:  # Si la ligne contient 2 mots (=> ignore les lignes vides des sauts de ligne)
                    etiquette = mots[1] # Récupère le 2e mot de la ligne (= l'étiquette)
                    if etiquette not in liste_etiquettes: # Vérifie si le mot n'est pas déjà dans la liste
                        liste_etiquettes.append(etiquette) # Ajoute le 2e mot à la liste dans ce cas
    return liste_etiquettes


if __name__ == "__main__":    
    etiquettes = extract_label("atis.train")
    print("Etiquettes : ", etiquettes)
    print("Nombre d'étiquettes : ", len(etiquettes))