
# ChatBot d'Assistance aux Inscriptions Universitaires

Ce projet consiste en un simple chatbot qui fournit des réponses aux questions fréquemment posées concernant les inscriptions universitaires. Le chatbot est construit en utilisant la bibliothèque NLTK (Natural Language Toolkit) en Python.

## Fonctionnalités

- Répond aux questions sur les dates limites d'inscription.
- Fournit des informations sur les frais d'inscription.
- Donne des détails sur les documents requis pour l'inscription.

## Prérequis

- Python 3.x
- Bibliothèque NLTK (`pip install nltk`)

## Utilisation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir les bibliothèques NLTK installées en exécutant `nltk.download("punkt")`, `nltk.download("averaged_perceptron_tagger")` et `nltk.download("wordnet")`.
3. Exécutez le fichier `cb.py` en utilisant la commande `python3 cb.py`.
4. Le chatbot vous accueillera et vous pourrez commencer à poser des questions sur les inscriptions.

## Exemple de questions

- Quelle date limite pour mon inscription ?
- Quels sont les frais d'inscription pour la formation ?
- Quels documents sont nécessaires pour l'inscription ?

## Utilisation de Docker

Si vous souhaitez exécuter le chatbot dans un environnement Docker, suivez ces étapes :

1. Assurez-vous d'avoir Docker installé sur votre système.

2. Clonez ce dépôt : git clone https://github.com/rawi124/chatBot et se placer dans le repertoire 
3. docker build -t chatbot .
4. docker run -it chatbot
5. Vous devriez maintenant voir le chatbot en cours d'exécution dans le conteneur Docker.



