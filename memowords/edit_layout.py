# encoding:utf-8
# edit layout for MemoWords kivy framework application

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


import config


class EditWordLayout(GridLayout):

    def __init__(self, *args, **kwargs):
        super(EditWordLayout, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.height = self.rows * config.HEIGHT
        self.add_widget(Label(text='Word', size_hint=(.25, None), height=config.HEIGHT))
        self.edit_word_field = TextInput(hint_text='Edit word here', size_hint=(.75, None), multiline=False, height=config.HEIGHT)
        self.add_widget(self.edit_word_field)
        self.add_widget(Label(text='Translation', size_hint=(.25, None), height=config.HEIGHT))
        self.edit_translation_field = TextInput(hint_text='Edit translation here', size_hint=(.75, None), multiline=False, height=config.HEIGHT)
        self.add_widget(self.edit_translation_field)

class ButtonBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(ButtonBarLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.btn_cancel = Button(text='Cancel', size_hint=(.33, None), height=config.HEIGHT)
        self.add_widget(self.btn_cancel)
        self.btn_save = Button(text='Save', size_hint=(.33, None), height=config.HEIGHT)
        self.add_widget(self.btn_save)
        self.btn_delete = Button(text='Delete', size_hint=(.33, None), height=config.HEIGHT)
        self.add_widget(self.btn_delete)


class EditLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(EditLayout, self).__init__(*kwargs)
        self.orientation = 'vertical'
        self.edit_word_layout = EditWordLayout(size_hint=(1.0, None))
        self.add_widget(self.edit_word_layout)
        self.add_widget(Widget(size_hint=(1.0, 1.0)))
        self.button_bar_layout = ButtonBarLayout(size_hint=(1.0, None))
        self.add_widget(self.button_bar_layout)

        self.button_bar_layout.btn_cancel.bind(on_press=self.btn_cancel_pressed)
        self.button_bar_layout.btn_save.bind(on_press=self.btn_save_pressed)
        self.button_bar_layout.btn_delete.bind(on_press=self.btn_delete_pressed)

        self.edit_word_layout.edit_word_field.bind(text=config.print_args)
        self.edit_word_layout.edit_translation_field.bind(text=config.print_args)

    def btn_cancel_pressed(self, instance, value=None):
        print('Cancel btn pressed')
        self.edit_word_layout.edit_word_field.text = ''
        self.edit_word_layout.edit_translation_field.text = ''
        config.sm.current = 'DictionaryScr'

    def btn_save_pressed(self, instance, value=None):
        print('Save btn pressed')

    def btn_delete_pressed(self, instance, value=None):
        print('Delete btn pressed')
