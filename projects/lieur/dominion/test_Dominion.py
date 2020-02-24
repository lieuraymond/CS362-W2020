from unittest import TestCase
import Dominion
import testUtility

class TestAction_card(TestCase):
    def setup_card(self):
        self.name = "Abracadabra"
        self.cost = 1
        self.actions = 10
        self.cards = 3
        self.buys = 5
        self.coins = 2
        self.test_action_card = Dominion.Action_card(self.name, self.cost, self.actions, self.cards, self.buys, self.coins)
        self.player = Dominion.Player("Bob")
        self.player.actions = 0
        self.player.buys = 0
        self.player.purse = 0

    def test_init(self):
        self.setup_card()
        self.assertEqual(self.name, self.test_action_card.name)
        self.assertEqual(self.cost, self.test_action_card.cost)
        self.assertEqual(self.actions, self.test_action_card.actions)
        self.assertEqual(self.cards, self.test_action_card.cards)
        self.assertEqual(self.buys, self.test_action_card.buys)
        self.assertEqual(self.coins, self.test_action_card.coins)

    def test_use(self):
        self.setup_card()
        self.trash = []
        self.player.hand.append(self.test_action_card)
        self.assertIn(self.test_action_card, self.player.hand)
        self.assertEqual(6, len(self.player.hand))
        self.test_action_card.use(self.player, self.trash)
        self.assertEqual(5, len(self.player.hand))
        self.assertNotIn(self.test_action_card, self.player.hand)
        self.assertEqual(1, len(self.player.played))
        self.assertEqual(self.test_action_card.name, self.player.played[0].name)

    def test_augment(self):
        self.setup_card()
        self.test_action_card.augment(self.player)
        self.assertEqual(self.player.actions, self.test_action_card.actions)
        self.assertEqual(self.player.buys, self.test_action_card.buys)
        self.assertEqual(self.player.purse, self.test_action_card.coins)
        self.assertEqual(8, len(self.player.hand))


class TestPlayer(TestCase):
    def test_draw(self):
        self.player = Dominion.Player("Bob")
        self.assertEqual(5, len(self.player.hand))
        self.assertEqual(5, len(self.player.deck))
        self.assertEqual(0, len(self.player.discard))
        self.player.draw()
        self.assertEqual(6, len(self.player.hand))
        self.assertEqual(4, len(self.player.deck))
        self.assertEqual(0, len(self.player.discard))
        self.player.draw(self.player.discard)
        self.assertEqual(6, len(self.player.hand))
        self.assertEqual(3, len(self.player.deck))
        self.assertEqual(1, len(self.player.discard))
        self.player.deck = []
        self.player.draw()
        self.assertEqual(7, len(self.player.hand))
        self.assertEqual(0, len(self.player.deck))
        self.assertEqual(0, len(self.player.discard))

    def test_action_balance(self):
        self.player = Dominion.Player("Bob")
        self.test_action_card = Dominion.Action_card("test", 2, 3, 0, 0, 0)
        self.test_action_card2 = Dominion.Action_card("test", 2, 0, 0, 0, 0)
        self.player.hand.append(self.test_action_card)
        self.assertEqual(self.player.action_balance(), 140/11)
        self.player.hand.append(self.test_action_card2)
        self.assertEqual(self.player.action_balance(), 70/ 12)


    def test_cardsummary(self):
        self.player = Dominion.Player("Bob")
        self.testSummary = {}
        self.testSummary['Copper'] = 7
        self.testSummary['Estate'] = 3
        self.testSummary['VICTORY POINTS'] = 3
        self.assertEqual(self.testSummary, self.player.cardsummary())
        self.test_hand_card = Dominion.Action_card('Hand', 2, 3, 0, 0, 0)
        self.test_discard_card = Dominion.Action_card('Discard', 2, 3, 0, 0, 0)
        self.test_played_card = Dominion.Action_card('Played', 2, 3, 0, 0, 0)
        self.test_aside_card = Dominion.Action_card('Aside', 2, 3, 0, 0, 0)
        self.test_hold_card = Dominion.Action_card('Hold', 2, 3, 0, 0, 0)
        self.player.hand.append(self.test_hand_card)
        self.testSummary['Hand'] = 1
        self.assertEqual(self.testSummary, self.player.cardsummary())
        self.player.hand.append(self.test_discard_card)
        self.testSummary['Discard'] = 1
        self.player.played.append(self.test_played_card)
        self.testSummary['Played'] = 1
        self.player.aside.append(self.test_aside_card)
        self.testSummary['Aside'] = 1
        self.player.hold.append(self.test_hold_card)
        self.testSummary['Hold'] = 1

    def test_calcpoints(self):
        self.player = Dominion.Player("Bob")
        self.assertEqual(3, self.player.calcpoints())
        self.player.hand.append(Dominion.Estate())
        self.assertEqual(4, self.player.calcpoints())
        self.player.deck.append(Dominion.Estate())
        self.assertEqual(5, self.player.calcpoints())
        self.player.discard.append(Dominion.Estate())
        self.assertEqual(6, self.player.calcpoints())
        for i in range(7):
            self.assertEqual(6 + i, self.player.calcpoints())
            self.player.hand.append(Dominion.Gardens())
        self.assertEqual(20, self.player.calcpoints())



