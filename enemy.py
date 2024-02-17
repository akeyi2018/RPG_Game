from kivy.uix.image import Image
from kivy.animation import Animation
import random

class Enemy(Image):
    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.size = (50,50)
        self.anim = Animation()
        self.randomize_animation()
        self.anim.repeat = True
        self.anim.start(self)

    def randomize_animation(self):
        # 3種類の敵のGIF画像パスをリストで定義
        enemy_gifs = ['enemy_01.gif', 'enemy_02.gif', 'enemy_03.gif']
        random_gif = random.choice(enemy_gifs)  # ランダムに1つのGIF画像を選択
        self.source = random_gif  # 選択されたGIF画像を敵の画像として設定
        self.anim = Animation(
            pos=(random.randint(50, 900),
                 random.randint(50, 300)),
            duration=5)  # ランダムな位置に移動するアニメーションを作成
        self.anim.bind(on_complete=lambda *args: self.randomize_animation())
        # self.anim.stop_all(self)  # すべてのアニメーションを停止
        # self.anim.repeat = True
        self.anim.start(self)
