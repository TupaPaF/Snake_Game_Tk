from threading import Thread
from time import sleep
import random


class Bait:
    def __init__(self, canvas, level):
        self.x = random.randrange(10, 520, 15) - 2.5
        self.y = random.randrange(10, 520, 15) - 2.5
        self.canvas = canvas
        self.time_to_move = 12-level*2
        self.timer = self.time_to_move
        self.size = 15

        self.item = canvas.create_rectangle(self.x - self.size / 2,
                                            self.y - self.size / 2,
                                            self.x + self.size / 2,
                                            self.y + self.size / 2,
                                            fill='green')
        
        Thread(target=self.auto_move).start()

    def move(self):
        self.timer = self.time_to_move
        self.canvas.move(self.item, -self.x, -self.y)
        self.x = random.randrange(10, 520, 15) - 2.5
        self.y = random.randrange(10, 520, 15) - 2.5
        self.canvas.move(self.item, self.x, self.y)

    def get_position(self):
        coords = self.canvas.coords(self.item)
        return (coords[2] - coords[0]) / 2 + coords[0], (coords[3] - coords[1]) / 2 + coords[1]

    def auto_move(self):
        while True:
            while self.timer>0:
                self.timer -= 1
                sleep(1)
            else:
                self.move()
