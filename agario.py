# AGAR.IO
import unittest
import pygame
import random
import math

name_of_player = input("What is your name?:  ")

# initialize all imported pygame modules + text for game over
pygame.init()
pygame.font.init()

# Set screen size an properties
width_screen = 1000
height_screen = 1000
screen = pygame.display.set_mode((width_screen,height_screen))
pygame.display.set_caption("Agar Python")

# text for game over
used_font_game_over = pygame.font.SysFont('freesansbold.ttf', 150)
text_surface = used_font_game_over.render('GAME OVER', True, (0,0,0))
text_rect = text_surface.get_rect()
text_rect.center = ((width_screen/2), (height_screen/2))


# Generating random colors for food
colors = []
i = 0
while i < 100:
    red_colour = random.randint(0, 255)
    green_colour = random.randint(0, 255)
    blue_colour = random.randint(0, 255)
    colors.append((red_colour, green_colour, blue_colour))
    i += 1

# Time counter
t0 = float(pygame.time.get_ticks()) / 1000.
tnow = float(pygame.time.get_ticks()) / 1000.

# VARIABLE
begin_food_list = []
colour_player = random.choice(colors)
colour_background = (255, 255, 255)
colour_text = (0, 0, 0)
food_radius = []
food_location = []
food_colour = []
food_x_coordinate = []
food_y_coordinate = []

x_player = width_screen/2
y_player = height_screen/2
position_player = [int(x_player),int(y_player)]

minimum_speed = 25
maximum_speed = 600
maxdt = 0.002
coefficient = 1.1


class Food:
    """Generates food particles and the choose a random position to deploy them, code also deploys them"""
    def __init__(self):
        """This will generate a random x position, y position, collor and radius for the food"""
        self.radius = random.randint(5,8)
        self.x_coordinate_food = random.randint(self.radius,width_screen-self.radius)
        self.y_coordinate_food = random.randint(self.radius,height_screen-self.radius)

        self.location = [self.x_coordinate_food, self.y_coordinate_food]
        self.colour = random.choice(colors)

        food_radius.append(self.radius)
        food_x_coordinate.append(self.x_coordinate_food)
        food_y_coordinate.append(self.y_coordinate_food)
        food_location.append(self.location)
        food_colour.append(self.colour)


