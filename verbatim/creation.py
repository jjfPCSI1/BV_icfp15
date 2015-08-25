% NE PAS OUBLIER DE MODIFIER AUSSI DANS pyverbatim/creation.py
\begin{verbatim}
import random as rd
ANCETRE = [3,2,1,100,1,100]  # La pondération "naturelle" de base
CANDIDATS = [ANCETRE]        # Les candidats "préqualifiés"
NOMBRE_DE_CANDIDATS= 12      # Pour une génération
MAX_VAL = 10                 # Pour un paramètre
NB_PARAMETRES = len(ANCETRE) # Le nombre de paramètres

def cree_candidat():
    """ Création d'un candidat aléatoire."""
    return [rd.randint(0,MAX_VAL) for j in range(NB_PARAMETRES)]  
    
for i in range(NOMBRE_DE_CANDIDATS-len(CANDIDATS)):
    CANDIDATS.append(cree_candidat())
\end{verbatim}
