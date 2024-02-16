from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window

# プレイヤーキャラクタークラス
class Player(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# メインの画面
class RPGMap(Widget):
    player = Player(source='player_image.gif')  # プレイヤーのGIF画像を指定

    def __init__(self, **kwargs):
        super(RPGMap, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self.keyboard.bind(on_key_down=self._on_keyboard_down)
        self.keyboard.bind(on_key_up=self._on_keyboard_up)

        with self.canvas:
            self.background = Rectangle(source='background_image.png', pos=self.pos, size=Window.size)
        self.player.size = (50, 50)  # プレイヤーのサイズを設定
        self.player.pos = (100, 100)  # プレイヤーの初期位置を設定
        self.add_widget(self.player)

    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard.unbind(on_key_up=self._on_keyboard_up)
        self.keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.player.velocity_y = 5
        elif keycode[1] == 's':
            self.player.velocity_y = -5
        elif keycode[1] == 'a':
            self.player.velocity_x = -5
        elif keycode[1] == 'd':
            self.player.velocity_x = 5

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'w' or keycode[1] == 's':
            self.player.velocity_y = 0
        elif keycode[1] == 'a' or keycode[1] == 'd':
            self.player.velocity_x = 0

    def update(self, dt):
        self.player.move()

# アプリケーションクラス
class RPGApp(App):
    def build(self):
        game = RPGMap()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    RPGApp().run()