class Player:
    "All atributes of the player will be coded here"
    def __init__(self):
        "This will generate all the standard parameters of the player"
        self.radius = 20
        self.new_radius_player = 20
        self.x_coordinate = random.randint(self.radius,width_screen-self.radius)
        self.y_coordinate = random.randint(self.radius,height_screen-self.radius)

        self.location = [self.x_coordinate, self.y_coordinate]
        self.colour = random.choice(colors)
        self.colour1 = random.choice(colors)
        self.new_bot1, self.new_bot2, self.new_bot3, self.new_bot4 = False, False, False, False

    def new_radius(self):
        """Determine if the player eats the food"""
        for i in range(len(food_location)):
            x_distance_food = self.x_coordinate - food_x_coordinate[i]
            y_distance_food = self.y_coordinate - food_y_coordinate[i]
            distance_food = math.sqrt(x_distance_food**2+y_distance_food**2)

            if distance_food <= self.radius:
                area_food = math.pi * food_radius[i] ** 2
                area_player = math.pi * self.new_radius_player ** 2
                new_area_player = area_food + area_player
                self.new_radius_player = math.sqrt(new_area_player/math.pi)
                self.radius = int(self.new_radius_player)
                del food_radius[i]
                del food_colour[i]
                del food_location[i]
                del food_x_coordinate[i]
                del food_y_coordinate[i]
                break

        if bot1.radius + 5 < self.radius:
            x_distance = bot1.x_coordinate - self.x_coordinate
            y_distance = bot1.y_coordinate - self.y_coordinate
            distance = math.sqrt(x_distance**2+y_distance**2)

            if distance <= self.radius:
                area_bot = math.pi * bot1.radius ** 2
                area_player= math.pi * self.new_radius_player ** 2
                new_area_player = area_player + area_bot
                print(str(area_bot) + ' + ' + str(area_player) + ' = ' +str(new_area_player))
                self.new_radius_player = math.sqrt(new_area_player/math.pi)
                self.radius = int(self.new_radius_player)
                self.new_bot1 = True
        if bot2.radius + 5 < self.radius:
            x_distance = bot2.x_coordinate - self.x_coordinate
            y_distance = bot2.y_coordinate - self.y_coordinate
            distance = math.sqrt(x_distance**2+y_distance**2)

            if distance <= self.radius:
                area_bot = math.pi * bot2.radius ** 2
                area_player= math.pi * self.new_radius_player ** 2
                new_area_player = area_player + area_bot
                print(str(area_bot) + ' + ' + str(area_player) + ' = ' +str(new_area_player))
                self.new_radius_player = math.sqrt(new_area_player/math.pi)
                self.radius = int(self.new_radius_player)
                self.new_bot2 = True
        if bot3.radius + 5 < self.radius:
            x_distance = bot3.x_coordinate - self.x_coordinate
            y_distance = bot3.y_coordinate - self.y_coordinate
            distance = math.sqrt(x_distance**2+y_distance**2)

            if distance <= self.radius:
                area_bot = math.pi * bot3.radius ** 2
                area_player= math.pi * self.new_radius_player ** 2
                new_area_player = area_player + area_bot
                print(str(area_bot) + ' + ' + str(area_player) + ' = ' +str(new_area_player))
                self.new_radius_player = math.sqrt(new_area_player/math.pi)
                self.radius = int(self.new_radius_player)
                self.new_bot3 = True
        if bot4.radius + 5 < self.radius:
            x_distance = bot4.x_coordinate - self.x_coordinate
            y_distance = bot4.y_coordinate - self.y_coordinate
            distance = math.sqrt(x_distance**2+y_distance**2)

            if distance <= self.radius:
                area_bot = math.pi * bot4.radius ** 2
                area_player= math.pi * self.new_radius_player ** 2
                new_area_player = area_player + area_bot
                print(str(area_bot) + ' + ' + str(area_player) + ' = ' +str(new_area_player))
                self.new_radius_player = math.sqrt(new_area_player/math.pi)
                self.radius = int(self.new_radius_player)
                self.new_bot4 = True

# NOG AANPASSEN, KLOPT NOG NIET MET DE ZIJKANTEN!!

    def move(self):
        x_position_cursor, y_position_cursor = pygame.mouse.get_pos()
        player_speed = max(minimum_speed, coefficient*maximum_speed/math.sqrt(self.radius))
        self.player_speed = player_speed

        if x_position_cursor - width_screen/2 == 0 or y_position_cursor - height_screen/2 == 0:
            x_position_cursor += 1
            y_position_cursor += 1

        if x_position_cursor < width_screen/2:
            speed_y = player_speed * -1 * math.sin(math.atan((y_position_cursor - height_screen/2)/(x_position_cursor - width_screen/2)))
            speed_x = player_speed * -1 * math.cos(math.atan((y_position_cursor - height_screen/2)/(x_position_cursor - width_screen/2)))
        elif x_position_cursor > width_screen/2:
            speed_y = player_speed * math.sin(math.atan((y_position_cursor - height_screen/2)/(x_position_cursor - width_screen/2)))
            speed_x = player_speed * math.cos(math.atan((y_position_cursor - height_screen/2)/(x_position_cursor - width_screen/2)))

        if self.x_coordinate < 0:
            speed_x = 0
            self.x_coordinate += 1
        elif self.x_coordinate > width_screen:
            speed_x = 0
            self.x_coordinate -= 1
        elif self.y_coordinate < 0:
            speed_y = 0
            self.y_coordinate += 1
        elif self.x_coordinate > height_screen:
            speed_y = 0
            self.y_coordinate -= 1

        self.x_coordinate += speed_x*dt
        self.y_coordinate += speed_y*dt

    def feed_players(self):
        pass

    def attack(self):
        pass

    def collision_explosion(self):
        pass

    def update_position(self):
        self.new_radius()
        self.move()
        self.collision_explosion()


