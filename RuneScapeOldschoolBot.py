#This is a script to mine iron/tin and fish shrimp in the videogame Oldschool Runescape. You can create as many bots as
#need by using threading. This bot works by taking a screenshot of your desktop and finding the correct pixel to press
#Based on the RGB-value.


from PIL import ImageGrab
import time
import random
import pyautogui as pg
import sys
import trace
import os
import threading




class Bot:
    def __init__(self, x_adjust, y_adjust):
        self.x_adjust = x_adjust
        self.y_adjust = y_adjust

    def click_ore_iron_1(self):
        if self.respawncheck((290 + self.x_adjust), 180+self.y_adjust):

            self.click(318+self.x_adjust+random.randrange(-4, 4), 181+self.y_adjust+random.randrange(-4,4), normal=True)

            number_while = 0
            while self.respawncheck((290 + self.x_adjust), 180+self.y_adjust) and number_while < 30:
                number_while += 1
                time.sleep(0.1)
                continue



    #Methods to mine ore.
    def random_ore_12(self):
     if self.inventory_bank_check() == False:
        if random.randrange(1,3) == 1:
            self.click_ore_tin_1()
        else:
            self.click_ore_tin_2()

    def click_ore_iron_2(self):

        if self.respawncheck(240 + self.x_adjust, 235 + self.y_adjust):

            self.click(262+self.x_adjust+random.randrange(-8, 8), 236+self.y_adjust+random.randrange(-8, 8), normal=True)
            number_while = 0
            while self.respawncheck(252+self.x_adjust, 236+self.y_adjust) and number_while < 30:
                number_while += 1
                time.sleep(0.1)
                continue


    def click_ore_tin_1(self):
        if self.respawncheck((240 + self.x_adjust), 243+self.y_adjust):

            self.click(247+self.x_adjust+random.randrange(-8, 8), 237+self.y_adjust+random.randrange(-8, 8), normal=True)
            number_while = 0
            while self.respawncheck((240 + self.x_adjust), 243+self.y_adjust) and number_while < 30:
                number_while += 1
                time.sleep(0.1)
                continue


    def click_ore_tin_2(self):

        if self.respawncheck(172 + self.x_adjust, 176 + self.y_adjust):
            self.click(182+self.x_adjust+random.randrange(-4, 4), 166+self.y_adjust+random.randrange(-4, 4), normal=True)
            number_while = 0
            while self.respawncheck(172+self.x_adjust, 176+self.y_adjust) and number_while < 30:
                number_while += 1
                time.sleep(0.1)
                continue



    def respawncheck(self, x_coordinate, y_coordinate):
        printscreen = ImageGrab.grab()
        x_coordinate_original = x_coordinate

        for i in range(200):
            x_coordinate += 1

            if i % 20 == 0:
                printscreen = ImageGrab.grab()

            if i % 30 == 0:

                y_coordinate += 1
                x_coordinate = x_coordinate_original
            coordinate = x_coordinate, y_coordinate


            r, g, b = printscreen.getpixel(coordinate)
            if r == 255 and g == 255 and b == 0:
                return False
        return True



#Methods to fish shrimp

    def click_shrimp_2(self):
        if self.check_shrimp_respawn(279 + self.x_adjust, 285 + self.y_adjust):
            self.click(279 + self.x_adjust, 285 + self.y_adjust, normal=True)

            number_while = 0
            while self.check_shrimp_respawn(276+self.x_adjust, 174+self.y_adjust) and number_while < 200:
                number_while += 1
                time.sleep(0.1)
                print(number_while)
                continue
        else:
            self.click(self.x_adjust + 262, self.y_adjust + 275, normal=True)
            time.sleep(10)

    def check_shrimp_respawn(self, x_coordinate, y_coordinate):
        printscreen = ImageGrab.grab()
        coordinate = x_coordinate, y_coordinate
        r, g, b = printscreen.getpixel(coordinate)
        if r == 88 and g == 107 and b == 149:
            return False
        else:
            return True

    def check_shrimp_respawn_area(self, x_coordinate=100, y_coordinate=251):
        printscreen = ImageGrab.grab()

        coordinate = self.x_adjust + x_coordinate, self.y_adjust + y_coordinate
        r, g, b = printscreen.getpixel(coordinate)
        for i in range(250):
            if r == 71 and g == 86 and b == 120:

                TureVar = True
                return self.x_adjust + 186 + i-1,  self.y_adjust + 251, TureVar

            else:
                coordinate = self.x_adjust + 186 + i, self.y_adjust + 251
                r, g, b = printscreen.getpixel(coordinate)
        TureVar = False
        return 0, 0, TureVar




