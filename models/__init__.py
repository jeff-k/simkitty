from os import path
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
    joints = []
    components = []
    name = None

    def __init__(self, p, origin, orientation=(0,0,0)):
        self.p = p 
        self.jointIndices = {}
        n = 0
        urdf_joints = []

        for parent, child in self.joints:
            xyz, rpy, axis, servo = self.joints[(parent, child)]
            self.jointIndices[f"{parent}-{child}"] = n
            urdf_joints.append((parent, child, xyz, rpy, axis, servo))
            n += 1
      
        with open('models/quadruped.urdf') as template_:
            template = jinja2.Template(template_.read())

        urdf = template.render(name=self.name,\
                scale=0.01, components=self.components,\
                joints=urdf_joints)

        print(urdf)
        self.model = p.loadURDF(self.urdf, origin, orientation)


    def setJoint(self, joint, target):
        jointIndex = self.jointsIndices[joint]
        self.p.setJointMotorControl2(self.model, jointIndex, p.POSITION_CONTROL, targetPosition=target)
