# encoding:utf-8
# GUI for password entropy calculator

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
Config.set('graphics', 'resizable', '0')

import sys
# import os

# print('Current working directory: {}'.format(os.getcwd()))

try:
    import passwd_entropy_calculator
except ImportError:
    print("Can't import passwd_entropy_calculator module!")
    sys.exit()
else:
    print('Import successfull!')


class MainLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Input password', size_hint=(1, 0.2), font_size=70))
        self.psswd = TextInput(size_hint=(1, 0.2), multiline=False)
        self.add_widget(self.psswd)
        self.psswd.bind(text=self.calculate)
        self.bits_label = Label(size_hint=(1, 0.2), font_size=70)
        self.bits_label2 = Label(size_hint=(1, 0.2), font_size=70)
        self.bits_label3 = Label(size_hint=(1, 0.2), font_size=70)
        self.add_widget(self.bits_label)
        self.add_widget(self.bits_label2)
        self.add_widget(self.bits_label3)
        self.add_widget(Button(text='Clear', on_press=self.clear, font_size=70, size_hint=(1, 0.2)))


    def clear(self, *args, **kwargs):
        self.psswd.text = ''
        for t in (self.bits_label, self.bits_label2, self.bits_label3):
            t.text = '0 bits'
        return None

    def calculate(self, *args, **kwargs):
        calculator = passwd_entropy_calculator.EntropyCalculator()
        func = (calculator.calc, calculator.calc2, calculator.calc3)
        texts = (self.bits_label, self.bits_label2, self.bits_label3)
        for (f, t) in zip(func, texts):
            bits_ = f(self.psswd.text)
            t.text = '{}: {} bits'.format(f.__name__, round(bits_, 1))
        return None


class eCalcApp(App):

    def build(self):
        self.title = 'Password entropy calculator'
        root = MainLayout()
        return root


if __name__ == '__main__':
    print('=' * 75)
    eCalcApp().run()
