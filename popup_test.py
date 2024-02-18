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

kivy.require('2.2.0')

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')

Builder.load_file('popup.kv')

from kivy.uix.image import Image

class PopupD(Popup):
    labels = ListProperty()
    images = ListProperty()

    def __init__(self, title, labels, images, **kwargs):
        super(PopupD, self).__init__(**kwargs)
        self.title = title
        self.labels = labels
        self.images = images

    def on_open(self):
        for text, source in zip(self.labels, self.images):
            inner_layout = BoxLayout(orientation='vertical')
            
            label = Label(text=text)
            inner_layout.add_widget(label)
            
            image = Image(source=source)
            inner_layout.add_widget(image)

            self.ids.content.add_widget(inner_layout)


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
        # image_paths = [
        #     './enemy_image/enemy_01.gif',
        #     './enemy_image/enemy_02.gif'
        #     ]
        # enemy_name_list = ['goblin',
        #                    'wizard'
        #                 ]
        self.popup = PopupD('battle screen', enemy_name_list, image_paths)
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