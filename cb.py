# -*- coding: utf-8 -*-
"""
un simple chatBot d'Assistances aux inscriptions universitaires
"""
import nltk
from nltk.chat.util import Chat, reflections

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

def chat_bot():
    """
    fonction qui definit le chatbot
    """
    question_reponse = [
            [
                r"(.*) date limite (.*)",
                ["la date limite d'inscription pour les etudiants en informatique est le 31/09"],
                ]
            ]
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
    chat_bot()
