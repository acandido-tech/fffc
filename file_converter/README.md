# Fixed File Format converter
L'objectif de cet exercice est d'écrire un outil générique qui convertira un fichier d'entrée au format fixe en un fichier csv, en se basant sur un fichier de metadonnées décrivant sa structure.

## Context
En indiquant le chemin vers le fichier d'entrée au format .txt et le fichier des métadatas au format .csv, l'application va déposer un nouveau fichier au format .csv dans le dossier publique de l'application

## Installation/execution
L'application est écrite en python et nécéssite l'installation des dépendances par le biais d'un environnement virtuel, suivre ces étapes pour mener à bien l'installation de l'application :

```
virtualenv env
```

```
source env/bin/activate
```

```
pip install -r requirements.txt
```

Effectuer le lancement de l'application :
```
python -m file_converter -f file_converter/tests/resources/fixed_file.txt -m file_converter/tests/resources/fixed_file_metadata.csv
```

## Tests
Pour executer les tests, nous utilisons pytest :

```
pytest file_converter
```

## Technical environment / Approach
* python 3.7
* VisualStudioCode
* Git
* Mac - iTerm2
* Oriented object programming
* TDD, clean code using linters (pylint, flake8 and docstring)
