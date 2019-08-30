import pygame
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

class Car:
    image_car = ['RacingCar01.png','RacingCar02.png','RacingCar03.png','RacingCar04.png','RacingCar05.png',\
                'RacingCar06.png','RacingCar07.png','RacingCar08.png','RacingCar09.png','RacingCar10.png',\
                'RacingCar11.png','RacingCar12.png','RacingCar13.png','RacingCar14.png','RacingCar15.png',\
                'RacingCar16.png','RacingCar17.png','RacingCar18.png','RacingCar19.png','RacingCar20.png',]

    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        self.image = ''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self):
        self.image = pygame.image.load(random.choice(self.image_car))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]
    
    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx
    
    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x+self.width > WINDOW_WIDTH or self.x <0:
            self.x -= self.dx

    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) and (self.y < car.y + car.height) and (self.y + self.height > self.y):
            return True
        else:
            return False

def draw_main_menu():
    draw_x = (WINDOW_WIDTH / 2) - 200
    draw_y = (WINDOW_HEIGHT / 2)
    image_intro = pygame.image.load('PyCar.png')
    screen.blit(image_intro, [draw_x, draw_y - 280])
    font_40 = pygame.font.SysFont('FixedSys', 40, True, False)
    font_40 = pygame.font.SysFont('FiexdSys', 40, True, False)
    text_title = font_40.render('PyCar : Racing Car Game', True, BLACK)
    screen.blit(text_title, [draw_x, draw_y])
    text_score = font_40.render('Score: ' + str(score), True, WHITE)
    screen.blit(text_score, [draw_x, draw_y + 70])
    text_start = font_40.render('Press Space Key to Start', True, RED)
    screen.blit(text_start, [draw_x, draw_y + 140])
    pygame.display.flip()

def draw_score():
    font_30 = pygame.font.SysFont('FixedSys', 30, True, False)
    text_score = font_30.render('Score:'+str(score), True, BLACK)
    screen.blit(text_score, [15, 15])


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pycar : Jinyoung Racing Car game")
    clock = pygame.time.Clock()
    # Game Sound
    pygame.mixer.music.load('race.wav')
    sound_crash = pygame.mixer.Sound('crash.wav')
    sound_engine = pygame.mixer.Sound('engine.wav')
    # Create User Racing Car 
    player = Car(WINDOW_WIDTH / 2, (WINDOW_HEIGHT - 150), 0, 0) 
    player.load_image() 

    # Create Computer Racing Car
    cars = []
    car_count = 3
    for i in range(car_count):
        x = random.randrange(0, WINDOW_WIDTH-55)
        y = random.randrange(-150, -50)
        car = Car(x, random.randrange(-150, -50), 0, random.randint(5, 10))
        car.load_image()
        cars.append(car)

    lanes = []
    lane_width = 10
    lane_height = 80
    lane_margin = 20
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width) /2 
    lane_y = -10
    for i in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin

    score = 0
    crash = True
    game_on = True

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

            if crash:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    crash = False
                    for i in range(car_count):
                        cars[i].x = random.randrange(0, WINDOW_WIDTH - cars[i].width)
                        cars[i].y = random.randrange(-150, -50)
                        cars[i].load_image()

                    player.load_image()
                    player.x = WINDOW_WIDTH / 2
                    player.dx = 0
                    score = 0
                    pygame.mouse.set_visible(False) # 마우스 안쓰도록
                    sound_engine.play()
                    sleep(5) # 사운드를 조금 들을 시간은 필요하니까
                    pygame.mixer.music.play(-1) # 반복 재생

            if not crash:
                if event.type == pygame.KEYDOWN: # 키가 눌렸을 때
                    if event.key == pygame.K_RIGHT:
                        player.dx = 4
                    elif event.key == pygame.K_LEFT:
                        player.dx = -4
                
                if event.type == pygame.KEYUP: # 키를 뗐을 때
                    if event.key == pygame.K_RIGHT:
                        player.dx = 0
                    elif event.key == pygame.K_LEFT:
                        player.dx = 0 
        
        screen.fill(GRAY)

        if not crash:
            for i in range(lane_count):
                pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10
                if lanes[i][1] > WINDOW_HEIGHT:
                    lanes[i][1] = -40 - lane_height 
            
            player.draw_image()
            player.move_x()
            player.check_out_of_screen()

            for i in range(car_count):
                cars[i].draw_image()
                cars[i].y += cars[i].dy
                if cars[i].y > WINDOW_HEIGHT:
                    score += 10
                    cars[i].x = random.randrange(0, WINDOW_WIDTH - cars[i].width)
                    cars[i].y = random.randrange(-150, -50)
                    cars[i].dy = random.randint(4, 9)
                    cars[i].load_image()

            for i in range(car_count):
                if player.check_crash(cars[i]):
                    crash = True
                    pygame.mixer.music.stop()
                    sound_crash.play()
                    sleep(2)
                    pygame.mouse.set_visible(True)
                    break

            draw_score()
            pygame.display.flip()

        else:
            draw_main_menu()
        
        clock.tick(60)
    
    pygame.quit()


