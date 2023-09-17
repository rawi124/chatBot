import unittest
from unittest.mock import patch
from cb import chat_bot, ExpressionInvalide

class TestChatBot(unittest.TestCase):

    @patch('builtins.input', side_effect=["date limite", "quitter"])
    def test_date_limite(self, mock_input):
        with self.subTest():
            expected_responses = "date limite d inscription est le 30/09"
            self.assertEqual(chat_bot(), expected_responses)

    @patch('builtins.input', side_effect=["frais", "quitter"])
    def test_frais(self, mock_input):
        with self.subTest():
            expected_responses = "les frais d'inscription pour la formation sont de 190 euros"
            self.assertEqual(chat_bot(), expected_responses)

    @patch('builtins.input', side_effect=["documents", "quitter"])
    def test_documents(self, mock_input):
        with self.subTest():
            expected_responses = "les documents necessaires sont une copie de votre piece d identite, releve de note de l annee precedente et notification bourse si vous etes boursier"
            self.assertEqual(chat_bot(), expected_responses)


if __name__ == '__main__':
    unittest.main()

