from kivy.uix.image import Image
from kivy.animation import Animation
import random
from kivy.event import EventDispatcher

# 自作クラス
from battle import BattleScreen

class EntryEnemy(Image, EventDispatcher):
    # 静的なカウンタを使用して一意のIDを生成
    enemy_id_counter =   0

    def __init__(self, **kwargs):
        super(EntryEnemy, self).__init__(**kwargs)
        # 敵が倒されるイベントを登録しておく
        self.register_event_type('on_enemy_defeated')
        self.size = (50, 50)
        self.anim = Animation()
        self.randomize_animation()
        self.anim.repeat = True
        self.anim.start(self)
        # IDを割り当て
        self.id = EntryEnemy.enemy_id_counter
        EntryEnemy.enemy_id_counter +=   1

    def randomize_animation(self):
        # 3種類の敵のGIF画像パスをリストで定義
        enemy_gifs = [
            './enemy_image/enemy_01.gif',
            './enemy_image/enemy_02.gif',
            './enemy_image/enemy_03.gif'
            ]
        random_gif = random.choice(enemy_gifs)  # ランダムに1つのGIF画像を選択
        self.source = random_gif  # 選択されたGIF画像を敵の画像として設定
        self.pos = (random.randint(50, 900), random.randint(50, 300))  # ランダムな位置に敵を配置
        self.anim = Animation(
            pos=(random.randint(50, 900),
                 random.randint(50, 300)),
            duration=60)  # ランダムな位置に移動するアニメーションを作成
        # self.anim.bind(on_complete=lambda *args: self.randomize_animation())
        self.anim.start(self)
        self.anim.bind(on_progress=self.check_collision)

    def check_collision(self, widget, progress, test):
        # ここでEnemyの位置を更新し、Playerとの衝突をチェックする
        self.x = self.pos[0]  # Enemyのx座標を更新
        self.y = self.pos[1]  # Enemyのy座標を更新
        if self.parent is not None and self.parent.player is not None:
            player = self.parent.player
            if self.collide_widget(player):
                self.show_battle_popup()

    def show_battle_popup(self):
        # アニメーションを停止する
        self.anim.stop(self)
        
        # check_collision  メソッドのアニメーションを停止
        self.anim.unbind(on_progress=self.check_collision)
        # ポップアップウィンドウを作成
        battle_screen = BattleScreen(self)
        battle_screen.open()
        battle_screen.bind(on_dismiss=self.resume_animation)

    def resume_animation(self, instance):
        # self.remove_widget(self)
        self.anim.start(self)
        # self.anim.bind(on_progress=self.check_collision)

    def on_enemy_defeated(self):
        print('敵が倒された')
        pass

    def remove_enemy(self):
        # 敵を管理しているウィジェットから敵を削除する処理を実装
        if self.parent is not None:
            self.parent.remove_widget(self)
            # 敵が倒されたことを通知
            self.dispatch('on_enemy_defeated')

