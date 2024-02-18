from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image

class RPGMap(Widget):
    def __init__(self, **kwargs):
        super(RPGMap, self).__init__(**kwargs)
        # self.size = (15, 15)  # マップのサイズを設定
        self.tile_size = 50 # タイルのサイズを設定
        self.map_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.tile_images = {
            0: 'yama.png',  # 0に対応する画像のパス
            1: 'sougen.png',  # 1に対応する画像のパス
            2: 'miti.png'
        }

        self.update_map()

    def update_map(self):
        self.clear_widgets()  # 既存のタイルをすべて削除

        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                tile_image_path = self.tile_images.get(tile)
                if tile_image_path:
                    tile_image = Image(source=tile_image_path)
                    tile_image.size = (self.tile_size, self.tile_size)
                    tile_image.pos = (x * self.tile_size, (len(self.map_data) - 1 - y) * self.tile_size)
                    self.add_widget(tile_image)        

    def is_valid_move(self, new_pos):
        # playerの座標
        x,y = new_pos
        # マップ座標へ変換
        # PlayerのX座標への補正(0カウントであるため、右側の壁１つ判定がおかしくなるため)
        if x > self.tile_size:
            map_x = int((x + self.tile_size) / self.tile_size)
        else:
            map_x = int(x / self.tile_size)
        # Playerの身長補正(タイルサイズ１つ)
        if y > self.tile_size:
            map_y = int((y + self.tile_size) / self.tile_size)
        else:
            map_y = int(y / self.tile_size)
        # print(f'x:{map_x} ,map_y: {map_y} map_data: {self.map_data[map_y][map_x]}')
        # 壁の場合
        if self.map_data[map_y][map_x] == 0:
            return False
        # 壁でない場合
        else:
            return True

class RPGApp(Widget):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)

        self.rpg_map = RPGMap()
        self.add_widget(self.rpg_map)

class RPGGame(App):
    def build(self):
        game = RPGApp()
        return game

# ウィンドウのサイズを設定
Window.size = (665, 535)

if __name__ == '__main__':
    RPGGame().run()