# encoding:utf-8
# add word layout for MemoWords kivy framework application

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


import config


class UpperBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(UpperBarLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Button(text='Menu', size_hint=(.25, None), on_press=self.btn_menu_pressed, height=config.HEIGHT))
        self.add_widget(Label(text='AddWordLayout', size_hint=(.5, None), height=config.HEIGHT))
        self.add_widget(Widget(size_hint=(.25, None), height=config.HEIGHT))

    def btn_menu_pressed(self, *args, **kwargs):
        print('Menu button pressed')
        config.sm.current = 'MenuScr'
        return None


class InputLayout(GridLayout):

    def __init__(self, *args, **kwargs):
        super(InputLayout, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.height = config.HEIGHT * self.rows
        self.add_widget(Label(text='Enter word', size_hint=(.25, None), height=config.HEIGHT))
        self.add_word = TextInput(hint_text='New word...', multiline=False, size_hint=(.75, None), height=config.HEIGHT)
        self.add_widget(self.add_word)
        self.add_widget(Label(text='Translation', size_hint=(.25, None), height=config.HEIGHT))
        self.word_translation = TextInput(hint_text='...and it\'s translation.', multiline=False, size_hint=(.75, None), height=config.HEIGHT)
        self.add_widget(self.word_translation)


class ButtonLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(ButtonLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.btn_clear = Button(text='Clear', size_hint=(.5, None), height=config.HEIGHT)
        self.add_widget(self.btn_clear)
        self.btn_add_word = Button(text='Add word', size_hint=(.5, None), height=config.HEIGHT)
        self.add_widget(self.btn_add_word)


class AddWordLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(AddWordLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(UpperBarLayout(size_hint=(1.0, None)))
        self.input_layout = InputLayout(size_hint=(1.0, None))
        self.add_widget(self.input_layout)
        self.info_label = Label(text='Awaiting input...')
        self.add_widget(self.info_label)
        self.button_layout = ButtonLayout(size_hint=(1.0, None))
        self.add_widget(self.button_layout)

        self.input_layout.add_word.bind(on_text=self.test)
        self.input_layout.word_translation.bind(on_text=self.test)
        self.button_layout.btn_clear.bind(on_press=self.btn_clear_pressed)
        self.button_layout.btn_add_word.bind(on_press=self.btn_add_word_pressed)

    def btn_clear_pressed(self, *args, **kwargs):
        print('btn_clear_pressed')
        self.input_layout.add_word.text = ''
        self.input_layout.word_translation.text = ''
        return None

    def btn_add_word_pressed(self, *args, **kwargs):
        print('btn_add_word_pressed')
        if self.input_layout.add_word.text and self.input_layout.word_translation.text:
            config.dictionary.add_word(self.input_layout.add_word.text, self.input_layout.word_translation.text)
            print('Word "{}" added; translation - {}'.format(self.input_layout.add_word.text, self.input_layout.word_translation.text))
            self.btn_clear_pressed(*args, **kwargs)
            self.info_label.text = ' Previous word successfully inputed! Awaiting new one...'
        else:
            print('Empty strings not allowed!')
        return None

    def test(self, instance, value=None, *args, **kwargs):
        print('Instance: {}, value: {}'.format(instance, value))
        if 'text' in dir(instance):
            print('Text entered: {}'.format(instance.text))
        return None
