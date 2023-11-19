import unittest
import my_game
from unittest.mock import patch, MagicMock
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from my_game import Game, TicTacToe

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.tic_tac_toe.game.screen = MagicMock()
        self.game.tic_tac_toe.game_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_new_game(self):
        initial_game_array = [row[:] for row in self.game.tic_tac_toe.game_array]
        self.game.new_game()
        new_game_array = self.game.tic_tac_toe.game_array
        self.assertNotEqual(initial_game_array, new_game_array)

    @patch('pygame.event.get', return_value=[MagicMock(type=QUIT)])
    def test_check_events_quit(self, mock_event_get):
        with self.assertRaises(SystemExit):
            self.game.check_events()

    @patch('pygame.event.get', return_value=[MagicMock(type=KEYDOWN, key=K_SPACE)])
    def test_check_events_new_game(self, mock_event_get):
        initial_game_array = [row[:] for row in self.game.tic_tac_toe.game_array]
        self.game.check_events()
        new_game_array = self.game.tic_tac_toe.game_array
        self.assertNotEqual(initial_game_array, new_game_array)

    # Add more test methods as needed...

if __name__ == '__main__':
    unittest.main()
