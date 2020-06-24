from . import Quadruped, Component, Servo

body = Component('opencat/files/cat-body-v2.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), scale=0.01)
tibia = Component('opencat/files/cat-tibia-mg90s.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='blue')
left_femur = Component('opencat/files/left-femur.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='red')
right_femur = Component('opencat/files/right-femur.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='red')
neck = Component('opencat/files/neck.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='blue')
head = Component('opencat/files/skull.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='green')
tail = Component('opencat/files/tail.stl', 1.0, (-0.1, 0.0, 1.0), (0.0, 0.0, 0.0), colour='green')

mg90d = Servo(pi, 1.0, 1.0, 1.0, 1.0)

class Opencat(Quadruped):
    self.components = [
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
            
    self.joints = {
        ('body', 'neck'): mg90d,
        ('body', 'left_arm'): mg90d,
        ('body', 'right_arm'): mg90d,
        ('body', 'left_leg'): mg90d,
        ('body', 'right_leg'): mg90d,
        ('body', 'tail'): mg90d,
        ('neck', 'head'): mg90d,
        ('left_arm', 'left_hand'):, mg90d,
        ('right_arm', 'right_hand'): mg90d,
        ('left_leg', 'left_foot'): mg90d,
        ('right_leg', 'right_foot'): mg90d,
    }
