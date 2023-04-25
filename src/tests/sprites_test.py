import unittest
from sprites import Sprite


class TestSprite(unittest.TestCase):
    def setUp(self):
        self.player = Sprite("robo")
        self.player.pos = [500,500]
        self.player.move = True
    def test_check_movement(self):
        self.target = [100,100]
        while self.player.move == True:
            self.player.move_sprite()
        self.assertEqual((True,True),(self.player.pos[0], self.player.pos[1]))