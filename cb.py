# -*- coding: utf-8 -*-
"""
un simple chatBot d'Assistances aux inscriptions universitaires
"""
import nltk
from nltk.chat.util import Chat, reflections
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")


class ExpressionInvalide(Exception):
    """
    exception si la question posée ne 
    match avec aucune question du chatBot
    """
    pass


question_reponse = [
    [
        r"(.*)date limite(.*)",
        ["date limite d inscription est le 30/09"]
    ],
    [
        r"(.*)frais(.*)",
        ["les frais d'inscription pour la formation sont de 190 euros"]
    ],
    [
        r"(.*)documents(.*)",
        ["les documents necessaires sont une copie de"
         + " votre piece d identite, releve de note de l annee precedente "
         + "et notification bourse si vous etes boursier"],
    ]
]


def chat_bot():
    """
    fonction qui fais appel aux paires de qestion reponses
    """
    chatbot = Chat(question_reponse, reflections)
    print("Bonjour ! Comment puis-je vous aider avec votre inscription ?")
    reponse = None
    while True:
        try:
            entree = input(">>> ")
            if entree.lower() == "quitter":
                print("Au revoir !")
                break
            if not entree:
                raise ExpressionInvalide(
                    "saisie non valide, veuillez entrer une autre expression")
            reponse = chatbot.respond(entree)
            if reponse is None:
                raise ExpressionInvalide(
                    "désolé je ne comprend pas votre demande")
            print(reponse)
        except Exception as err :
            print(f"une erreur c'est produite : {err}")
    return reponse


if __name__ == "__main__":
    reponses = chat_bot()
