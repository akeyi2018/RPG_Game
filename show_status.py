from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.label import Label

class PlayerStatusWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(PlayerStatusWidget, self).__init__(**kwargs)
        
        # 枠の描画
        with self.canvas:
            Color(1, 1, 1, 1)  # 枠の色を青に設定
            Line(circle=(30 - 10, 890 - 10, 10, -90, 0), width=2)
            # Line(points=[20, 890, 170, 890], width=2) # OK
            Line(circle=(180 - 10, 890 - 10, 10, 90, 0), width=2)
            Line(points=[20, 730, 170, 730], width=2) # OK
            Line(circle=(180 - 10, 750 - 10, 10, 90, 180), width=2)
            Line(points=[180, 880, 180, 740], width=2) # OK
            Line(circle=(30 - 10, 750 - 10, 10, 180, 270), width=2)
            Line(points=[10, 880, 10, 740], width=2) #ok
            Color(0, 0, 1, 1)  # 枠の色を青に設定
            self.rect = Rectangle(size=(165, 150), pos=(14, 735))
            self.rect = Rectangle(size=(150, 10), pos=(20, 885))
        
        # プレイヤーステータスを表示するラベルを作成し、キャンバス内に配置
        font_path = './font/NotoSansSC-Regular.ttf'
        self.player_name_label = Label(text="エンジニア Y", font_name=font_path,
                                    font_size=20, pos_hint={'center_x': 0.9, 'center_y': 8.85},
                                    halign='left')
        self.job = Label(text="職業: SE", font_name=font_path, font_size=20, 
                              pos_hint={'center_x': 0.8, 'center_y': 8.75},
                                    halign='left')
        self.hp_label = Label(text="HP: 100", font_name=font_path, font_size=20, 
                              pos_hint={'center_x': 0.8, 'center_y': 8.5},
                                    halign='left')
        self.mp_label = Label(text="MP: 50", font_name=font_path, font_size=20,
                              pos_hint={'center_x': 0.8, 'center_y': 8.25},
                                    halign='left')
        self.level_label = Label(text="レベル: 1", font_name=font_path, font_size=20,
                              pos_hint={'center_x': 0.8, 'center_y': 8.0},
                                    halign='left')
        
        # テキストサイズを自動計算して左揃えにする
        # self.player_name_label.text_size = self.player_name_label.size
        self.job.text_size = self.job.size
        self.hp_label.text_size = self.hp_label.size
        self.mp_label.text_size = self.mp_label.size
        self.level_label.text_size = self.level_label.size
        self.add_widget(self.player_name_label)
        self.add_widget(self.job)
        self.add_widget(self.hp_label)
        self.add_widget(self.mp_label)
        self.add_widget(self.level_label)

class RPGApp(App):
    def build(self):
        return PlayerStatusWidget()

if __name__ == '__main__':
    RPGApp().run()
