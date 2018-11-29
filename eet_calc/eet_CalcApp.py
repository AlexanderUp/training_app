# encoding:utf-8
# GUI for eet calculator (equivalent-effective temperature)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'width', '512')
Config.set('graphics', 'height', '288')
# Config.set('graphics', 'resizable', '0')

import sys

try:
    import eet
except ImportError as err:
    print('Can\'\\t import eet.py')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Import successfull!')


class InputLayout(GridLayout):

    def __init__(self, *args, **kwargs):
        super(InputLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Temperature', font_size=70, size_hint=(1, .33)))
        self.temperature = TextInput(font_size=70, size_hint=(1, .2), multiline=False)
        self.add_widget(self.temperature)
        self.add_widget(Label(text='Wind velocity', font_size=70, size_hint=(1, .33)))
        self.wind_velocity = TextInput(font_size=70, size_hint=(1, .2), multiline=False)
        self.add_widget(self.wind_velocity)
        self.add_widget(Label(text='Humidity', font_size=70, size_hint=(1, .33)))
        self.humidity = TextInput(font_size=70, size_hint=(1, .2), multiline=False)
        self.add_widget(self.humidity)


class MainLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.input_layout = InputLayout()
        self.add_widget(self.input_layout)
        self.eet = Label(text='Awaiting data...', font_size=70, size_hint=(1, .33))
        self.add_widget(self.eet)
        self.eet2 = Label(text='Awaiting data...', font_size=70, size_hint=(1, .33))
        self.add_widget(self.eet2)
        self.add_widget(Button(text='Calculate', font_size=70, size_hint=(1, .33), on_press=self.calculate))

    def calculate(self, *args, **kwargs):
        self.eet.text = '{} Celsius degrees (eet)'.format(str(round(eet.eet(float(self.input_layout.temperature.text),
        float(self.input_layout.wind_velocity.text),
        float(self.input_layout.humidity.text)), 1)))
        self.eet2.text = '{} Celsius degrees (eet2)'.format(str(round(eet.eet2(float(self.input_layout.temperature.text),
        float(self.input_layout.wind_velocity.text),
        float(self.input_layout.humidity.text)), 1)))



class eet_CalcApp(App):

    def build(self):
        self.title = 'eet Calculator'
        root = MainLayout()
        return root


if __name__ == '__main__':
    print('=' * 75)
    eet_CalcApp().run()
