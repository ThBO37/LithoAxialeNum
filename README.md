# TIPE : Lithographie axiale numérique

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Sommaire</summary>
  <ol>
    <li><a href="#Motivations-du-sujet">Motivations du sujet</a></li>
    <li><a href="#Ancrage">Ancrage au thème</a></li>
    <li><a href="#MCOT">Mise en cohérence des objectifs</a></li>
    <li><a href="#Biblio">Bibliographie commentée</a></li>
    <li><a href="#Références">Réferences bibliographiques</a></li>
  </ol>
</details>

## Motivations du sujet

<div align="justify">
	La réaction de photopolymérisation étant déjà utilisée dans certaines imprimantes 3D selon un
procédé linéique et discret, nous nous sommes demandés s’il était possible de rendre celui-ci continu
et volumétrique afin d'augmenter la vitesse de fabrication et la qualité des pièces produites.
Le dispositif étudié pourrait permettre la fabrication très rapide, précise et durable de pièces à la
demande, pouvant servir de pierre angulaire au développement d’un modèle de production plus
local et décentralisé permettant de modifier profondément notre futur modèle socio-économique.
</div>

## Mise en cohérence des objectifs

### Bibliographie commentée
<div align="left">
Dans les années 1980, un groupe de chercheurs français se heurte aux limitations géométriques des
procédés de fabrication classiques alors utilisés (usinage, fonderie, …). Ils cherchent alors un
nouveau moyen de fabriquer des pièces aux géométries complexes, puis réalisent quelque temps plus
tard, grâce à leur procédé solidifiant localement un photopolymère liquide à l’aide d’un laser, le
premier objet imprimé en 3D.[1]
</div>
<br/>

<div align="left">
Depuis cette invention en 1984 et jusqu’à aujourd’hui, un certain nombre de procédés de fabrication
additive ont été développés, basés sur une approche 0D (construction d’un point à la fois, en
général par une fusion puis une solidification) pour les technologies FDM, SLA ou SLS par exemple ; ou sur une approche 2D (construction d’une couche à la fois) pour la technologie DLP. Ces
technologies présentent cependant deux carences. La première est la limitation en termes de
rapidité de ces technologies : la durée de fabrication de pièces n’est dépendante (à qualité donc
résolution constante) que de la taille desdites pièces (temps de déplacement de la tête d’impression
pour la FDM, séquence de déplacement du plateau entre les couches pour la DLP, …), nous avons
alors affaire à des procédés industriels lents (par comparaison avec le moulage par injection par
exemple). La deuxième est l’aspect « discret » des pièces générées, dû à l’approche couche-par-couche de ces technologies. Les conséquences de cet aspect discret sont de deux ordres : au niveau
de la résistance des pièces fabriquées, celles-ci devenant anisotropes, ce qui tend à rendre aléatoire
et imprévisible leur comportement réel ; et au niveau de l’état de surface (effet « créneau »), ce qui
limite l’utilisation mécanique et l’esthétique de ces pièces.[2]
</div>
<br/>

<div align="left">
De nouveaux procédés apportent des solutions à l’anisotropie tout en améliorant considérablement
la vitesse de production.[3][4] Ces procédés reposent sur l’utilisation de la photopolymérisation, qui,
sous un éclairage lumineux à une longueur d’onde donnée, transforme une résine liquide formée de
monomères en un solide composé d’un assemblage de ces monomères, un polymère plastique.[5]
</div>
<br/>

<div align="left">
A l’aide d'images créées selon le mode de projection et l'objet lui-même, on pourrait alors éclairer
une cuve de résine photopolymère de sorte que chaque point du volume de travail reçoive une
quantité d'énergie précise.[3] Selon l’intensité de l’énergie lumineuse reçue, la résine se polymérise
ou pas, ce qui permet de solidifier certaines zones du volume de travail, et d'en laisser d'autres
liquides. En particulier, un procédé à prendre en compte (appelé lithographie axiale numérique) est
celui d'une cuve de résine mise en rotation autour d'un axe, et dans laquelle sont projetées des
images déterminées en fonction de l'angle de manière à créer dans l'espace de la cuve des zones
ayant reçu plus ou moins d'énergie.[4]
</div>
<br/>

