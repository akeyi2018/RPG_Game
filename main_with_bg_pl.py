from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image

# プレイヤーキャラクタークラス
class Player(Image):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# メインの画面
class RPGMap(Widget):
    player = Player(source='player_image.png')  # プレイヤーの画像を指定

    def __init__(self, **kwargs):
        super(RPGMap, self).__init__(**kwargs)
        with self.canvas:
            self.background = Rectangle(source='background_image.png', pos=self.pos, size=Window.size)
        self.player.size = (50, 50)  # プレイヤーのサイズを設定
        self.player.pos = (100, 100)  # プレイヤーの初期位置を設定
        self.add_widget(self.player)

    def on_touch_down(self, touch):
        self.player.velocity = Vector(touch.x - self.player.center_x, touch.y - self.player.center_y)

    def on_touch_up(self, touch):
        self.player.velocity = Vector(0, 0)

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
