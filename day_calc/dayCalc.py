# encoding:utf-8
# calculate days between two dates with leap years been taken into account

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
form kivy.properties import DictProperty
from kivy.graphics import Color

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
# Config.set('graphics', 'resizable', '0')
import sys

try:
    from calendar_class import LeapCalendar
except ImportError:
    print('Can\'t import module LeapCalendar')
    sys.exit()
else:
    print('Import successfull!')

class RootWidget(BoxLayout):
    pass


# class CustomLayout(AnchorLayout):
#
#     # def __init__(self, my_text, colors, **kwargs):
#     def __init__(self, my_text, **kwargs):
#         super(CustomLayout, self).__init__(**kwargs)
#         self.height = 40
#         self.anchor_x = 'center'
#         self.anchor_y = 'top'
#         self.my_text = my_text
#         # self.a, self.b, self.c, self.mode = colors
#         # with self.canvas.before:
#         #     Color(self.a, self.b, self.c, mode=self.mode)
#         self.add_widget(Label(text=self.my_text, size_hint=(1.0, None)))


# class CustomLayout(BoxLayout):
#
#     def __init__(self, my_text, **kwargs):
#         super(BoxLayout, self).__init__(**kwargs)
#         self.height = 40
#         self.my_text = my_text
#         self.add_widget(Label(text='Total number of days between dates is:', size_hint=(1.0, None)))
#         self.add_widget(Label(text=self.my_text, size_hint=(1.0, None)))


class MainLayout(GridLayout):

    # {'day1':int, 'month1':int, 'year1':int, 'day2':int, 'month2':int, 'year2':int}
    input_data = DictProperty({'day1':0, 'month1':0, 'year1':0, 'day2':0, 'month2':0, 'year2':0})

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 4
        self.height = 40
        self.days = 'DAYS'
        self.add_widget(Label(text='*****', size_hint=(.25, None)))
        self.add_widget(Label(text='Day', size_hint=(.25, None)))
        self.add_widget(Label(text='Month', size_hint=(.25, None)))
        self.add_widget(Label(text='Year', size_hint=(.25, None)))
        self.add_widget(Label(text='Date 1', size_hint=(.25, None)))
        self.day1 = TextInput(multiline=False, size_hint=(.25, None))
        self.month1 = TextInput(multiline=False, size_hint=(.25, None))
        self.year1 = TextInput(multiline=False, size_hint=(.25, None))
        self.add_widget(self.day1)
        self.add_widget(self.month1)
        self.add_widget(self.year1)
        self.add_widget(Label(text='Date 2', size_hint=(.25, None)))
        self.day2 = TextInput(multiline=False, size_hint=(.25, None))
        self.month2 = TextInput(multiline=False, size_hint=(.25, None))
        self.year2 = TextInput(multiline=False, size_hint=(.25, None))
        self.add_widget(self.day2)
        self.add_widget(self.month2)
        self.add_widget(self.year2)
        self.add_widget(Label(text='*****', size_hint=(.25, None)))
        self.add_widget(Label(text='Total days:', size_hint=(.25, None)))
        self.add_widget(Label(text=self.days, size_hint=(.25, None)))
        self.add_widget(Label(text='*****', size_hint=(.25, None)))


class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        root = RootWidget(orientation='vertical')
        a = MainLayout()
        # b = CustomLayout(my_text='Total number of days between dates is:')
        # c = CustomLayout(orientation='vertical', my_text='NUMBER')
        root.add_widget(a)
        # root.add_widget(b)
        # root.add_widget(c)
        return root


if __name__ == '__main__':
    DayCalcApp().run()
