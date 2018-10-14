# encoding:utf-8
# calculate days between two dates with leap years been taken into account

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import DictProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
# Config.set('graphics', 'resizable', '0')
import sys

print("*" * 125)

try:
    from calendar_class import LeapCalendar
except ImportError:
    print('Can\'t import module LeapCalendar')
    sys.exit()
else:
    print('Import successfull!')


class MainLayout(GridLayout):


    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.cols = 4
        # self.rows = 4
        self.height = 40
        self.days = 'DAYS'
        self.add_widget(Widget(size_hint=(.25, None)))
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
        self.add_widget(Widget(size_hint=(.25, None)))
        self.add_widget(Label(text='Total days:', size_hint=(.25, None)))
        self.add_widget(Label(text=self.days, size_hint=(.25, None)))
        self.add_widget(Widget(size_hint=(.25, None)))
        self.add_widget(Button(text='Calculate', on_press=self.calculate_dates, size_hint=(.25, None)))

    def calculate_dates(self, *args,  **kwargs):
        print('Args recieved: {}'.format(*args))
        print('Kwargs recieved: {}'.format(kwargs))
        cal = LeapCalendar()
        dates = [self.year1.text, self.month1.text, self.day1.text, self.year2.text, self.month2.text, self.day2.text]
        dates = [int(date) for date in dates]
        print('Dates inputed: {}'.format(dates))
        return cal.daysBetweenDates(*dates)



class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        root = MainLayout()
        return root


if __name__ == '__main__':
    DayCalcApp().run()
