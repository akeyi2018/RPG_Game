from kivy.event import EventDispatcher
from kivy.properties import StringProperty

class MyCustomClass(EventDispatcher):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_test')
        self.register_event_type('on_enemy_defeated')

    def on_test(self, *args, **kwargs):
        pass

    def on_enemy_defeated(self):
        print('敵が倒されました')

#     def trigger_event(self):
#         self.dispatch('on_my_custom_event')

def on_my_custom_event(instance):
    print("My custom event was triggered with value:")

my_instance = MyCustomClass()
# my_instance.bind(on_test=lambda __, *args, **kwargs: print('on_test', args, kwargs))

# my_instance.dispatch('on_test')
print('-------------------')
# my_instance.dispatch('on_test', 12, 34, kivy='awesome', python='awesome')

my_instance.bind(on_enemy_defeated=on_my_custom_event)
my_instance.dispatch('on_enemy_defeated')
# on_my_custom_event(1)

