# encoding:utf-8
# seventh kivy framework training app
# screen manager

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
