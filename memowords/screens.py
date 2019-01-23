# encoding:utf-8
# screens for MemoWords kivy framework application

from kivy.uix.screenmanager import Screen

from menu_layout import MenuLayout
from add_word_layout import AddWordLayout
from dictionary_layout import DictionaryLayout
from test_layout import TestLayout
from edit_layout import EditLayout


class MenuScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.add_widget(MenuLayout())


class AddWordScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(AddWordScreen, self).__init__(**kwargs)
        self.add_widget(AddWordLayout())


class DictionaryScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(DictionaryScreen, self).__init__(**kwargs)
        self.add_widget(DictionaryLayout())


class TestScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        self.add_widget(TestLayout())


class EditScreen(Screen):

    def __init__(self, *args, **kwargs):
        super(EditScreen, self).__init__(**kwargs)
        self.add_widget(EditLayout())
