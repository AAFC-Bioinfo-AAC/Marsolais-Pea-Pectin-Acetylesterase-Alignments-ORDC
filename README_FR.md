# Alignements-Marsolais-Pois-Pectine-Acétylestérase-ORDC

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](README_FR.md)

## Table des matières

- [À propos](#à-propos)
- [Documentation](#documentation)
- [Crédits](#crédits)
- [Citation](#citation)
- [Contribution](#contribution)
- [Références](#références)
- [Sécurité](#sécurité)
- [Licence](#licence)

## À propos

Ce dépôt contient des scripts pour la création d'alignements de nucléotides et d'acides aminés à l'aide de 118 génomes de pois et d'un gène de référence de la pectine acétylestérase. Le flux de travail traite des séquences génomiques complètes de trois espèces de pois différentes et génère des alignements de séquences nucléotidiques et protéiques grâce à une série d'étapes automatisées comprenant des recherches BLASTn, l'extraction de séquences, la traduction et l'alignement.

**Caractéristiques principales :**
- Traitement automatisé de 118 génomes entiers de pois
- Alignement guidé par référence à l'aide de séquences du gène de la pectine acétylestérase
- Génération d'alignements de séquences nucléotidiques et d'acides aminés
- Prise en charge de plusieurs espèces (pois et pois chiche)
- Flux de travail modulaire avec des étapes de traitement distinctes

## Documentation

Pour des informations techniques détaillées, y compris :
- Instructions étape par étape du flux de travail
- Exigences d'entrée et sources de données
- Dépendances logicielles et versions
- Explications détaillées de chaque étape de traitement

Veuillez vous référer aux sections de documentation technique ci-dessous ou consulter le [Guide de l'utilisateur](docs/user-guide.md) pour des instructions complètes.

## Crédits

**Auteure principale :**
- Dre Haley Sanderson, programmeuse en bioinformatique, Agriculture et Agroalimentaire Canada (Haley.Sanderson@agr.gc.ca)

**Chef d'équipe :**
- Jackson Eyres, chef d'équipe en bioinformatique, Agriculture et Agroalimentaire Canada (jackson.eyres@agr.gc.ca)

**Organisation :**
- Agriculture et Agroalimentaire Canada, Gouvernement du Canada

## Citation

Pour citer ce projet, veuillez cliquer sur le bouton **Citer ce dépôt** dans la barre latérale droite, ou utiliser les informations fournies dans le fichier `CITATION.cff`.

## Contribution

Les contributions sont les bienvenues! Veuillez contacter l'auteure principale ou le chef d'équipe pour discuter des contributions potentielles. Assurez-vous que toutes les contributions respectent les meilleures pratiques en matière de qualité du code et de documentation.

## Références

### Publications clés

- Yang et al. - Séquences du génome du pois (disponibles sur [Zenodo](https://zenodo.org/api/records/6622578/files-archive))
- Khan et al. - Séquences du génome du pois chiche (disponibles sur [NCBI](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1043734))

### Citations logicielles

- **BLAST**: Korf, I., Yandell, M., & Bedell, J. (2003). BLAST. "O'Reilly Media, Inc.".
- **EMBOSS**: Rice, P., Longden, I., & Bleasby, A. (2000). EMBOSS: the European molecular biology open software suite. *Trends in Genetics*, 16(6), 276-277.
- **MAFFT**: Katoh, K., Misawa, K., Kuma, K. I., & Miyata, T. (2002). MAFFT: a novel method for rapid multiple sequence alignment based on fast Fourier transform. *Nucleic Acids Research*, 30(14), 3059-3066.
- **SeqKit**: Shen, W., Le, S., Li, Y., & Hu, F. (2016). SeqKit: a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. *PLoS ONE*, 11(10), e0163962.

## Sécurité

⚠️ **Ne publiez aucun problème de sécurité sur le dépôt public !** Veuillez les signaler comme décrit dans [SECURITY.md](SECURITY.md).

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails. Visitez [LicenseHub](https://licensehub.ca/) ou [tl;drLegal](https://tldrlegal.com/) pour consulter un résumé de cette licence en langage clair.

**Copyright © Sa Majesté le Roi du chef du Canada, représentée par la Ministre de l'Agriculture et de l'Agroalimentaire, 2025.**
