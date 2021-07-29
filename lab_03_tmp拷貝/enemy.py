import pygame
import math
import os
from settings import PATH

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        pygame.draw.rect(win,(0,255,0),[self.x-20,self.y-30,20,5])
        pygame.draw.rect(win, (255, 0, 0), [self.x, self.y - 30, 20, 5])

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = [Enemy()]  # don't change this line until you do the EX.3 

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        self.expedition.append(self.reserved_members.pop())



    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        global x, y, counter
        stride = 1
        self.x, self.y = self.path[self.path_pos] # x, y position
        x_b, y_b = self.path[self.path-pos + 1]
        distance= math.sqrt((self.x - x_b) ** 2 + (self.y - y_b) ** 2)
        max_count = int(distance/ stride)  # total footsteps that needed from A to B

        if (self.move_countc < max_count):
            unit_vector_x = (x_b - self.x) / distance
            unit_vector_y = (y_b - self.y) / distance
            delta_x = unit_vec_x * stride
            delta_y = unit_vec_y * stride

            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
            self.path_pos += 1


def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





