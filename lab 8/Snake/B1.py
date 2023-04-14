import pygame
import random, time
from pygame.math import Vector2

pygame.init()

block_size = 35
menu_color = (255, 153, 255)
surface_size = (block_size*20+250, block_size*20+40)
count_column, count_row = 20, 20
zhylan_color = (204, 0, 204)
head_color = (102, 0, 102)
border_color = (255, 153, 255)
font_color = (0, 0, 0)
block_color1 = (255, 204, 255)
block_color2 = (255, 255, 255)
font_size = 30
ms = 150
image_heart1 = pygame.image.load(r"lab 8\Snake\heart.png")
image_heart = pygame.transform.scale(image_heart1, (35, 35))
masic = pygame.mixer.music.load(r"lab 8\Snake\music.mp3")
pygame.mixer.music.play(-1)

surface = pygame.display.set_mode(surface_size)
surface.fill(border_color)
clock = pygame.time.Clock()
done = False

# шрифт для меню
fonts = pygame.font.SysFont('Arial Black', font_size)

def draw_block(colour, column, row):
            pygame.draw.rect(surface, colour, [20+block_size*column, 20+row*block_size, block_size, block_size])


class ZHYLAN():
    def __init__(self):
        # позиция во время начала игры
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # нейтральное движение для змейки, где она стоит на одном месте
        self.direction = Vector2(0,0)
        self.new_block = False

    def draw_zhylan(self):
        # голова змейки
        draw_block(head_color, self.body[0].x, self.body[0].y)
        # тело змейки (отличаются по цветам)
        for block in self.body[1:]:
            draw_block(zhylan_color, block.x, block.y)         

    def move_zhylan(self):
        # если змейка скушала еду
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # копируем тело змеи без хвоста
            body_copy = self.body[:-1]
            # добавляем блок в напралении змейки в начале тела
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
    
    def reset(self):
        # перезапуск игры и позиция, где игра снова начинается
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)


class HEART():
    def __init__(self):
        self.random_spawn(10, 5)

    def random_spawn(self, x, y):
        # обновляет позицию еды
        self.pos = Vector2(x, y)
   
    def draw(self):
        # изображение еды для змейки
        surface.blit(image_heart, (int(self.pos.x * block_size+20) , int(self.pos.y * block_size+20)))


class MAIN():
    def __init__(self):
        self.zhylan = ZHYLAN()
        self.heart = HEART()
        self.score = 0
        self.level = 0
        # обновление каждые 150 миллисекунд 
        self.speed = 150
    
    def update(self):
        self.zhylan.move_zhylan()
        self.colission()
        self.death()

    def draw_game(self):
        self.zhylan.draw_zhylan()
        self.heart.draw()
        self.menu()
    
    # столкновение змейки с едой
    def colission(self):
        if self.heart.pos == self.zhylan.body[0]:
            x, y = self.random_location()
            self.heart.random_spawn(x, y)
            self.zhylan.new_block = True
            self.score += 1
            # каждые 4 очки увеличивает уровень и скорость 
            if self.score % 4 == 0:
                self.level += 1
                self.update_speed()

    def random_location(self):
        # задает рандомные координаты для еды
        x = random.randint(0, count_column - 1)
        y = random.randint(0, count_row - 1)
        while (Vector2(x,y) in self.zhylan.body):
            x = random.randint(0, count_column - 1)
            y = random.randint(0, count_row - 1)
        return x,y    

    def death(self):
        # змейка умирает, когда бьется об границы поля
        if not 0 <= self.zhylan.body[0].x < count_column or not 0<= self.zhylan.body[0].y < count_row:
            self.game_over()

        # чтобы змейка умирала, когда бьется об саму себя
        for block in self.zhylan.body[1:]:
            if block == self.zhylan.body[0]:
                self.game_over()

    # перезапуск игры, когда змейка умирает
    def game_over(self):
        self.speed = 150
        pygame.time.set_timer(pygame.USEREVENT, self.speed)
        self.level = 0
        self.score = 0
        self.zhylan.reset()

    def update_speed(self):
        # минус потому что мы обновляем время движения змейки
        self.speed -= self.speed//7
        pygame.time.set_timer(pygame.USEREVENT, self.speed)

    def menu(self):
        # рисуем меню на экране с текстом
        pygame.draw.rect(surface, menu_color, [block_size*count_column + 40, 0, 1000, 1000])
        score_text = fonts.render("score: " + str(self.score), True, font_color, menu_color)
        level_text = fonts.render("level: "+ str(self.level), True, font_color, menu_color)
        surface.blit(score_text, (block_size*20 + 50, 20))
        surface.blit(level_text, (block_size*20 + 50, 20 + font_size*2))


game = MAIN()


pygame.time.set_timer(pygame.USEREVENT, 150)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.USEREVENT:
            game.update()
        # меняем направление движения с клавишами
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.zhylan.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                game.zhylan.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                game.zhylan.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                game.zhylan.direction = Vector2(-1, 0)

    # нарисовать шахматное поле для змейки
    for row in range(count_row):
        for column in range(count_column):
            if (column+row) % 2 == 0:
                colour = block_color1
            else: colour = block_color2
            draw_block(colour, column, row)

    game.draw_game()

    pygame.display.flip()

    clock.tick(60)