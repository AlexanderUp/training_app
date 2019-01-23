# encoding:utf-8
# menu layout for MemoWords kivy framework application

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput


import config


class UpperBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(UpperBarLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Button(text='Menu', size_hint=(.25, None), on_press=self.btn_menu_pressed, height=config.HEIGHT))
        self.add_widget(Label(text='TestLayout', size_hint=(.5, None), height=config.HEIGHT))
        self.btn_next = Button(text='Next', size_hint=(.25, None), height=config.HEIGHT)
        self.add_widget(self.btn_next)

    def btn_menu_pressed(self, *args, **kwargs):
        print('Menu button pressed')
        config.sm.current = 'MenuScr'


class AnswerLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(AnswerLayout, self).__init__(**kwargs)
        # self.orientation = 'vertical'
        self.height = config.HEIGHT
        self.add_widget(Label(text='Input answer', size_hint=(.25, None), height=config.HEIGHT))
        self.user_answer = TextInput(hint_text='Enter answer here...', size_hint=(.75, None), height=config.HEIGHT)
        self.add_widget(self.user_answer)
        self.add_widget(Button(text='Clear', size_hint=(.25, None), height=config.HEIGHT, on_press=self.btn_clear_pressed))
        # if self.orientation == 'vertical':
            # self.height = config.HEIGHT * len(self.children)

    def btn_clear_pressed(self, *args, **kwargs):
        # config.print_args(args, kwargs)
        print('Btn clear pressed')
        self.user_answer.text = ''


class TestLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(TestLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.upper_bar_layout = UpperBarLayout(size_hint=(1.0, None))
        self.add_widget(self.upper_bar_layout)
        self.random_word_label = Label(text='Press NEXT to start test', size_hint=(1.0, 1.0), font_size = 70)
        self.add_widget(self.random_word_label)
        self.answer_layout = AnswerLayout(size_hint=(1.0, None))
        self.add_widget(self.answer_layout)

        self.upper_bar_layout.btn_next.bind(on_press=self.get_random_word)
        self.answer_layout.user_answer.bind(text=config.print_args)

    def get_random_word(self, *args, **kwargs):
        print('Next button pressed')
        # config.print_args(args, kwargs)
        random_word = config.dictionary.get_random_word()
        print('Random word is {}'.format(random_word.upper()))
        self.random_word_label.text = random_word
        # self.random_word_label.text = config.dictionary.get_random_word()
