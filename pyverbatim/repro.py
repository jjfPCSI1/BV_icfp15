% NE PAS OUBLIER DE MODIFIER AUSSI DANS verbatim/repro.py
\begin{pyverbatim}[][numbers=left]
def reproduction(p1,r1,p2,r2):
    """ M�lange des g�nes pour p1 et p2. Renvoie un enfant.
    r1 et r2 sont les r�sultats respectivement pour p1 et p2. """   
    poids = r1/(r1+r2)
    enfant = []
    for i in range(NB_PARAMETRES):
        # 9 fois sur 10, c'est le mixage normal
        if rd.randint(0,9) < 9:
            # On met un peu d'al�atoire dans le m�lange 
            coeff = poids + (-1)**rd.randint(0,1) * rd.random()
            enfant.append(int(coeff*p1[i] + (1-coeff)*p2[i]))
        else: # Sinon, mutation al�atoire
            enfant.append(rd.randint(0,MAX_VAL))
    return enfant
\end{pyverbatim}
