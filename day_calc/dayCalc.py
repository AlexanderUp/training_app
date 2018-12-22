# encoding:utf-8
# calculate days between two dates with leap years been taken into account


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'resizable', '0')

import sys


print("*" * 125)


try:
    from screens import MainScreen
    from screens import AddScreen
except ImportError as err:
    print('Can\'t import screens')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Screens imported successfully')


class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='MainScr'))
        sm.add_widget(AddScreen(name='AddScreen'))
        return sm


if __name__ == '__main__':
    print('Args rcvd: {}'.format(sys.argv))
    DayCalcApp().run()
