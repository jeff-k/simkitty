import pybullet as p
import math
import pybullet_data

from models.opencat import Opencat

physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-9.8)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")

orientation = (0.0, 0.0, 2.0)
orientation = p.getQuaternionFromEuler([0,0,0])

knee = p.addUserDebugParameter('Knee', -0.7, 0.7, 0)

cat = Opencat(p, origin, orientation)

while True:
    cat.setLeftLeg(p.readUserDebugParameter(knee))
    p.stepSimulation()

print("done")
p.disconnect()
