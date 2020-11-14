"""Quadruped template
"""
from os import path
import tempfile
import jinja2

class Component:
    """Physical model of a robot component
    """
    def __init__(self, model, mass, ix, iy, colour='black'):
        assert path.isfile(model)
        self.model = model
        self.colour = colour
        self.mass = mass
        self.ixx = ix[0]
        self.ixy = ix[1]
        self.ixz = ix[2]
        self.iyy = iy[0]
        self.iyz = iy[1]
        self.izz = iy[2]


class Servo:
    """Represent servo motor dynamics
    """
    def __init__(self, dof, effort, velocity, friction, damping):
        self.upper = dof/2
        self.lower = -dof/2
        self.effort = effort
        self.velocity = velocity
        self.friction = friction
        self.damping = damping


class Quadruped:
    """abstract Quadruped class
    """
    joints = {}
    components = []
    name = None

    def __init__(self, env, origin, orientation=(0, 0, 0)):
        self.env = env
        self.joint_indices = {}
        urdf_joints = []

        for index, (parent, child) in enumerate(self.joints):
            xyz, rpy, axis, servo = self.joints[(parent, child)]
            self.joint_indices[f"{parent}-{child}"] = index
            urdf_joints.append((parent, child, xyz, rpy, axis, servo))
            index += 1

        with open('models/quadruped.urdf') as template_:
            template = jinja2.Template(template_.read())

        urdf = template.render(name=self.name,\
                scale=0.01, components=self.components,\
                joints=urdf_joints)
        with tempfile.NamedTemporaryFile(mode='w', suffix='urdf') as tf:
            print(urdf, file=tf)
            self.model = env.loadURDF(tf.name, origin, orientation)


    def set_joint(self, joint, target):
        joint_index = self.joint_indices[joint]
        self.env.setJointMotorControl2(self.model,\
                joint_index, self.env.POSITION_CONTROL, targetPosition=target)
