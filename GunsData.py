from ursina import *

class GunsData:
    aimCoords = (0,0,0)
    nameGun = ""
    def __init__(self, nameGun, aimCoords, position, rotation, parent, camera):
        self.position = position
        self.rotation = rotation
        self.nameGun = nameGun
        self.aimCoords = aimCoords
        self.parent = parent
        self.camera = camera


    def logTest(self):
        print("Log Test")


    def basicInit(self):
        self.animationsStates() 

    def animationsStates(self):
        self.idle_Pistol = Animation("assets/Pistol", fps=12,Loop=False, autoplay=True)
        self.a=Animator(
            animations={
            "Idle": self.idle_Pistol
            })
        self.idle_Pistol.parent = self.camera
        self.idle_Pistol.position = self.idle_Pistol.position + Vec3(.8, -.3, 1)
        self.idle_Pistol.scale = 1
       # self.idle_Pistol.rotation = self.idle_Pistol.rotation + self.camera.rotation
    def update(self):
        self.position = self.parent.position + Vec3(0, 0, 5)
       # self.rotation = self.camera.rotation + Vec3(180,0,180)

    def Shoot(self):
        self.a.state = "Idle"
       # self.idle_Pistol.rotation = self.camera.rotation

