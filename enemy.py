from kivy.uix.image import Image
from kivy.animation import Animation
import random

class Enemy(Image):
    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.size = (50, 50)
        self.anim = Animation()
        self.randomize_animation()
        self.anim.repeat = True
        self.anim.start(self)

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
            duration=5)  # ランダムな位置に移動するアニメーションを作成
        self.anim.bind(on_complete=lambda *args: self.randomize_animation())
        self.anim.start(self)
        self.anim.bind(on_progress=self.check_collision)

    def check_collision(self, widget, progress, test):
        # ここでEnemyの位置を更新し、Playerとの衝突をチェックする
        self.x = self.pos[0]  # Enemyのx座標を更新
        self.y = self.pos[1]  # Enemyのy座標を更新
        if self.parent is not None and self.parent.player is not None:
            player = self.parent.player
            if self.collide_widget(player):
                self.parent.show_battle_popup()
