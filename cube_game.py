import pygame
import time

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BULLET_SPEED = 15

class Player:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(WIN, (0, 0, 0), (self.x, self.y, self.width, self.height))
    
    def move(self, direction):
        if direction == "up":
            self.y -= 5
        if direction == "down":
            self.y += 5
        if direction == "right":
            self.x += 5
        if direction == "left":
            self.x -= 5

class Bullet:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.x_speed = 0
        self.y_speed = 0
        if direction == "up":
            self.y_speed = -10
        if direction == "down":
            self.y_speed = 10
        if direction == "right":
            self.x_speed = 10
        if direction == "left":
            self.x_speed = -10
        

    
    def draw(self):
        pygame.draw.rect(WIN, (255, 0, 0), (self.x, self.y, 10, 10))

class Enemy:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = 5
        self.y_speed = 5
        self.shot = False
        self.temp_x = x
        self.temp_y = y
    
    def draw(self):
        pygame.draw.rect(WIN, (106, 13, 173), (self.x, self.y, self.width, self.height))
    
    def move(self, direction):
        if direction == "horizontal":
            self.y_speed = 0
            if self.x == 720:
                self.x_speed = -5
            if self.x == 80:
                self.x_speed = 5
            self.x += self.x_speed
            
        if direction == "vertical":
            self.x_speed = 0
            if self.y == 520:
                self.y_speed = -5
            if self.y == 80:
                self.y_speed = 5
            self.y += self.y_speed

class Enemy_bullet:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.x_speed = 0
        self.y_speed = 0
        if direction == "up":
            self.y_speed = -10
        if direction == "down":
            self.y_speed = 10
        if direction == "right":
            self.x_speed = 10
        if direction == "left":
            self.x_speed = -10
    
    def draw(self):
        pygame.draw.rect(WIN, (255, 0, 0), (self.x, self.y, 10, 10))
        
        
def draw(player):
    WIN.fill((255, 255, 255))
    player.draw()

    for bullet in bullets:
        bullet.draw()
    
    for enemy in enemies:
        enemy.draw()
    
    pygame.display.update()


#dummy = Enemy(60, 60, 30, 30)
enemies = []
bullets = []
# MAINLOOP
def main():

    running = True
    clock = pygame.time.Clock()
    ready = True
    first_shot = True
    

    player = Player(400, 300, 30, 30)
    enemies.append(Enemy(150, 50, 30, 30))
    enemies.append(Enemy(150, 520, 30, 30))
    enemies.append(Enemy(720, 150, 30, 30))
    enemies.append(Enemy(80, 150, 30, 30))
    

    while running:
        clock.tick(FPS)
        draw(player)
        end = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        #BULLET MOVEMENT
        for bullet in bullets:
            if (bullet.x < 800 and bullet.x > 0) and (bullet.y > 0 and bullet.y < 600):
                bullet.x += bullet.x_speed
                bullet.y += bullet.y_speed
            else:
                bullets.pop(bullets.index(bullet))

            for enemy in enemies:
                if (bullet.x <= enemy.x + 30 and bullet.x >= enemy.x) and (bullet.y <= enemy.y + 30 and bullet.y >= enemy.y):
                    enemy.shot = True
                    enemy.temp_x = enemy.x
                    enemy.temp_y = enemy.y
                    enemy.x = 1000
                    enemy.y = 1000
                    global int0
                    int0 = time.time()
                
                
        #ENEMY DISAPPEAR
        for enemy in enemies:
            if enemy.shot:
                if end-int0 > 1:
                    enemy.x = enemy.temp_x
                    enemy.y = enemy.temp_y
                    enemy.shot = False


        #ENEMY MOVEMENT
        if not enemies[0].shot:
            enemies[0].move("horizontal")
        if not enemies[1].shot:
            enemies[1].move("horizontal")
        if not enemies[2].shot:
            enemies[2].move("vertical")
        if not enemies[3].shot:
            enemies[3].move("vertical")
        

        keys = pygame.key.get_pressed()
        #PLAYER MOVEMENT
        if keys[pygame.K_w]:
            player.move("up")
        if keys[pygame.K_s]:
            player.move("down")
        if keys[pygame.K_d]:
            player.move("right")
        if keys[pygame.K_a]:
            player.move("left")

        #BULLET SHOOTING
        if keys[pygame.K_i]:
            start = time.time()
            if ready:
                start_temp = start
                ready = False
            if end - start_temp >= 0.5 or first_shot:
                bullets.append(Bullet(player.x, player.y, "up"))
                ready = True
                first_shot = False
        if keys[pygame.K_k]:
            start = time.time()
            if ready:
                start_temp = start
                ready = False
            if end - start_temp >= 0.5 or first_shot:
                bullets.append(Bullet(player.x, player.y, "down"))
                ready = True
                first_shot = False
        if keys[pygame.K_l]:
            start = time.time()
            if ready:
                start_temp = start
                ready = False
            if end - start_temp >= 0.5 or first_shot:
                bullets.append(Bullet(player.x, player.y, "right"))
                ready = True
                first_shot = False
        if keys[pygame.K_j]:
            start = time.time()
            if ready:
                start_temp = start
                ready = False
            if end - start_temp >= 0.5 or first_shot:
                bullets.append(Bullet(player.x, player.y, "left"))
                ready = True
                first_shot = False
                
            
    
    pygame.quit()


if __name__ == "__main__":
    main()
