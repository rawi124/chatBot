# -*- coding: utf-8 -*-
"""
un simple chatBot d'Assistances aux inscriptions universitaires
"""
import nltk
from nltk.chat.util import Chat, reflections

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

question_reponse = [
        [ 
            r"(.*)date limite(.*)",
           [ "date limite d inscription est le 30/09"]
        ],
        [
            r"(.*)frais(.*)",
            ["les frais d'inscription pour la formation sont de 190 euros"]
        ],
        [
            "r(.*)documents(.*)",
            ["les documents necessaires sont une copie de votre piece d'identité, relevé de note de l'année precedente et notification bourse si vous etes boursier"],
        ]
        ]
def chat_bot(question_reponse):
    """
    fonction qui definit le chatbot
    """
    chatbot = Chat(question_reponse, reflections)
    print("Bonjour ! Comment puis-je vous aider avec les inscriptions ?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Au revoir !")
            break
        response = chatbot.respond(user_input)
        print(response)
if __name__ == "__main__":
    chat_bot(question_reponse)
