from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.image import Image
from kivy.vector import Vector

# プレイヤーキャラクタークラス
class Player(Image):
    # これをinitの中で宣言するとVectorエラーが表示される
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)  # ReferenceListPropertyを直接クラス変数として定義する

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (50, 50)  # デフォルトのサイズを設定
        self.pos = (50, 50)  # デフォルトの位置を設定
        self.source = 'player_image.gif'  # デフォルトの画像ソースを設定

    def move(self, rpg_map):
        # 次に移動する位置
        new_pos = Vector(*self.velocity) + self.pos  # ReferenceListPropertyをタプルとして渡すため、*を付けて展開する

        # 移動先が障害物でないかチェック
        if rpg_map.is_valid_move(new_pos):
            # 障害物でない場合→新しい位置にPlayerを移動する
            self.pos = new_pos

        # print('player:', self.pos)
