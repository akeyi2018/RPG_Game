from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class BattleScreen(Popup):
    def __init__(self, **kwargs):
        super(BattleScreen, self).__init__(**kwargs)
        # ポップアップ内のコンテンツを作成
        content = Button(text='Attack!', size_hint=(None, None), size=(200, 200))
        content.bind(on_press=self.dismiss)  # ボタンが押されたときにポップアップを閉じる
        self.title = 'Battle Screen'
        self.size_hint = (None, None)
        self.size = (400, 400)
        self.auto_dismiss = False  # ポップアップを自動的に閉じないように設定
        self.add_widget(content)  # ポップアップにコンテンツを追加

class RPGApp(App):
    def build(self):
        # ボタンを作成し、クリック時にポップアップを表示する
        button = Button(text='Show Battle Screen')
        button.bind(on_press=self.show_battle_screen)
        return button

    def show_battle_screen(self, instance):
        # ポップアップを表示
        battle_screen = BattleScreen()
        battle_screen.open()

if __name__ == '__main__':
    RPGApp().run()
