from kivy.base import runTouchApp
from kivy.factory import Factory

lvl = ['***************',
       '*             *',
       '* *** *** *** *',
       '*  *   *   *  *',
       '*             *',
       '***************']

layout = Factory.BoxLayout(orientation='vertical')
for lvlrow in lvl:
    row = Factory.BoxLayout(orientation='horizontal')
    layout.add_widget(row)
    for block in lvlrow:
        if block == '*':
            row.add_widget(Factory.Button(size_hint=(None, None)))
        else:
            row.add_widget(Factory.Widget(size_hint=(None, None)))

runTouchApp(layout)