class Bot:
    """This will generate random bots who will fight you in the game"""
    def __init__(self):
        self.radius = random.randint(10, player1.radius + 5)
        self.new_radius_bot = self.radius
        self.x_coordinate = random.randint(self.radius,width_screen-self.radius)
        self.y_coordinate = random.randint(self.radius,height_screen-self.radius)

        self.location = [self.x_coordinate, self.y_coordinate]
        self.colour = random.choice(colors)
        self.colour1 = random.choice(colors)
        self.speed_bot_y = 0
        self.speed_bot_x = 0
        self.angle = random.random() * 2 * math.pi

        self.bot_radius = []
        self.bot_x_coordinate = []
        self.bot_y_coordinate =[]
        self.bot_location = []
        self.bot_colour = []

        self.bot_radius.append(self.radius)
        self.bot_x_coordinate.append(self.x_coordinate)
        self.bot_y_coordinate.append(self.y_coordinate)
        self.bot_location.append(self.location)
        self.bot_colour.append(self.colour)
        self.game_over = False

    def new_radius(self):
        for i in range(len(food_location)):
            x_distance = self.x_coordinate - food_x_coordinate[i]
            y_distance = self.y_coordinate - food_y_coordinate[i]
            distance = math.sqrt(x_distance**2+y_distance**2)

            if distance <= self.radius:
                area_food = math.pi * food_radius[i] ** 2
                area_bot = math.pi * self.new_radius_bot ** 2
                new_area_bot = area_food + area_bot
                self.new_radius_bot = math.sqrt(new_area_bot/math.pi)
                self.radius = int(self.new_radius_bot)
                del food_radius[i]
                del food_colour[i]
                del food_location[i]
                del food_x_coordinate[i]
                del food_y_coordinate[i]
                break

        if self.radius > player1.radius + 5:
            x_distance = self.x_coordinate - player1.x_coordinate
            y_distance = self.y_coordinate - player1.y_coordinate
            distance = math.sqrt(x_distance**2+y_distance**2)
            if distance <= self.radius:
                area_player = math.pi * player1.radius ** 2
                area_bot = math.pi * self.new_radius_bot ** 2
                new_area_bot = area_player + area_bot
                self.new_radius_bot = math.sqrt(new_area_bot/math.pi)
                self.radius = int(self.new_radius_bot)
                screen.blit(text_surface, text_rect)
                self.game_over = True

    # WERKT NIET HELEMAAL MET OMHEINING, ligt aan verwijderd deel
    def move(self):
        bot_speed = max(minimum_speed, coefficient*maximum_speed/math.sqrt(self.radius))
        if abs(self.x_coordinate - player1.x_coordinate) < 200 and abs(self.y_coordinate - player1.y_coordinate) < 200 and self.radius > (player1.radius + 5):
            self.angle = math.atan((self.y_coordinate - player1.y_coordinate)/(self.x_coordinate - player1.x_coordinate))
            if player1.x_coordinate < self.x_coordinate:
                self.speed_bot_y = bot_speed * -1 * math.sin(self.angle)
                self.speed_bot_x = bot_speed * -1 * math.cos(self.angle)
            elif player1.x_coordinate > self.x_coordinate:
                self.speed_bot_y = bot_speed * math.sin(self.angle)
                self.speed_bot_x = bot_speed * math.cos(self.angle)

            self.x_coordinate += self.speed_bot_x*dt
            self.y_coordinate += self.speed_bot_y*dt

        else:
            if self.x_coordinate - self.radius < 0:
                self.angle += math.pi
                self.x_coordinate += 1

            elif self.x_coordinate + self.radius > width_screen:
                self.angle += math.pi
                self.x_coordinate -= 1

            elif self.y_coordinate - self.radius < 0:
                self.angle += math.pi
                self.y_coordinate += 1

            elif self.y_coordinate + self.radius > height_screen:
                self.angle += math.pi
                self.y_coordinate -= 1

            self.speed_bot_y = bot_speed * math.sin(self.angle)
            self.speed_bot_x = bot_speed * math.cos(self.angle)
            self.x_coordinate += self.speed_bot_x*dt
            self.y_coordinate += self.speed_bot_y*dt

    def update_position(self):
        self.new_radius()
        self.move()

