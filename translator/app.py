# encoding:utf-8
# kivy framework training app
# https://ru.smedialink.com/razrabotka/kross-platformennoe-prilozhenie-perevodchik-na-frejmforke-kivy-chast-1/
# https://github.com/nikolay-kovalenko91/translator_app_with_kivy

from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')

# class TranslatorApp(App):
#     title = 'Translator'
#     root_widget = None
#
#     def initialize_app(self):
#         self.root_widget = Button(text='Test')
#
#     def build(self):
#         self.initialize_app()
#         return self.root_widget

from screens.screenmanager import sm, screens
from kivy.uix.screenmanager import ScreenManagerException

class TranslatorApp(App):
    title = 'Translator'
    screen_manager = None

    def initialize_app(self):
        self.screen_manager = sm
        self.switch_screen('main')

    def switch_screen(self, screen_name):
        if screen_name in screens.keys():
            screen = screens[screen_name](name=screen_name)
            self.screen_manager.switch_to(screen)
            return
        else:
            raise ScreenManagerException('Screen {} not found'.format(screen_name))

    def build(self):
        self.initialize_app()
        return self.screen_manager

if __name__ == '__main__':
    TranslatorApp().run()
