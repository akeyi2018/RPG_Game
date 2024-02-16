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
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.tile_images = {
            0: 'floor_brick.png',  # 0に対応する画像のパス
            1: 'floor_carpet.png'  # 1に対応する画像のパス
        }

        self.update_map()

    def update_map(self):
        self.clear_widgets()  # 既存のタイルをすべて削除

        for y, row in enumerate(self.map_data):
            print(y)
            for x, tile in enumerate(row):
                tile_image_path = self.tile_images.get(tile)
                if tile_image_path:
                    tile_image = Image(source=tile_image_path)
                    tile_image.size = (self.tile_size, self.tile_size)
                    tile_image.pos = (x * self.tile_size, (len(self.map_data) - 1 - y) * self.tile_size)
                    self.add_widget(tile_image)

    def is_valid_move(self, new_pos):
        x,y = new_pos
        if x < 0 or y < 0 or x >= len(self.map_data[0]) * self.tile_size or y >= len(self.map_data) * self.tile_size:
            return False
        map_x = int(x / self.tile_size)
        map_y = int((len(self.map_data) * self.tile_size - y) / self.tile_size)
        return self.map_data[map_y][map_x] != 0  # 0が壁を表す場合は!= 0を使用

class RPGApp(Widget):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)

        self.rpg_map = RPGMap()
        self.add_widget(self.rpg_map)

class RPGGame(App):
    def build(self):
        game = RPGApp()
        # Clock.schedule_interval(game.update, 1.0 / 30.0)
        return game

# ウィンドウのサイズを設定
Window.size = (665, 535)

if __name__ == '__main__':
    RPGGame().run()