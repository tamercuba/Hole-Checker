#!/usr/bin/env python

import unittest
import app

class HoleCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.words = {
            'Laranja': 3,
            'Brasília': 4,
            'Balestra': 5,
            'Absurdo': 3,
            'Alarme': 3,
            'Calamidade': 6,
            'Milho': 1,
            'City': 0,
            '': 0,
        }
    def test_holes(self):
        for key, value in self.words.items():
            self.assertEqual(app.hole_checker(key), value)

if __name__=='__main__':
    unittest.main()
