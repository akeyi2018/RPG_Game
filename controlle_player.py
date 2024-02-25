import pygame
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Character(Image):
    velocity = NumericProperty(5)

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self.source = './player_image/player_image.gif'
        self.size_hint = (None, None)
        self.size = (100, 100)
        # self.center = self.parent.center

    def on_velocity(self, instance, value):
        pass

    def move(self, axis_x, axis_y):
        self.x += axis_x * self.velocity
        # self.y += axis_y * self.velocity
        self.y -= axis_y * self.velocity

class GameControllerApp(App):
    def build(self):
        self.character = Character()
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        Clock.schedule_interval(self.update, 1/60)
        return self.character

    def update(self, dt):
        pygame.event.pump()
        axis_x = self.gamepad.get_axis(0)
        axis_y = self.gamepad.get_axis(1)
        self.character.move(axis_x, axis_y)

if __name__ == '__main__':
    GameControllerApp().run()
