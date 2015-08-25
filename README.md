# ICFP 2015 pour le BV

Travail collaboratif pour écrire un article pour le Bulletin Vert de l'UPS 
(Union des Professeurs de classes préparatoires Scientifiques) au sujet de 
notre participation à l'ICFP 2015.

## Dessins, couleurs et pythontex

Le fichier `main.tex` contient trois bascules qui permettent de compiler le 
document plus ou moins vite selon vos envies et votre installation:
* Mettre `\dessinstrue` si vous voulez rajouter les schémas explicatifs (très bien faits, mais très longs à compiler).
* Mettre `\couleurstrue` si vous voulez des dessins couleurs (la bascule est inutile si la bascule précédente est à `\dessinsfalse`).
* Mettre `\pythontextrue` si vous voulez que Pygments s'occupe de la mise en page du code. Il faudra aussi compiler le document avec `pythontex` (voir plus bas). Si vous ne disposez pas du package `pythontex.sty` ou du module python Pygments, mettez `\pythontexfalse`

## Compilation

Pour le moment, exécutez `latex` (ou `pdflatex`) sur le fichier `main.tex` pour 
obtenir l'article.

Si `\pythontextrue`, il faut en plus faire un passage de pythontex au milieu 
(voir Rakefile pour la syntaxe).

Le Rakefile permet de simplifier un peu ceci (nécessite Ruby sur sa machine):

```
~/git/BV_icfp15>rake -T
rake comp     # Compilation sans execution de pythontex
rake compile  # Compilation avec execution de pythontex
```
