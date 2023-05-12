import unittest
from sprites import Sprite


class TestSprite(unittest.TestCase):
    def setUp(self):
        self.player = Sprite("robo","robo",False,[])
        self.player.pos = [500,500]
        self.player.move = True
    def test_check_movement_within(self,target=[330,467]):
        self.player.target = target
        while self.player.move == True:
            self.player.move_sprite()
        self.assertEqual((True),abs(self.player.pos[0]-target[0])<=6 and abs(self.player.pos[1]-target[1])<=6)
    def test_check_movement_outside(self,target=[2000,2000]):
        self.player.target = target
        while self.player.move == True:
            self.player.move_sprite()
        self.assertEqual((True),self.player.pos[0]<=1280 and self.player.pos[1]<=960)
    def test_area_change(self,triggers=["n","s","w","e"]):
        all_directions = ""
        self.player.pos[0]=550
        self.player.pos[1]=851
        all_directions += self.player.area_change(triggers)
        self.player.pos[1]=49
        all_directions += self.player.area_change(triggers)
        self.player.pos[1]=351
        self.player.pos[0]=1201
        all_directions += self.player.area_change(triggers)
        self.player.pos[0]=39
        all_directions += self.player.area_change(triggers)
        self.assertEqual((all_directions),"snew")