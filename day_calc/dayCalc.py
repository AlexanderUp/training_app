# encoding:utf-8
# calculate days between two dates with leap years been taken into account

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '512')
Config.set('graphics', 'resizable', '0')
import sys

print("*" * 125)

try:
    from calendar_class import LeapCalendar
except ImportError:
    print('Can\'t import module LeapCalendar')
    sys.exit()
else:
    print('Import successfull!')


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.inpl = InputLayout()
        self.cal = LeapCalendar()
        self.add_widget(self.inpl)
        self.add_widget(Button(text='Clear', on_press=self.clear, size_hint=(1, 0.2)))
        self.add_widget(Button(text='Calculate', on_press=self.calculate_dates, size_hint=(1, 0.2)))

    def calculate_dates(self, *args,  **kwargs):
        print('Args recieved: {}'.format(*args))
        print('Kwargs recieved: {}'.format(kwargs))
        dates = [self.inpl.year1.text, self.inpl.month1.text, self.inpl.day1.text, self.inpl.year2.text, self.inpl.month2.text, self.inpl.day2.text]
        try:
            dates = [int(date) for date in dates]
        except ValueError:
            print('Wrong date inputed!')
            # print('Exiting....')
            # sys.exit()
            self.inpl.days_label.text = 'Wrong date inputed!'
            return None
        else:
            print('Dates inputed: {}'.format(dates))
            if not self.validate(dates[:3]) or not self.validate(dates[3:]) or dates[0] > dates[3]:
                print('Incorrect dates!!')
                self.inpl.days_label.text = 'Incorrect dates!!'
                return
            else:
                print('Correct input!')
        self.inpl.days_label.text = str(self.cal.daysBetweenDates(*dates)) + ' days'

    def clear(self, *args):
        print('Args received: {}'.format(*args))
        self.inpl.day1.text = ''
        self.inpl.month1.text = ''
        self.inpl.year1.text = ''
        self.inpl.day2.text = ''
        self.inpl.month2.text = ''
        self.inpl.year2.text = ''

    def validate(self, date):
        # date is represented as list [year, month, day]
        if all(d > 0 for d in date):
            if self.cal.is_leap(date[0]):
                daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date[1] > 0 and date[1] <= 12:
                if date[2] > 0 and date[2] <= daysOfMonths[date[1]-1]:
                    return True
        return False


class InputLayout(GridLayout):

    def __init__(self, **kwargs):
        super(InputLayout, self).__init__(**kwargs)
        self.cols = 4
        # self.rows = 4
        self.height = 40
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
        self.days_label = Label(text='DAYS', size_hint=(0.25, None))
        self.add_widget(self.days_label)
        self.add_widget(Widget(size_hint=(.25, None)))


class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        root = MainLayout()
        return root


if __name__ == '__main__':
    DayCalcApp().run()
    print('*' * 12 + 'Some tests' + '*' * 12)
    t = MainLayout()
    test_cases = [(2012, 2, 28),
                  (2012, 3, 1),
                  (2012, 6, 30),
                  (2012, 8, 8),
                  (1999, 12, 31),
                  (2012, 1, 1),
                  (2012, 1, 1),
                  (2011, 6, 30),
                  (2011, 1, 1),
                  (1900, 1, 1),
                  (2012, 2, 29),
                  (2013, 2, 29),
                  (2018, 10, 45),
                  (2018, 15, 12),
                  (2011, -12, 2),]
    for test in test_cases:
        print('Tested: {:15} with result {}'.format(str(test), t.validate(test)))
