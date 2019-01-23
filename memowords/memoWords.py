# encoding:utf-8
# application for words memorization

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '640')
# Config.set('graphics', 'resizable', '0')

import sys

import config
from screens import MenuScreen
from screens import AddWordScreen
from screens import DictionaryScreen
from screens import TestScreen
from screens import EditScreen


class MemoWordsApp(App):

    def build(self):
        self.title = 'MemoWordsApp'
        config.sm.add_widget(MenuScreen(name='MenuScr'))
        config.sm.add_widget(AddWordScreen(name='AddWordScr'))
        config.sm.add_widget(DictionaryScreen(name='DictionaryScr'))
        config.sm.add_widget(TestScreen(name='TestScr'))
        config.sm.add_widget(EditScreen(name='EditScr'))
        return config.sm

    def on_stop(self, *args, **kwargs):
        try:
            # buttom clear to be pressed
            config.dictionary.close()
        except Exception as err:
            print('During closing the following error occured:')
            print(err)
        else:
            print('Shelve object successfully closed.')
        return None

if __name__ == '__main__':
    print("*" * 125)
    MemoWordsApp().run()