# THE ACTUAL CODE
player1 = Player()
bot1 = Bot()
bot2 = Bot()
bot3 = Bot()
bot4 = Bot()

while True:
    tnow = float(pygame.time.get_ticks())/1000.
    dt = min((tnow-t0)*2, maxdt)
    screen.fill(colour_background)
    pygame.event.pump()

    # Making of the food particles in the beginning and when playing the game
    while len(food_location) < 500:
        food = Food()

    for j in range(len(food_location)):
        pygame.draw.circle(screen, food_colour[j], food_location[j], food_radius[j])

    player1.update_position()
    bot1.update_position()
    bot2.update_position()
    bot3.update_position()
    bot4.update_position()

    pygame.draw.circle(screen, player1.colour, (int(player1.x_coordinate), int(player1.y_coordinate)), player1.radius)
    pygame.draw.circle(screen, player1.colour1, (int(player1.x_coordinate), int(player1.y_coordinate)), int(6/7* player1.radius))

    if bot1.radius != 0:
        pygame.draw.circle(screen, bot1.colour, (int(bot1.x_coordinate), int(bot1.y_coordinate)), bot1.radius)
        pygame.draw.circle(screen, bot1.colour1, (int(bot1.x_coordinate), int(bot1.y_coordinate)), int(6/7* bot1.radius))
    if bot2.radius != 0:
        pygame.draw.circle(screen, bot2.colour, (int(bot2.x_coordinate), int(bot2.y_coordinate)), bot2.radius)
        pygame.draw.circle(screen, bot2.colour1, (int(bot2.x_coordinate), int(bot2.y_coordinate)), int(6/7* bot2.radius))
    if bot3.radius != 0:
        pygame.draw.circle(screen, bot3.colour, (int(bot3.x_coordinate), int(bot3.y_coordinate)), bot3.radius)
        pygame.draw.circle(screen, bot3.colour1, (int(bot3.x_coordinate), int(bot3.y_coordinate)), int(6/7* bot3.radius))
    if bot4.radius != 0:
        pygame.draw.circle(screen, bot4.colour, (int(bot4.x_coordinate), int(bot4.y_coordinate)), bot4.radius)
        pygame.draw.circle(screen, bot4.colour1, (int(bot4.x_coordinate), int(bot4.y_coordinate)), int(6/7* bot4.radius))

    while player1.new_bot1:
        bot1 = Bot()
        player1.new_bot1 = False
    while player1.new_bot2:
        bot2 = Bot()
        player1.new_bot2 = False
    while player1.new_bot3:
        bot3 = Bot()
        player1.new_bot3 = False
    while player1.new_bot4:
        bot4 = Bot()
        player1.new_bot4 = False
    while bot1.game_over:
        pygame.display.update()
    while bot2.game_over:
        pygame.display.update()
    while bot3.game_over:
        pygame.display.update()
    while bot4.game_over:
        pygame.display.update()

    # Text for name
    used_font_name = pygame.font.SysFont('freesansbold.ttf', int(3.5*player1.radius/len(name_of_player)))
    text_name = used_font_name.render(name_of_player, True, (0,0,0))
    text_rect_name = text_name.get_rect()
    text_rect_name.center = (player1.x_coordinate, player1.y_coordinate)
    screen.blit(text_name, text_rect_name)

    pygame.display.flip()
