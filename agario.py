# AGAR.IO
import pygame
import random
import math
import time

# Basic game settings
name_of_player = input("What is your name?:  ")
number_of_bots = int(input('With how many bots you want to play?:   '))
number_of_foods = 500

# initialize all imported pygame modules + text for game over
pygame.init()
pygame.font.init()

# Set screen size properties
width_screen = 1300
height_screen = 900
screen = pygame.display.set_mode((width_screen, height_screen))
pygame.display.set_caption("Agar Python")

# text middle of screen
def print_something(text):
    used_font = pygame.font.SysFont('freesansbold.ttf', 150)
    text_surface = used_font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = ((width_screen/2), (height_screen/2))
    screen.blit(text_surface, text_rect)

# Generating random colors
colors = []
for i in range(100):
    red_colour = random.randint(0, 255)
    green_colour = random.randint(0, 255)
    blue_colour = random.randint(0, 255)
    colors.append((red_colour, green_colour, blue_colour))

# Time counter
time_zero = float(pygame.time.get_ticks()) / 1000.
current_time = float(pygame.time.get_ticks()) / 1000.

# colors for background and text
colour_background = (255, 255, 255)
colour_text = (0, 0, 0)

# the maximum time step
maxdt = 0.002


class Vector2D:
    """Class that introduces a new 'data type', being a vector for 2D space. It handles basic operations such as
    addition, subtraction, multiplication and also normalization and calculation of magnitude"""
    # set elements of a vector
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def magnitude(self): return math.sqrt(self.x**2 + self.y**2)

    def normalize(self): return Vector2D(self.x / self.magnitude(),
                                         self.y / self.magnitude())

    def add(self, vector_to_add):
        return Vector2D(self.x + vector_to_add.x, self.y + vector_to_add.y)

    def subtract(self, vector_to_subtract_with):
        return Vector2D(self.x - vector_to_subtract_with.x,
                        self.y - vector_to_subtract_with.y)

    def multiply(self, factor):
        return Vector2D(self.x * float(factor), self.y * float(factor))


class MovingObject:
    """Superclass that handles generic behaviour for every moving object on the screen. This includes: moving from
    its own location towards a destination, updating the size of the object based on whether it has eaten an enemy or
    piece of food and drawing the circle on the screen"""
    def __init__(self, radius, object_id):
        self.id = object_id
        self.radius = radius
        self.area = math.pi * radius**2
        self.x = random.randint(radius, width_screen-radius)
        self.y = random.randint(radius, height_screen-radius)

        self.base_speed = 250
        self.minimum_speed = 100

        self.location = Vector2D(self.x, self.y)
        self.color_fill = random.choice(colors)
        self.color_stroke = random.choice(colors)

    # We use destination=Vector2D(0, 0) to tell the method that destination is of type
    #   Vector2D to allow for recognition of methods in PyCharm
    def move(self, destination=Vector2D(0, 0), speed_modifier=1.):
        """This method moves the object from its current position towards its destination by a tiny bit"""
        # get the direction vector from its current position to its destination
        direction = destination.subtract(self.location).normalize()

        # determine the velocity (scalar). This decreases with increase of the area of the object
        velocity = max([self.minimum_speed, speed_modifier * self.base_speed / math.sqrt(self.radius)])
        # multiply the direction with velocity to get the velocity vector
        velocity_vector = direction.multiply(velocity)
        # update it's current position
        self.location = self.location.add(velocity_vector.multiply(dt))
        self.x = self.location.x
        self.y = self.location.y

    def update_size(self):
        """This method checks if the area of the circle needs to be updated. First it checks if a piece of food is
        touching the circle. If so, the food is eaten (A.k.a deleted) and the area is increased.

        Similar, it also checks if an enemy (other moving object) is eaten. If the enemy is slighty smaller than this
        object it is eaten, and the area of the current object is updated. It checks also if the player was eaten. If
        so, a game over text appears. If not, a new enemy is created for in the game"""
        # Check for every food in the game if it is being eaten by the this moving object
        for i in range(len(foods_in_game)):
            distance_to_food = foods_in_game[i].location.subtract(self.location).magnitude()

            # Check if the piece of food is touching the circle
            if distance_to_food <= self.radius:
                # The new area of this object is the sum of its old area and the area of the piece of food
                area_food = math.pi * foods_in_game[i].radius**2
                self.area = area_food + self.area
                self.radius = int(math.sqrt(self.area/math.pi))
                del foods_in_game[i]
                break

        # Check for every moving object, if this moving object can eat another moving object
        for moving_object in moving_objects_in_game:
            # Check if the enemy is smaller than this one, and whether the other object is not this object
            if moving_object.radius + 5 < self.radius and moving_object.id != self.id:
                distance_to_enemy = moving_object.location.subtract(self.location).magnitude()

                # Check whether the enemy is touching the circle of the this object
                if distance_to_enemy <= self.radius:
                    self.area = moving_object.area + self.area
                    self.radius = int(math.sqrt(self.area/math.pi))

                    # Get the ID of the object that is going to be removed, to assign it to a new bot
                    new_object_id = moving_object.id

                    # Check if the enemy is the player. If so, show game over screen
                    if moving_object.id == 0:
                        print_something("Game Over!")
                        pygame.display.update()
                        time.sleep(1000)

                    # Remove the eaten bot
                    moving_objects_in_game.remove(moving_object)
                    # Create a new bot to replace it
                    moving_objects_in_game.append(Bot(new_object_id))

    def draw(self):
        """Draws the circle to represent the object"""
        # Draw the stroke of the circle
        pygame.draw.circle(screen, self.color_stroke, [int(self.x), int(self.y)], self.radius)
        # Draw the inner part of the circle
        pygame.draw.circle(screen, self.color_fill, [int(self.x), int(self.y)], self.radius)

    def update(self):
        """Updates the state of the moving object"""
        self.update_size()
        self.move()
        self.draw()


