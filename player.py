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
        self.source = './player_image/front.gif'  # デフォルトの画像ソースを設定
        self.event_key = ''

    def move(self, rpg_map):
        # Map範囲
        max_y = 400
        min_y = 0
        max_x = 950
        min_x = 0        
        # 次に移動する位置
        new_pos = Vector(*self.velocity) + self.pos  # ReferenceListPropertyをタプルとして渡すため、*を付けて展開する
        
        # # 移動先が障害物でないかチェック
        if rpg_map.is_valid_move():
            if new_pos[0] < min_x:
                new_pos[0] = min_x
            if new_pos[0] > max_x:
                new_pos[0] = max_x
            # Mapから出れないようにする（Y座標はマイナスに対して補正）
            if new_pos[1] < min_y:
                new_pos[1] = min_y
            if new_pos[1] > max_y:
                new_pos[1] = max_y
        #     # 障害物でない場合→新しい位置にPlayerを移動する
            self.pos = new_pos
        else:
            if self.event_key == 'right':
                self.pos[0] =  self.pos[0] - 5
            if self.event_key == 'down':
                self.pos[1] =  self.pos[1] + 5

            if self.event_key == 'up':
                self.pos[1] =  self.pos[1] - 5
            if self.event_key == 'left':
                self.pos[0] =  self.pos[0] + 5
