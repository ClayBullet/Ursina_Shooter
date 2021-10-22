from ursina import *
from GunsData import *
from ursina.prefabs.first_person_controller import FirstPersonController
from Enemy import *

class Player(Entity):
    def __init__(self,**kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent=self.controller)

        self.hand_gun = Entity(parent=self.controller.camera_pivot,
                            scale=1,
                            position=Vec3(-.5, -.5, 1.5),
                            rotation=Vec3(0, 0, 0),
                            visible=False)

        self.handGunData = GunsData("Hand Gun", (0.71, 0.2,0), self.hand_gun.position, self.hand_gun.rotation, self.controller, self.controller.camera_pivot)
        self.rifle_gun = Entity(parent=self.controller.camera_pivot,
                            scale=0.025,
                            position = Vec3(0.7, 0, 2),
                            rotation = Vec3(0, 0, 0),
                            model="SM_Wep_Shotgun_01.fbx",
                            texture='Emissive_02.png',
                            visible=False
                            )
        self.rifleGunData = GunsData("Rifle Gun", (0.71, 0.2,0), self.rifle_gun.position, self.rifle_gun.rotation, self.controller, self.controller.camera_pivot)

        self.weapons = [self.hand_gun, self.rifle_gun]
        self.gunsData = [self.handGunData, self.rifleGunData]
        self.current_weapon = 0
        self.entity_gun = self.hand_gun


    def switch_weapon(self):
        for i,v in enumerate(self.weapons):
            if i == self.current_weapon:
                self.entity_gun = v
                self.gunsData[i].basicInit()
                v.visible = True
            else:
                v.visible = False

    def input(self, key):
        try:
            self.current_weapon = int(key) - 1
            self.switch_weapon()
        except ValueError:
            pass

        if key == 'scroll up':
            self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
            self.switch_weapon()
        if key == 'scroll down':
            self.current_weapon = (self.current_weapon - 1) % len(self.weapons)
            self.switch_weapon()

        if key == 'right mouse down':
            self.aimSystem(True)
        elif key == 'right mouse up':
             self.aimSystem(False)

        if key == 'left mouse down':
            self.Shoot()


    def Shoot(self):
        self.handGunData.animationsStates()
        self.handGunData.Shoot()
        #self.animGun = self.Animation('Pistol', 12, false)
        #self.a = Animator(
        #                    animations = {
        #                        'shoot':animGun
        #                    })
        #self.a.state = 'shoot'

    def aimSystem(self, isAiming):
        for i,v in enumerate(self.gunsData):
            if i == self.current_weapon:
                if isAiming == True:
                    self.entity_gun.position -= v.aimCoords
                    camera.fov = 45
                else:
                    camera.fov = 90
                    self.entity_gun.position += v.aimCoords

    def update(self):
        self.controller.camera_pivot.y = 2 - held_keys['left control']







app = Ursina()

ground = Entity(model='plane',
                scale=20,
                texture='white_cube',
                texture_scale=(20,20,20),
                collider='mesh',
                color = color.red)

enemyProfile = enemy()
enemyProfile.changePos((0, 2, 0))



player = Player(position=(0, 10, 0))
cube = Entity(model='cube',
            position = (0, 2, -2),
            texture = 'white_cube')

enemyProfile.initAnimations()

def update():
  #  enemyProfile.look_at(player)
    rotation = enemyProfile.rotation.y + time.dt * 5
    enemyProfile.rotation.x = 0
    enemyProfile.rotation.z = 0
    enemyProfile.rotation = Vec3(0, rotation, 0)
    enemyProfile.look_at(Vec3(90,player.world_position.z,0))
    cube.look_at(player.world_position)
    worldPos = Vec3(player.world_position.x, player.world_position.y, player.world_position.z)
    enemyProfile.look_at(worldPos * -1)
    enemyProfile.rotation_x = 0
    enemyProfile.idleAnim()

app.run()
