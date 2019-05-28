#!/usr/bin/env python

import unittest
import app

class HoleCheckerTestCase(unittest.TestCase):
    '''
    Classe de teste para a função que checa buracos
    '''
    def setUp(self):  # Define os valores que serão testados
        self.right_words = {
            'Laranja': 3,
            'Brasília': 4,
            'Balestra': 5,
            'Absurdo': 4,
            'Alarme': 3,
            'Calamidade': 6,
            'Milho': 1,
            'City': 0,
            '': 0,
        }
        self.wrong_words = {
            'T4mer': 'A palavra inserida deve conter apenas letras',
            '123': 'A palavra inserida deve conter apenas letras'
        }

    def test_holes_correct(self):  # Testa os valores previamente definidos
        for key, value in self.right_words.items():
            self.assertEqual(app.checa_buracos(key),value)

    def test_wrong_holes(self):
        for key in self.wrong_words.keys():
            self.assertRaises(KeyError, lambda: app.checa_buracos(key))
if __name__=='__main__':
    unittest.main()
