class Component:
    """Physical model of a robot component
    """
    def __init__(self, model, mass, ix, iy, colour='black'):
        assert os.fileexists(model)
        self.model = model
        self.mass = mass
        self.ix = ix
        self.iy = iy


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
    self.components = []
    self.joints = {}

    def __init__(self, p, origin, components, joints, orientation=(0,0,0)):
        self.p = p 

        jointIndices = {}
        n = 0
        for j in self.joints:
            jointIndices['-'.join(j)] = n

        
        fn = "tmp" 
        self.model = p.loadURDF(f"{fn}.urdf", origin, orientation)

    def.setJoint(self, joint, target):
        jointIndex = self.jointsIndices[joint]
        self.p.setJointMotorControl2(self.model, jointIndex, p.POSITION_CONTROL, targetPosition=target)
