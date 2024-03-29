from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.event import EventDispatcher

# 自作クラス
from map import Map
from enemy import EntryEnemy
from show_status import PlayerStatusWidget
from player import Player
from enemy_maneger import Enemy


# メインの画面
class RPGApp(Widget, EventDispatcher):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)
        self.register_event_type('on_generate_new_enemys')
        # ステータスの配置
        status_widget = PlayerStatusWidget()
        self.add_widget(status_widget)

        # Mapの配置
        self.rpg_map = Map()
        self.add_widget(self.rpg_map)

        # キーボード
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self.keyboard.bind(on_key_down=self._on_keyboard_down)
        self.keyboard.bind(on_key_up=self._on_keyboard_up)
        
        # Playerの配置
        self.player = Player()
        self.add_widget(self.player)

        # 敵の配置
        # self.enemys_num = 3
        # self.place_enemy_fix()
    
    def place_enemy_fix(self):
        self.enemies = []  # Enemyインスタンスを格納するリスト
        for i in range(self.enemys_num):
            # 敵のGIF
            enemy_status = Enemy().generate_random_enemy()
            enemy = EntryEnemy(json_data=enemy_status, pos=(100 * (i + 2)*1, 200))
            # 新しい敵が生成されたらバインドする
            enemy.bind(on_enemy_defeated= lambda instance: self.respawn_enemy(enemy))
            enemy.move_enemy_animation_fix()
            self.enemies.append(enemy)
            
            enemy.dispatch('on_enemy_generated')
            self.add_widget(enemy)

    def on_generate_new_enemys(self):
        # print('on_generate_new_enemys')
        for enemy in self.enemies:
            self.remove_widget(enemy)
        self.place_enemy_fix()

    # 敵再配置（敵が倒されたときに新しい敵を生成して配置する）
    def respawn_enemy(self, instance):

        print(f'x:{instance.x}: y:{instance.y}')
        print(f'play_x:{self.player.x}:play_y:{self.player.y}')
        
        enemy_status = Enemy().generate_random_enemy() 
        # 敵が倒されたときに新しい敵を生成して配置する
        enemy = EntryEnemy(json_data=enemy_status, pos=(self.player.x - 80,  200))

        # 敵が生成されたときにバインドする
        enemy.bind(on_enemy_generated=self.generate_enemy)
        # 新しい敵が生成されたらバインドする
        enemy.bind(on_enemy_defeated= lambda instance: self.respawn_enemy(enemy))
        enemy.move_enemy_animation_fix()
        # 新しい敵を生成して配置する
        self.enemies.append(enemy)
        enemy.dispatch('on_enemy_generated')
        self.add_widget(enemy)

    def generate_enemy(self, instance):
        pass

    def stop_all_enemy_animations(self):
        for enemy in self.enemies:
            enemy.stop_animation()

    def on_touch_up(self, touch):
        self.player.velocity = Vector(0, 0)

    def update(self, dt):
        self.player.move(self.rpg_map)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        key = keycode[1]  # キーボードイベントのキーを取得
        if key == 'up':
            self.player.source = './player_image/back.gif'
            self.player.event_key = key
            self.player.velocity_y = 2
        elif key == 'down':
            self.player.source = './player_image/front.gif'
            self.player.event_key = key
            self.player.velocity_y = -2
        elif key == 'left':
            self.player.source = './player_image/left.gif'
            self.player.event_key = key
            self.player.velocity_x = -2
        elif key == 'right':
            self.player.source = './player_image/right.gif'
            self.player.event_key = key
            self.player.velocity_x = 2
    
    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard.unbind(on_key_up=self._on_keyboard_up)
        self.keyboard = None

    # キーボードがupした場合、停止する
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
