from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

# 自作クラス
from rpgmap import RPGMap
from enemy import EntryEnemy
from show_status import PlayerStatusWidget
from player import Player


# メインの画面
class RPGApp(Widget):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)

        # ステータスの配置
        status_widget = PlayerStatusWidget()
        self.add_widget(status_widget)

        # Mapの配置
        self.rpg_map = RPGMap()
        self.add_widget(self.rpg_map)

        # キーボード
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self.keyboard.bind(on_key_down=self._on_keyboard_down)
        self.keyboard.bind(on_key_up=self._on_keyboard_up)
        
        # Playerの配置
        self.player = Player()
        self.add_widget(self.player)

        # 敵の配置
        self.place_enemy()

       
        # self.bind(on_enemy_defeated=self.respawn_enemy)

    def respawn_enemy(self, instance):
        # 敵が倒されたときに新しい敵を生成して配置する
        enemy = EntryEnemy(pos=(100 * (len(self.enemies) +  1),  150))
        enemy.bind(on_enemy_defeated=self.respawn_enemy)
        self.enemies.append(enemy)
        self.add_widget(enemy)
        

    def place_enemy(self):
        self.enemies = []  # Enemyインスタンスを格納するリスト
        for i in range(3): 
            enemy = EntryEnemy(pos=(100 * (i + 1), 150))
            
            # 敵が倒されたときに再生成するためのリスナーを追加
            enemy.bind(on_enemy_defeated=self.respawn_enemy)
            self.enemies.append(enemy)
            self.add_widget(enemy)

    def on_touch_up(self, touch):
        self.player.velocity = Vector(0, 0)

    def update(self, dt):
        self.player.move(self.rpg_map)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        key = keycode[1]  # キーボードイベントのキーを取得
        if key == 'up':
            self.player.velocity_y = 2
        elif key == 'down':
            self.player.velocity_y = -2
        elif key == 'left':
            self.player.velocity_x = -2
        elif key == 'right':
            self.player.velocity_x = 2
    
    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard.unbind(on_key_up=self._on_keyboard_up)
        self.keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'up' or keycode[1] == 'down':
            self.player.velocity_y = 0
        elif keycode[1] == 'left' or keycode[1] == 'right':
            self.player.velocity_x = 0

class RPGGame(App):
    def build(self):
        game = RPGApp()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

# ウィンドウのサイズを設定
Window.size = (665, 600)
if __name__ == '__main__':
    RPGGame().run()
