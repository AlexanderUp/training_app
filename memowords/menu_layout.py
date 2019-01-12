# encoding:utf-8
# menu layout for MemoWords kivy framework application

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import config


class MenuLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(MenuLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='MenuLayout'))
        self.add_widget(Button(text='Add new word', on_press=self.btn_add_word_pressed))
        self.add_widget(Button(text='See added words', on_press=self.btn_see_added_words_pressed))
        self.add_widget(Button(text='Start test', on_press=self.btn_start_test_pressed))

    def btn_add_word_pressed(self, *args, **kwargs):
        print('Add word pressed')
        config.sm.current = 'AddWordScr'

    def btn_see_added_words_pressed(self, *args, **kwargs):
        print('See added words pressed')
        config.sm.current = 'DictionaryScr'

    def btn_start_test_pressed(self, *args, **kwargs):
        print('Start test pressed')
        config.sm.current = 'TestScr'
