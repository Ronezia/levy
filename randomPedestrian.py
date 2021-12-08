import random
import pygame
from pygame.math import Vector2

from p5 import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    core.memory("origine",Vector2(200,400))
    core.memory("positionVecteur",Vector2(0,0))
    core.memory("nomVecteur",Vector2(0, 200))
    print("Setup END-----------")


def run():

    core.cleanScreen()
    if core.getkeyPressValue() == 276:
        if core.memory("nomVecteur").angle_to(Vector2(0,1)) > -45:
            core.memory("nomVecteur",core.memory("nomVecteur").rotate(1))
    elif core.getkeyPressValue() == 275:
        if core.memory("nomVecteur").angle_to(Vector2(0,1))< 45:
            core.memory("nomVecteur",core.memory("nomVecteur").rotate(-1))
    elif core.getkeyPressValue() == 275 or 276 :
        if core.memory("nomVecteur").angle_to(Vector2(0,1))< 0.00001:
            if core.memory("nomVecteur").angle_to(Vector2(0, 1)) > 0.00001:
                core.memory("nomVecteur", core.memory("nomVecteur").rotate(-1))
        else:
            core.memory("nomVecteur").angle_to(Vector2(0,1)) > -0.00001
            core.memory("nomVecteur", core.memory("nomVecteur").rotate(1))
    print(core.getkeyPressValue())



    #core.printMemory()

    pygame.draw.line(core.screen,(255,255,255),core.memory("origine")+ core.memory("positionVecteur"),core.memory("origine")+ Vector2(core.memory("nomVecteur").x,-core.memory("nomVecteur").y))


core.main(setup, run)
