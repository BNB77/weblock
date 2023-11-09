
import random
import pygame
from os import path

img_dir = path.join(path.dirname(__file__))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 55)
YELLOW = (255, 255, 0)

WIDTH = 480
HEIGHT = 600
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

def print_score(surface, score, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(score, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (30, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(random.choice(enemies_images), (30, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = 20
        self.rect.x = random.randint(20, WIDTH - 20)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.y = 20
            self.speedx = random.randint(-3, 3)
        if self.rect.right > WIDTH:
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.speedx = -self.speedx
            
        
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 7))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


background = pygame.image.load(path.join(img_dir, "purple.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
enemies_images = []
enemies_list = ['enemyBlack1.png', 'enemyBlue2.png', 'enemyGreen3.png', 'enemyRed4.png']
for img in enemies_list:
    enemies_images.append(pygame.image.load(path.join(img_dir, img)).convert())

background_rect = background.get_rect() 
died = 0
score = 1
flag = 0
bullets = pygame.sprite.Group()        
all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
for i in range(1):
    enemy = Enemy()
    all_sprites.add(enemy)
    all_enemies.add(enemy)
player = Player()
all_sprites.add(player)
#font = pygame.font.Font(none, 14)


done = True
while done:
    clock.tick(FPS)
    if score % 5 == 0 and flag == 0:
        enemy = Enemy()
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        flag = 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                player.shoot()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                score = 1
                all_sprites = pygame.sprite.Group()
                all_enemies = pygame.sprite.Group()
                player = Player()
                enemy = Enemy()
                all_sprites.add(enemy)
                all_enemies.add(enemy)
                all_sprites.add(player)
                died = 0

    hits = pygame.sprite.groupcollide(all_enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        score += 1
        flag = 0

    
    hits = pygame.sprite.spritecollide(player, all_enemies, True)
    if hits:
        died = 1
        
    if died == 0:     
        all_sprites.update()
        window.fill(BLACK)
        window.blit(background, background_rect)
        print_score(window, 'Score: ' + str(score - 1), 22, WIDTH - 40, 10)
        all_sprites.draw(window)
        pygame.display.flip()
    else:
        window.fill(BLACK)
        window.blit(background, background_rect)
        print_score(window, 'YOU DIED', 40, WIDTH // 2, HEIGHT // 2)
        print_score(window, 'Your score: ' + str(score - 1), 30, WIDTH // 2, HEIGHT // 2 + 40)
        print_score(window, 'Click r to restart', 20, WIDTH // 2, HEIGHT // 2 + 80)
        pygame.display.flip()
        
pygame.quit()

