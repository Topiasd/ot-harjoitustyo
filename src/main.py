import pygame




class Sprite:
    def __init__(self,name:str):
        self.image = pygame.image.load(name+".png")
        self.x = 640-self.image.get_width()
        self.y = 480-self.image.get_height()
        self.dimensions = (self.image.get_width(),self.image.get_height())
        
        self.speed = 4
        self.move_player_live = False
        self.move_player_last = False
        self.pos_y_collision = False
        self.pos_x_collision = False
        self.neg_y_collision = False
        self.neg_x_collision = False
    def move_sprite(self,destination: tuple):
        self.check_wall_collision()

        x_direction = 1
        y_direction = 1
        if destination[0]<self.x: x_direction = -1
        if destination[1]<self.y: y_direction = -1
        x_dis = abs(self.x - destination[0]) 
        y_dis = abs(self.y - destination[1])
        if x_dis < 5 and y_dis < 5:
            return
        elif x_dis == 0 or self.pos_x_collision and x_direction == 1:
            y_dis += self.speed*y_direction
        elif y_dis == 0 or self.pos_y_collision and y_direction == 1:
            x_dis += self.speed*x_direction
        elif x_dis == 0 or self.neg_x_collision and x_direction == -1:
            y_dis += self.speed*y_direction
        elif y_dis == 0 or self.neg_y_collision and y_direction == -1:
            x_dis += self.speed*x_direction
        elif self.neg_y_collision and y_direction == -1 and self.pos_x_collision and x_direction == 1 or self.neg_y_collision and y_direction == 1 and self.pos_x_collision and x_direction == -1:
            return
        elif self.neg_y_collision and y_direction == 1 and self.pos_x_collision and x_direction == 1 or self.neg_y_collision and y_direction == -1 and self.pos_x_collision and x_direction == -1:
            return
        
        elif x_dis <= y_dis:
            self.x += self.speed*(x_dis/y_dis)*x_direction
            self.y += self.speed*y_direction
        else:
            self.y += self.speed*(y_dis/x_dis)*y_direction
            self.x += self.speed*x_direction
    def check_wall_collision(self):
        self.pos_y_collision = False
        self.pos_x_collision = False
        self.neg_y_collision = False
        self.neg_x_collision = False
        if  self.x < 5:
            self.neg_x_collision = True
        if  self.x > 1275-self.dimensions[0]:
            self.pos_x_collision = True
        
        if  self.y < 5:
            self.neg_y_collision = True
        if  self.y > 955-self.dimensions[1]:
            self.pos_y_collision = True
    
class Game:
    def __init__(self):
        self.mouse_x=0
        self.mouse_y=0
        self.destination_x = 0
        self.destination_y = 0
        pygame.init()

        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Adventure(?)")
        self.clock = pygame.time.Clock()
        self.player = Sprite("robo")
        self.loop()
    def loop(self):
        while True:
            self.render()
            self.events()
            self.clock.tick(60)
    
    def render(self):
        self.display.fill((0,0,0))
        self.display.blit(self.player.image, (self.player.x, self.player.y)) #pelaaja

        pygame.display.flip()
      
    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_x = event.pos[0]
                    self.mouse_y = event.pos[1]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.move_player_last = False
                    self.destination_x = self.mouse_x
                    self.destination_y = self.mouse_y
                    self.player.move_player_live = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.player.move_player_live = False
                    self.destination_x = self.mouse_x
                    self.destination_y = self.mouse_y
                    self.player.move_player_last = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.move_player_last = False
                        self.player.move_player_live = False
                if event.type == pygame.QUIT:
                    exit()
            
            
            if self.player.move_player_live: self.player.move_sprite((self.mouse_x-25,self.mouse_y-35))
            if self.player.move_player_last: self.player.move_sprite((self.destination_x-25,self.destination_y-35))
            
    
    







if __name__ == "__main__":
    Game()