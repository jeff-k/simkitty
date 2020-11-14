import pybullet as p
import math
import pybullet_data

from models.opencat import Opencat

physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-9.8)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")

orientation = p.getQuaternionFromEuler([0,0,0])


cat = Opencat(p, (0, 0, 1), orientation)

joint_controls = {}
for joint in cat.joints:
    jn = '-'.join(joint)
    print(jn)
    joint_controls[jn] = p.addUserDebugParameter(jn, -0.7, 0.7, 0)

print("joints")
print(cat.joints)

while True:
    for joint in joint_controls:
        cat.set_joint(joint, p.readUserDebugParameter(joint_controls[joint]))
    p.stepSimulation()

print("done")
p.disconnect()
