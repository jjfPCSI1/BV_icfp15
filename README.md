# ICFP 2015 pour le BV

Travail collaboratif pour �crire un article pour le Bulletin Vert de l'UPS 
(Union des Professeurs de classes pr�paratoires Scientifiques) au sujet de 
notre participation � l'ICFP 2015.

## Compilation

Pour le moment, ex�cutez `latex` (ou `pdflatex`) sur le fichier `main.tex` pour 
obtenir l'article.

Si `\pythontextrue`, il faut en plus faire un passage de pythontex au milieu 
(voir Rakefile pour la syntaxe).

Le Rakefile permet de simplifier un peu ceci (n�cessite Ruby sur sa machine):

```
~/git/BV_icfp15>rake -T
rake comp     # Compilation sans execution de pythontex
rake compile  # Compilation avec execution de pythontex
```