class Player(MovingObject):
    """Subclass that represents the player. It inherits from MovingObject"""
    def __init__(self):
        # Use __init__ of MovingObject
        super().__init__(radius=20, object_id=0)

    def move(self):
        """Moves the player towards the cursor on the screen"""
        # get mouse cursor position
        x_position_cursor, y_position_cursor = pygame.mouse.get_pos()
        # set the destination to move to
        destination = Vector2D(x_position_cursor, y_position_cursor)
        super().move(destination)


class Bot(MovingObject):
    """Subclass to represent a computer controlled object (called a bot). It inherits from MovingObject"""
    def __init__(self, object_id):
        # use __init__ from MovingObject. Assign the radius randomly, but based on the player's current size
        radius = random.randint(10, player.radius + 5)
        super().__init__(radius, object_id)

        # initialize a destination for the bot to move to
        self.destination = Vector2D(random.randint(100, width_screen-100), random.randint(100, height_screen-100))

    def move(self):
        """Moves the bot towards a random destination. If the player gets close, it either runs away (if the player is
        bigger) or follows the player to eat it (the player is smaller)"""
        # initialize a factor to reduce or increase the speed
        speed_modifier = 1

        # the heading from the bot to the player
        direction_to_player = player.location.subtract(self.location)
        distance_to_player = direction_to_player.magnitude()
        distance_to_destination = self.destination.subtract(self.location).magnitude()

        # if the random selected destination is (almost) reached, assign the bot a new random destination
        if distance_to_destination < 15:
            self.destination = Vector2D(random.randint(100, width_screen-100),
                                        random.randint(100, height_screen-100))
        # if the player is close and smaller than the bot, set the destination equal to the player position to chase
        # the player
        elif distance_to_player < 200 and self.radius > (player.radius + 5):
            self.destination = player.location
        # if the player is close but the player is bigger than the but, run away in the opposite direction. The bot
        # gets a penalty to its velocity for doing so
        elif distance_to_player < 200 and self.radius < (player.radius - 5):
            speed_modifier = 0.65
            self.destination = self.location.add(direction_to_player.multiply(-1))
        # if the bot reaches the borders of the screen, assign it a new random destination to move to
        else:
            if self.x + self.radius < 0:
                self.destination = Vector2D(random.randint(100, width_screen-100), random.randint(100, height_screen-100))
            elif self.x + self.radius > width_screen:
                self.destination = Vector2D(random.randint(100, width_screen-100), random.randint(100, height_screen-100))
            elif self.y - self.radius < 0:
                self.destination = Vector2D(random.randint(100, width_screen-100), random.randint(100, height_screen-100))
            elif self.y + self.radius > height_screen:
                self.destination = Vector2D(random.randint(100, width_screen-100), random.randint(100, height_screen-100))

        # call the method from the superclass to actually perform the movement
        super().move(self.destination, speed_modifier)


class Food:
    """Generates food particles and the choose a random position to deploy them, code also deploys them"""
    def __init__(self):
        """This will generate a random x position, y position, color and radius for the food"""
        self.radius = random.randint(5, 8)
        self.x = random.randint(self.radius, width_screen-self.radius)
        self.y = random.randint(self.radius, height_screen-self.radius)

        self.location = Vector2D(self.x, self.y)
        self.colour = random.choice(colors)

    def draw(self):
        """This methods draws a particle on the screen"""
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)

'''The game loop starts here'''
player = Player()                                                   # create an instance of Player
moving_objects_in_game = [Bot(x+1) for x in range(number_of_bots)]  # create an x amount of instances of Bot
# All moving objects are stored in a list, insert the player in the beginning of the list
moving_objects_in_game.insert(0, player)

foods_in_game = [Food() for x in range(number_of_foods)]
doquit = False
while doquit == False:
    current_time = float(pygame.time.get_ticks()) / 1000.
    # Determine the time step between frames
    dt = min((current_time - time_zero) * 2, maxdt)
    # Draw the background
    screen.fill(colour_background)
    # Because no other event functions of PyGame are called, this needs to be called
    pygame.event.pump()
    for ev in pygame.event.get():
            keys = pygame.key.get_pressed()
            if ev.type == pygame.QUIT:
                print("Quit event!")
                doquit = True 
                
            elif keys[pygame.K_ESCAPE]:
                print("Quit event!")
                doquit = True
                
    # Create new food particles to replace the eaten ones
    if len(foods_in_game) < number_of_foods:
        foods_in_game.append(Food())
    # draw every food particle in the game
    for f in foods_in_game:
        f.draw()

    # Update the position of the player and the bots
    for obj in moving_objects_in_game:
        obj.update()

    # Player is big enough, so it wins the game
    if player.radius > 200:
        print_something("Good job!")
        pygame.display.update()
        time.sleep(1000)

    # Print text for name
    used_font_name = pygame.font.SysFont('freesansbold.ttf', int(3.5 * player.radius / len(name_of_player)))
    text_name = used_font_name.render(name_of_player, True, (0, 0, 0))
    text_rect_name = text_name.get_rect()
    text_rect_name.center = (player.x, player.y)
    screen.blit(text_name, text_rect_name)

    # Update the screen, all the draw commands are now actually performed
    pygame.display.flip()
