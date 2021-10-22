from ursina import *
import ursina.prefabs.animator
class enemy(Entity):

    def __init__(self):
        super().__init__(self)
      #  self.model='quad'
       # self.texture='Imp.jpg'
        self.scale=1
        self.position = Vec3(0, 0, 0)
       
    def changePos(self, position):
        self.position = position

    def initAnimations(self):
        self.animationsStates()

    def lookat(self, target):
            print(target)
            if target != Vec3(0,0,0):
                self.look_at(target)
                print(target)


    def changeTarget(self, targetForTake):
        self.currentTarget = targetForTake

    def animationsStates(self):
        self.idle = Animation('Doom_Imp', position = self.position, scale=self.scale, rotation=self.rotation, fps=2, loop=True, autoplay=True)
        self.shoot = Animation('Imp_Doom2', position = (0, 0, 0), scale=1, fps=2, loop=True, autoplay=True)

        #Entity(model='quad', color=color.red)
        #Entity(model='quad', color=color.green)
        self.anim = Animator(  
             animations = {  
                'idle' : self.idle, 
                'shoot' : self.shoot,
             },
             start_state = "idle"
        )
        self.anim.state = "idle"

    def idleAnim(self):
        self.idle.rotation = self.rotation
        self.anim.state = "idle"

