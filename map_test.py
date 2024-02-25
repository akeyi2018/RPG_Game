# main.py

from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image  
from kivy.lang import Builder  
from kivy.app import App  
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout  

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        for j in range(9):
            for i in range(12):
                self.add_widget(ImageButton(text=f'id{i}_{j}', source='./background_image/sougen2.png',
                                        size_hint=(.2, .2), pos=(i*100, j*100)))
        # self.image_button = ImageButton(text='bt1', source='./background_image/floor_brick.png', size_hint=(.2, .2), pos=(300,  300))
        # self.add_widget(self.image_button)

class ImageButton(ButtonBehavior, Image):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.text = text
  
    def on_press(self):  
        print ('pressed', self.text)

# Builder.load_string("""  
# <RootWidget>:
#     GridLayout:  
#         ImageButton:
#             id: ibt_01
#             text: 'bt1'  
#             source:'./background_image/floor_brick.png'  
#             size_hint: .2, .2
#             pos: (100, 100) 
#         ImageButton:
#             id: ibt_02
#             text: 'bt2'  
#             source:'./background_image/floor_brick.png'  
#             size_hint: .2, .2
#             pos: (100, 150) 
#         ImageButton:
#             id: ibt_03
#             text: 'bt3'  
#             source:'./background_image/floor_brick.png'  
#             size_hint: .2, .2
#             pos: (150, 100)  
#         ImageButton:
#             id: ibt_04
#             text: 'bt4'  
#             source:'./background_image/floor_brick.png'  
#             size_hint: .2, .2
#             pos: (200, 200)   
# """)  

class The_AssignmentApp(App):  
    def build(self):  
        return RootWidget()

if __name__ == "__main__":  
    The_AssignmentApp().run() 
