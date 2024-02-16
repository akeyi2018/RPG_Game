from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App

class Player(Image):
    # NumericPropertyの定義
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    veloc = ReferenceListProperty(velocity_x,velocity_y)

    def on_velocity_x(self, instance, value):
        # NumericPropertyが変更されたときに呼び出されるコールバック関数
        print("x property changed to:", value)

    def on_velocity_y(self, instance, value):
        # NumericPropertyが変更されたときに呼び出されるコールバック関数
        print("y property changed to :", value)

    def move(self):
        # 未調査
        print(self.pos)


class RPGApp(Widget):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self.keyboard.bind(on_key_down=self._on_keyboard_down)
        self.keyboard.bind(on_key_up=self._on_keyboard_up)

        self.player = Player(source='player_image.gif')
        self.player.size = (100, 100)
        self.player.pos = (50, 50)
        self.add_widget(self.player)
    
    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard.unbind(on_key_up=self._on_keyboard_up)
        self.keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'w' or keycode[1] == 's':
            self.player.velocity_y = 0
        elif keycode[1] == 'a' or keycode[1] == 'd':
            self.player.velocity_x = 0

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        key = keycode[1]  # キーボードイベントのキーを取得
        if key == 'w':
            self.player.velocity_y = 5
        elif key == 's':
            self.player.velocity_y = -5
        elif key == 'a':
            self.player.velocity_x = -5
        elif key == 'd':
            self.player.velocity_x = 5
        elif key == 'q':
            App.stop(self)
    # def update(self, dt):
        # pass

class RPGGame(App):
    def build(self):
        game = RPGApp()
        # Clock.schedule_interval(game.update, 1.0 / 30.0)
        return game
    
if __name__ == '__main__':
    RPGGame().run()
