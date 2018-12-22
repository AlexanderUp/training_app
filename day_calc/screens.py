# encoding:utf-8
# screens for kivy framework application calculated dates with leap years
# had been taken into account

from kivy.uix.screenmanager import Screen
from kivy.graphics import Color
from kivy.graphics import Rectangle


try:
    from main_layout import MainLayout
    from add_layout import AddLayout
except ImportError as err:
    print('Can\'t import input layouts')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Layouts imported succsessfully')


class MainScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        main_screen = MainLayout()
        self.add_widget(main_screen)
        main_screen.bind(pos=self.update_rect, size=self.update_rect)
        with main_screen.canvas.before:
            Color(0.3, 0.5, 0.5, 1.0)
            self.rect = Rectangle(size=main_screen.size, pos=main_screen.pos)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class AddScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(AddScreen, self).__init__(**kwargs)
        self.add_widget(AddLayout())
