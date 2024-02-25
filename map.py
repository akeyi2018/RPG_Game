from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.behaviors import ButtonBehavior 

class ImageButton(ButtonBehavior, Image):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
  
    def on_press(self):  
        print ('pressed', self.text)

class Map(Widget):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.tile_size = 50 # タイルのサイズを設定
        self.map_data = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
        self.tile_images = {
            0: './background_image/sougen2.png',  
            1: './background_image/miti2.png',  
            2: './background_image/yama.png', 
        }

        self.update_map()

    def update_map(self):
        self.clear_widgets()  # 既存のタイルをすべて削除

        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                tile_image_path = self.tile_images.get(tile)
                if tile_image_path:
                    tile_image = ImageButton(text=f'{tile}',source=tile_image_path)
                    tile_image.size = (self.tile_size, self.tile_size)
                    tile_image.pos = (x * self.tile_size, (len(self.map_data) - 1 - y) * self.tile_size)
                    self.add_widget(tile_image)

    def is_valid_move(self):
        move_list = ['0','1']
        stop_list = ['2']
        player = self.parent.player
        for img_bt in self.children:
            if img_bt.collide_widget(player):
                if img_bt.text in move_list:
                    return True
                elif img_bt.text in stop_list:
                    return False
                else:
                    return False

class RPGApp(Widget):
    def __init__(self, **kwargs):
        super(RPGApp, self).__init__(**kwargs)

        self.rpg_map = Map()
        self.add_widget(self.rpg_map)

class RPGGame(App):
    def build(self):
        game = RPGApp()
        return game

if __name__ == '__main__':
    RPGGame().run()