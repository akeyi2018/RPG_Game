from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

class PlayerStatusWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(PlayerStatusWidget, self).__init__(**kwargs)
        
        # 枠の描画
        with self.canvas:
            Color(0.5, 0.5, 0.5, 1)  # 枠の色をグレーに設定
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # フォントファイルの指定
        font_path = 'NotoSansSC-Regular.ttf'

        # プレイヤーステータスを表示するラベルを作成
        self.player_name_label = Label(text="プレイヤー名: 勇者", font_name=font_path, font_size=20, size_hint=(None, None), pos_hint={'x': 0.1, 'top': 0.9})
        self.hp_label = Label(text="HP: 100", font_name=font_path, font_size=20, size_hint=(None, None), pos_hint={'x': 0.1, 'top': 0.8})
        self.mp_label = Label(text="MP: 50", font_name=font_path, font_size=20, size_hint=(None, None), pos_hint={'x': 0.1, 'top': 0.7})
        self.level_label = Label(text="レベル: 1", font_name=font_path, font_size=20, size_hint=(None, None), pos_hint={'x': 0.1, 'top': 0.6})
        
        # ラベルをレイアウトに追加
        self.add_widget(self.player_name_label)
        self.add_widget(self.hp_label)
        self.add_widget(self.mp_label)
        self.add_widget(self.level_label)

class RPGApp(App):
    def build(self):
        # プレイヤーステータスを表示するウィジェットを追加
        return PlayerStatusWidget()

if __name__ == '__main__':
    RPGApp().run()
