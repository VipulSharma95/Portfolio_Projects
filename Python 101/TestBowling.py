import unittest
import Game

class TestBowling(unittest.TestCase):

    def test_all_ones(self):
        game = Game.Game()
        game.roll(11,1)
        self.assertEqual(game.score,11)  # add assertion here


if __name__ == '__main__':
    unittest.main()