#Methods to bank/drop items

    def bank(self):
        if self.inventory_bank_check():
            time.sleep(1)
            self.transport_bank()
            time.sleep(1)
            self.empty_inventory_bank()
            time.sleep(1)
            self.transport_bank_back()

    def invetory_check(self):
        printscreen = ImageGrab.grab()
        coordinate = 658+self.x_adjust, 220+self.y_adjust
        r, g, b = printscreen.getpixel(coordinate)

        if r != 73 and g != 64 and b != 53:
            return True


    def inventory_bank_check(self):
        printscreen = ImageGrab.grab()
        coordinate = 695 + self.x_adjust, 438 + self.y_adjust
        r, g, b = printscreen.getpixel(coordinate)
        if r == 75 and g == 66 and b == 58:
            return False
        if r == 69 and g == 60 and b == 51:
            return False
        if r == 72 and g == 62 and b == 53:
            return False
        if r == 73 and g == 64 and b == 53:
            return False
        return True


    def empty_inventory_bank(self):
        self.click(244 + self.x_adjust, 215 + self.y_adjust, right=True)
        time.sleep(1)
        self.click(244 + self.x_adjust, 240 + self.y_adjust, normal=True)
        time.sleep(1)

        y_coordinate = [86, 134, 186, 230]
        x_coordinate = [122, 179, 231, 283, 335, 390]

        for y in y_coordinate:
            if y != 86:
                self.click(67 + self.x_adjust, y + self.y_adjust, normal=True)
                time.sleep(0.2)
            for x in x_coordinate:
                self.click(x + self.x_adjust, y + self.y_adjust, normal=True)
                time.sleep(0.2)

        self.click(449 + self.x_adjust, 49 + self.y_adjust, normal=True)



    def drop_all(self):
        time.sleep(1)
        y_coordinate = [228, 265, 301, 338, 374, 407, 428]
        x_coordinate = [619, 656, 710]
        if self.inventory_bank_check():
            for y in y_coordinate:
                if y != 228:
                    self.click(576 + self.x_adjust + random.randrange(-5, 5), y + self.y_adjust + random.randrange(0, 4),
                               drop=True)
                    time.sleep(random.random())
                for x in x_coordinate:
                    self.click(x + self.x_adjust + random.randrange(-5, 5), y + self.y_adjust + random.randrange(0, 4), drop=True)
                    time.sleep(random.random())




    def drop(self):
        if self.invetory_check():
            self.click(620 + self.x_adjust + random.randrange(-4, 4), 220 + self.y_adjust + random.randrange(-4, 4), drop=True)
            self.click(658 + self.x_adjust + random.randrange(-4, 4), 220 + self.y_adjust + random.randrange(-4, 4), drop=True)


#Methods to lock resources to thread and click

    def click(self, x_coordinate, y_coordinate, bank=False, drop=False, normal=False, right=False):
        threadLock.acquire()
        if drop:
            self.drop_click(x_coordinate, y_coordinate)
        if normal:
            self.click_normal(x_coordinate, y_coordinate)
        if right:
            pg.moveTo(x_coordinate, y_coordinate)
            pg.click(button="right")
        threadLock.release()




    def drop_click(self, x_coordinate, y_coordinate):
        pg.moveTo(x_coordinate, y_coordinate)
        pg.click(button="right")
        time.sleep((random.random() / 6) + 0.1)
        pg.moveTo(x_coordinate, y_coordinate + 35)
        pg.click()

    def click_normal(self, x_coordinate, y_coordinate):
        pg.moveTo(x_coordinate, y_coordinate)
        pg.click()

    def pause(self):
        condition = random.randrange(0, 400)
        if condition == 2:
            time.sleep(random.randrange(80, 300))



    def click_shrimp_1(self):

            x_coordinate, y_coordinate, TrueVar = self.check_shrimp_respawn_area()

            if TrueVar:
                self.click(x_coordinate + 10 + random.randrange(0,8), y_coordinate+ random.randrange(-5, 15), normal=True)

                number_while = 0
                while TrueVar and number_while < 100 and self.inventory_bank_check() == False:
                    x_coordinate, y_coordinate, TrueVar = self.check_shrimp_respawn_area(x_coordinate + 10, y_coordinate)
                    number_while += 1
                    time.sleep(0.1)

#Method to afk without getting logged out

    def afk(self):
        self.click(617 + self.x_adjust + random.randrange(-30 ,30), 51 + self.y_adjust + random.randrange(-10,40), normal=True)
        time.sleep(random.randrange(0, 200))



#Functions for running the bots.

def bot_1():
    #x, y coordinate of upper right corner of Runelite-client
    x_adjust = 7
    y_adjust = 25
    bot = Bot(x_adjust, y_adjust)
    while True:
        bot.random_ore_12()
        bot.drop_all()


def bot_2():
    #x, y coordinate of upper right corner of Runelite-client
    x_adjust = 778
    y_adjust = 29
    bot = Bot(x_adjust, y_adjust)
    while True:
        bot.random_ore_12()
        bot.drop_all()





if __name__ == '__main__':
    threadLock = threading.Lock()
    t1 = threading.Thread(target=bot_1)
    t2 = threading.Thread(target=bot_2)

    t1.start()
    t2.start()

