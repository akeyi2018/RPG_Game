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
import os

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
        self.image_path = './enemy_image'
        self.title = ''
        self.entry_enemy_instance = entry_enemy_instance
        self.enemy_status = entry_enemy_instance.status
        self.enemy_image = os.path.join(os.getcwd(), self.image_path, self.enemy_status['IMG'])
        # print(self.enemy_image)
        # image 表示用
        self.images = [self.enemy_image]

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
        # 敵の名前
        self.ids.battle_message.text = f'{self.enemy_status["name"]}が現れました \n'
        for source in self.images:
            inner_layout = BoxLayout(
                orientation='vertical', height=150)
            
            image = Image(source=source)
            inner_layout.add_widget(image)

            self.ids.content.add_widget(inner_layout)
        
    def finish_battle(self):

        # モンスターを倒したメッセージ表示
        new_message = f'{self.enemy_status["name"]}を倒しました \n'
        self.reconstruct_battle_message(new_message)

        # モンスターが存在する場合
        if len(self.ids.content.children) > 0:
            # モンスターを削除
            self.ids.content.remove_widget(self.ids.content.children[0])

        # 戦闘終了ボタンの表示
        self.ids.finish_battle_button.text = '戦闘終了'
        self.ids.finish_battle_button.disabled = False
    
    def reconstruct_battle_message(self, new_message):
        current_message = self.ids.battle_message.text
        lines = current_message.split('\n')
        if len(lines) >  5:
            #  5行を超えた場合、最初の行を削除
            lines = lines[1:]
        self.ids.battle_message.text = '\n'.join(lines) + new_message

    def physical_attack(self):
        # ここに物理攻撃時の処理を記述します。
        attack_str = 8
        if len(self.ids.content.children) > 0:
            self.enemy_status['HP'] -= attack_str
            if self.enemy_status['HP'] > 0:
                new_message = f'{self.enemy_status["name"]}に{attack_str}のダメージを与えました \n'
                self.reconstruct_battle_message(new_message)
            else:
                # 戦闘終了処理
                self.finish_battle()    
        
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
        
        json_data = Enemy().generate_random_enemy()
        enemy = EntryEnemy(json_data)

        print(enemy.status)

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