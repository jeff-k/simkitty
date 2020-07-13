"""Opencat specification
"""
from math import pi
from models import Quadruped, Component, Servo

body = Component('models/opencat/cat-body-v2.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0))
tibia = Component('models/opencat/cat-tibia-mg90s.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='blue')
left_femur = Component('models/opencat/left-femur.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='red')
right_femur = Component('models/opencat/right-femur.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='red')
neck = Component('models/opencat/neck.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='blue')
head = Component('models/opencat/skull.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='green')
tail = Component('models/opencat/tail.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='green')

mg90d = Servo(pi, 1.0, 1.0, 1.0, 1.0)

class Opencat(Quadruped):
    components = [
        ('body', body),
        ('neck', neck),
        ('head', head),
        ('left_arm', tibia),
        ('right_arm', tibia),
        ('left_leg', tibia),
        ('right_leg', tibia),
        ('left_hand', left_femur),
        ('right_hand', right_femur),
        ('left_foot', left_femur),
        ('right_foot', right_femur),
        ('tail', tail),
    ]

    joints = {
        ('body', 'neck'): ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('body', 'left_arm'): ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('body', 'right_arm'): ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('body', 'left_leg'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('body', 'right_leg'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('body', 'tail'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('neck', 'head'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('left_arm', 'left_hand'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('right_arm', 'right_hand'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('left_leg', 'left_foot'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
        ('right_leg', 'right_foot'):  ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), mg90d),
    }
