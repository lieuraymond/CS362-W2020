from unittest import TestCase
import Dominion
import testUtility

class TestCard(TestCase):
    def setUp(self):
        self.player_names = ["Annie", "*Ben", "*Carla"]
        self.nV, self.nC = testUtility.set_vc_number(self.player_names)
        self.box, self.supply_order = testUtility.define_box(self.nV)
        self.supply = testUtility.set_supply(self.box, self.player_names, self.nV, self.nC)
        self.trash = []
        self.players = testUtility.set_players(self.player_names)
        self.players = testUtility.set_players(self.player_names)
        self.player = Dominion.Player('Bob')
    def test_unit(self):
        self.setUp()
        cost = 1
        buypower = 5
        card = Dominion.Coin_card(self.player.name, cost, buypower)
        self.assertEqual("Bob", card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        pass

