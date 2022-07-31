import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cg = CardGame()
        self.h1 = Card("Hearts", 1)
        self.d1 = Card("Diamond", 7)
        self.cards = [self.h1, self.d1]


    
    def test_check_for_ace(self):
        
        self.assertEqual(True, self.cg.check_for_ace(self.h1))
        
    

    def test_highest_card(self):
        self.assertEqual(self.h1, self.cg.highest_card(self.h1, self.d1))
        


    def test_cards_total(self):
        self.assertEqual('You have a total of 8', self.cg.cards_total(self.cards))
        