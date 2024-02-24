# -*- coding: utf-8 -*-
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

kivy.require('2.3.0')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
resource_add_path('./font')
LabelBase.register(DEFAULT_FONT, 'NotoSansSC-Regular.ttf')
Builder.load_file('popup.kv')

from enemy import EntryEnemy
from enemy_maneger import Enemy

class CustomLayout(BoxLayout):
    pass

class BattleScreen(Popup):
    labels = ListProperty()
    images = ListProperty()
    image_paths = ListProperty()  #  インスタンス変数としてimage_pathsを追加

    # def __init__(self, title, labels, image_paths, **kwargs):
    def __init__(self, entry_enemy_instance, **kwargs):
        super(BattleScreen, self).__init__(**kwargs)
        self.title = ''
        self.entry_enemy_instance = entry_enemy_instance
        self.images = [self.entry_enemy_instance.source]
        self.labels = [self.entry_enemy_instance.enemy_name]

    def on_dismiss(self):
        # print('close')
        self.entry_enemy_instance.remove_enemy()
        # enemy = self.entry_enemy_instance.enemy
        # self.entry_enemy_instance.anim.start(self.entry_enemy_instance)

    def spinner_clicked(self,text):
        if text == 'ホイミ':
            self.handle_item1()
        elif text == 'メラ':
            self.handle_item2()
        self.ids.spinner_id.text = 'まほう'

    def handle_item1(self):
        # 項目1を選択した場合の処理
        # print("ホイミを唱えました")
        new_message = 'ホイミを唱えました \n'
        self.reconstruct_battle_message(new_message)

    def handle_item2(self):
        # 項目2を選択した場合の処理
        print("メラを唱えました")
        new_message = 'メラを唱えました \n'
        self.reconstruct_battle_message(new_message)
  

    def on_open(self):
        for text, source in zip(self.labels, self.images):
            inner_layout = BoxLayout(
                orientation='vertical', height=150)
            
            image = Image(source=source)
            inner_layout.add_widget(image)

            self.ids.content.add_widget(inner_layout)
        

    def del_monster(self):
        # モンスターを削除
        # モンスターが存在する場合
        if len(self.ids.content.children) > 0:
            self.ids.content.remove_widget(self.ids.content.children[0])
    
    def reconstruct_battle_message(self, new_message):
        current_message = self.ids.battle_message.text
        lines = current_message.split('\n')
        if len(lines) >  5:
            #  5行を超えた場合、最初の行を削除
            lines = lines[1:]
        self.ids.battle_message.text = '\n'.join(lines) + new_message

    def physical_attack(self):
        #   ここに物理攻撃時の処理を記述します。
        print("Physical attack executed!")
        new_message = 'Physical attack executed. \n'
        self.reconstruct_battle_message(new_message)
        
    def magical_attack(self):
        #   ここに魔法攻撃時の処理を記述します。
        print("Magical attack executed!")
        # self.replace_image(1, './enemy_image/black.png', 'New Label Text')
        new_message = 'Monster defeated. \n'
        self.del_monster()
        self.reconstruct_battle_message(new_message)  

class MainDisp(Widget):

    def __init__(self, **kwargs):
        super(MainDisp, self).__init__(**kwargs)

    def on_release(self):
        image_paths = [
            './enemy_image/enemy_01.gif',
            './enemy_image/enemy_02.gif',
            './enemy_image/enemy_03.gif'
            ]
        enemy_name_list = ['goblin',
                           'wizard',
                           'Snake Woman'
                        ]
        
        enemy_name, random_gif = Enemy().generate_random_enemy()
        enemy = EntryEnemy(source=random_gif, enemy_name=enemy_name)

        self.popup = BattleScreen(entry_enemy_instance=enemy)
        self.popup.open()

class MainDispApp(App):
    def __init__(self, **kwargs):
        super(MainDispApp, self).__init__(**kwargs)
        self.title = 'Popup Test'

    def build(self):
        return MainDisp()


if __name__ == '__main__':
    app = MainDispApp()
    app.run()