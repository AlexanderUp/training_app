# encoding:utf-8
# menu layout for MemoWords kivy framework application

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
# from kivy.graphics import Color
# from kivy.graphics import Rectangle


import config


class UpperBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(UpperBarLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Button(text='Menu', size_hint=(.25, None), on_press=self.btn_menu_pressed, height=config.HEIGHT))
        self.add_widget(Label(text='TestLayout', size_hint=(.5, None), height=config.HEIGHT))
        self.add_widget(Widget(size_hint=(.25, None), height=config.HEIGHT))

    #     self.bind(pos=self.update_rect, size=self.update_rect)
    #     with self.canvas.before:
    #         Color(0.1, 0.9, 0.7, 1.0)
    #         self.rect = Rectangle(size=self.size, pos=self.pos)
    #
    # def update_rect(self, instance, value):
    #     self.rect.pos = instance.pos
    #     self.rect.size = instance.size

    def btn_menu_pressed(self, *args, **kwargs):
        print('Menu button pressed')
        config.sm.current = 'MenuScr'


class AnswerLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(AnswerLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        # self.height = config.HEIGHT * 2
        self.add_widget(Label(text='Input translation below', size_hint=(1.0, None), height=config.HEIGHT))
        self.user_answer = TextInput(size_hint=(1.0, None), height=config.HEIGHT)
        self.add_widget(self.user_answer)
        self.height = config.HEIGHT * len(self.children)

    #     self.bind(pos=self.update_rect, size=self.update_rect)
    #     with self.canvas.before:
    #         Color(0.1, 0.3, 0.3, 1.0)
    #         self.rect = Rectangle(size=self.size, pos=self.pos)
    #
    # def update_rect(self, instance, value):
    #     self.rect.pos = instance.pos
    #     self.rect.size = instance.size


class TestLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(TestLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(UpperBarLayout(size_hint=(1.0, None)))
        self.add_widget(Label(text='Test case here', size_hint=(1.0, 1.0)))
        self.add_widget(AnswerLayout(size_hint=(1.0, None)))
