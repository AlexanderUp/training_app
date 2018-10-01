# encoding:utf-8
# calculate days between two dates with leap years been taken into account

from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty

class Calc(GridLayout):

    def __init__(self, **kwargs):
        super(Calc, self).__init__(**kwargs)
        self.cols = 4
        self.height = 40
        self.add_widget(Label(text='*****', size_hint= (.25, None)))
        self.add_widget(Label(text='Day', size_hint= (.25, None)))
        self.add_widget(Label(text='Month', size_hint= (.25, None)))
        self.add_widget(Label(text='Year', size_hint= (.25, None)))
        self.add_widget(Label(text='Date 1', size_hint= (.25, None)))
        self.day1 = TextInput(multiline=False, size_hint= (.25, None))
        self.month1 = TextInput(multiline=False, size_hint= (.25, None))
        self.year1 = TextInput(multiline=False, size_hint= (.25, None))
        self.add_widget(self.day1)
        self.add_widget(self.month1)
        self.add_widget(self.year1)
        self.add_widget(Label(text='Date 2', size_hint= (.25, None)))
        self.day2 = TextInput(multiline=False, size_hint= (.25, None))
        self.month2 = TextInput(multiline=False, size_hint= (.25, None))
        self.year2 = TextInput(multiline=False, size_hint= (.25, None))
        self.add_widget(self.day2)
        self.add_widget(self.month2)
        self.add_widget(self.year2)


class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        return Calc()


if __name__ == '__main__':
    DayCalcApp().run()
