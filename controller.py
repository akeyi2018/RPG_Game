import pygame
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class GameController(GridLayout):
    def __init__(self, **kwargs):
        super(GameController, self).__init__(**kwargs)
        self.cols = 1  # 1列のレイアウトに変更

        self.label_button = Label(text="Button A: ", size_hint=(1, None))
        self.add_widget(self.label_button)

        self.label_button_b = Label(text="Button B: ", size_hint=(1, None))
        self.add_widget(self.label_button_b)

        self.label_x = Label(text="X-axis: ", size_hint=(1, None))
        self.add_widget(self.label_x)

        self.label_y = Label(text="Y-axis: ", size_hint=(1, None))
        self.add_widget(self.label_y)

        Clock.schedule_interval(self.update, 1/60)
        pygame.init()
        pygame.joystick.init()

        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()

    def update(self, dt):
        pygame.event.pump()

        # ゲームパッドのボタンの状態を取得
        button_a = self.gamepad.get_button(0)
        button_b = self.gamepad.get_button(1)

        # ゲームパッドのスティックの状態を取得
        axis_x = self.gamepad.get_axis(0)
        axis_y = self.gamepad.get_axis(1)

        self.label_button.text = f"Button A: {button_a}"
        self.label_button_b.text = f"Button B: {button_b}"
        self.label_x.text = f"X-axis: {axis_x}"
        self.label_y.text = f"Y-axis: {axis_y}"

class GameControllerApp(App):
    def build(self):
        return GameController()

if __name__ == '__main__':
    GameControllerApp().run()
