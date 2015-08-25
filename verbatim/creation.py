% NE PAS OUBLIER DE MODIFIER AUSSI DANS pyverbatim/creation.py
\begin{verbatim}
import random as rd
ANCETRE = [3,2,1,100,1,100]  # La pond�ration "naturelle" de base
CANDIDATS = [ANCETRE]        # Les candidats "pr�qualifi�s"
NOMBRE_DE_CANDIDATS= 12      # Pour une g�n�ration
MAX_VAL = 10                 # Pour un param�tre
NB_PARAMETRES = len(ANCETRE) # Le nombre de param�tres

def cree_candidat():
    """ Cr�ation d'un candidat al�atoire."""
    return [rd.randint(0,MAX_VAL) for j in range(NB_PARAMETRES)]  
    
for i in range(NOMBRE_DE_CANDIDATS-len(CANDIDATS)):
    CANDIDATS.append(cree_candidat())
\end{verbatim}