<div align="left">
Afin de pouvoir exploiter ce phénomène, il est nécessaire d’établir un modèle cinétique de la
réaction chimique, afin d’adapter la vitesse de rotation de la cuve, la puissance d’éclairement, et de
s’assurer d’obtenir une pièce finale aux propriétés mécaniques intéressantes. La cinétique de la
réaction est conditionnée par de nombreux paramètres : le matériau lui-même, mais aussi la
température, la longueur d’onde utilisée, ou encore l’absorbance du matériau, qui de surcroît change
lors de la polymérisation.[6]
</div>
<br/>

<div align="left">
De plus, le procédé de lithographie axiale numérique étant basé sur la modulation de l'intensité
lumineuse en fonction de l'angle de projection, il est indispensable d'élaborer des images projetées
permettant de moduler au mieux l'énergie lumineuse reçue par chaque point du volume de travail.
Pour chacune des images projetées (dépendantes de l'angle de projection), on cherche alors à
moduler l'énergie apportée à la résine en associant à chacun des points de cette image une valeur
proportionnelle à l'épaisseur de la pièce "du point de vue de l'image". Ce méthode est appelée
"transformée de Radon". On peut de même obtenir l'énergie reçue en chaque point en appliquant la
transformée de Radon inverse, tout comme pour la méthode de reconstruction 3D à partir de
coupes de la technique d'imagerie médicale dite de tomodensitométrie.[7]
</div>
<br/>


### Références bibliographiques
<div align="left">
[1] André, J.-C., Le Méhauté, A., & De Witte, O. : Dispositif pour réaliser un modèle de pièce
industrielle : 1984. FR 2567668 A1. Institut National de la Propriété Intellectuelle. https://bases-brevets.inpi.fr/fr/document/FR2567668.html
</div>
<br/>

<div align="left">
[2] Ngo, T. D., Kashani, A., Imbalzano, G., Nguyen, K. T. Q., & Hui, D. : Additive manufacturing (3D
printing) : A review of materials, methods, applications and challenges : 2018. Composites Part B
: Engineering, 143, 172 196. doi:10.1016/j.compositesb.2018.02.012
</div>
<br/>

<div align="left">
[3] Shusteff, M., Browar, A. E. M., Kelly, B. E., Henriksson, J., Weisgraber, T. H., Panas, R. M., Fang,
N. X., & Spadaccini, C. M. : One-step volumetric additive manufacturing of complex polymer
structures : 2017. Science Advances, 3(12), eaao5496. doi:10.1126/sciadv.aao5496
</div>
<br/>

<div align="left">
[4] Kelly, B. E., Bhattacharya, I., Heidari, H., Shusteff, M., Spadaccini, C. M., & Taylor, H. K. :
Volumetric additive manufacturing via tomographic reconstruction : 2019. Science, 363(6431),
1075 1079. doi:10.1126/science.aau7114
</div>
<br/>

<div align="left">
[5] Odian, G. G. : Principles of polymerization (Vol. 4) : 2004. Wiley-Interscience.
doi:10.1002/047147875X
</div>
<br/>

<div align="left">
[6] Patacz, C. : Etude cinétique de la polymérisation de monomères acryliques sous faisceau
d’électrons : approche analytique et réactivités comparées : 1996. https://ori-nuxeo.univ-lille1.fr/nuxeo/site/esupversions/60cb0bd9-f05c-4239-9bdb-3096785a0508
</div>
<br/>

<div align="left">
[7] Zvolsky, M. : Tomographic Image Reconstruction : An Introduction : 2014.
https://www.desy.de/~garutti/LECTURES/BioMedical/Lecture7_ImageReconstruction.pdf
</div>
<br/>
