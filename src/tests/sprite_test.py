import pygame
import unittest

from main import Sprite


class TestSprite(unittest.TestCase):
    def setUp(self):
        self.player = Sprite("robo")
    def test_check_collision_out_of_bounds_pos_x(self):
        self.player.move_sprite((2000,2000))
        self.assertEqual(False,self.player.x>1280)
    def test_check_collision_out_of_bounds_pos_y(self):
        self.player.move_sprite((2000,2000))
        self.assertEqual(False,self.player.y>1280)
    def test_check_collision_out_of_bounds_neg_x(self):
        self.player.move_sprite((2000,2000))
        self.assertEqual(False,self.player.x<0)
    def test_check_collision_out_of_bounds_neg_y(self):
        self.player.move_sprite((-2000,-2000))
        self.assertEqual(False,self.player.y<0)