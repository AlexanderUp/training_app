# encoding:utf-8
# calculate days between two dates with leap years been taken into account


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color
from kivy.graphics import Rectangle

from kivy.config import Config
Config.set('graphics', 'height', '288')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'resizable', '0')

import sys
import datetime

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
        self.days_label = Label(text='Awaiting input...', size_hint=(0.2, None), pos_hint={'center_x':.5})
        self.add_widget(self.days_label)
        self.add_widget(Button(text='Clear', on_press=self.clear, size_hint=(1, 0.2)))
        # self.add_widget(Button(text='Calculate', on_press=self.calculate_dates, size_hint=(1, 0.2)))

        self.inpl.today_date1.bind(active=self.on_today_date1_active)
        self.inpl.today_date2.bind(active=self.on_today_date2_active)
        self.inpl.last_day_checkbox.bind(active=self.on_last_day_checkbox_active)

        self.inpl.day1.bind(text=self.calculate_dates)
        self.inpl.month1.bind(text=self.calculate_dates)
        self.inpl.year1.bind(text=self.calculate_dates)
        self.inpl.day2.bind(text=self.calculate_dates)
        self.inpl.month2.bind(text=self.calculate_dates)
        self.inpl.year2.bind(text=self.calculate_dates)

    def calculate_dates(self, *args,  **kwargs):
        # print('Args recieved: {}'.format(args))
        # print('Kwargs recieved: {}'.format(kwargs))
        dates = [self.inpl.year1.text, self.inpl.month1.text, self.inpl.day1.text, self.inpl.year2.text, self.inpl.month2.text, self.inpl.day2.text]
        if all(dates):
            try:
                dates = [int(date) for date in dates]
            except ValueError:
                print('Wrong data inputed!')
                self.days_label.text = 'Wrong data inputed!'
                return None
            else:
                print('Dates inputed: {}'.format(dates))
                if self.validate(dates[:3]) and self.validate(dates[3:]) and self.validate_date_sequence(dates):
                    print('Correct dates!')
                    total_days_between_dates = self.cal.daysBetweenDates(*dates)
                    if self.inpl.last_day_checkbox.active:
                        total_days_between_dates += 1
                    if total_days_between_dates != 1:
                        self.days_label.text = str(total_days_between_dates) + ' days total'
                    else:
                        self.days_label.text = 'Only one day total'
                else:
                    print('Incorrect dates!!')
                    self.days_label.text = 'Incorrect dates!!'
        else:
            self.days_label.text = 'Awaiting input...'
        return None

    def clear(self, *args):
        # print('Args received: {}'.format(*args))
        self.inpl.day1.text = ''
        self.inpl.month1.text = ''
        self.inpl.year1.text = ''
        self.inpl.day2.text = ''
        self.inpl.month2.text = ''
        self.inpl.year2.text = ''
        self.days_label.text = 'Awaiting input...'
        self.inpl.today_date1.active = False
        self.inpl.today_date2.active = False

    def validate(self, date):
        # date is represented as list [year, month, day]
        if all(d > 0 for d in date):
            if self.cal.is_leap(date[0]):
                daysOfMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date[1] <= 12 and date[2] <= daysOfMonths[date[1]-1]:
                return True
        return False

    def validate_date_sequence(self, dates):
        # print('Rcvd for validation: {}'.format(dates))
        year1, month1, day1, year2, month2, day2 = dates
        # print('y1: {}, m1: {}, d1: {}, y2: {}, m2: {}, d2: {}'.format(year1, month1, day1, year2, month2, day2))
        if (year1 < year2) or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 <= day2):
            return True
        return False

    def on_today_date1_active(self, checkbox, value):
        print('Rcvd: {}, value: {}'.format(checkbox, value))
        if value:
            d = datetime.date.today()
            self.inpl.day1.text = str(d.day)
            self.inpl.month1.text = str(d.month)
            self.inpl.year1.text = str(d.year)
        else:
            self.inpl.day1.text = ''
            self.inpl.month1.text = ''
            self.inpl.year1.text = ''
            self.days_label.text = 'Awaiting input...'
        return None

    def on_today_date2_active(self, checkbox, value):
        print('Rcvd: {}, value: {}'.format(checkbox, value))
        if value:
            d = datetime.date.today()
            self.inpl.day2.text = str(d.day)
            self.inpl.month2.text = str(d.month)
            self.inpl.year2.text = str(d.year)
        else:
            self.inpl.day2.text = ''
            self.inpl.month2.text = ''
            self.inpl.year2.text = ''
            self.days_label.text = 'Awaiting input...'
        return None

    def on_last_day_checkbox_active(self, checkbox, value, *args, **kwargs):
        print('Rcvd: {}, value: {}'.format(checkbox, value))
        if value:
            self.calculate_dates(*args, **kwargs)
        else:
            if all((self.inpl.day1.text, self.inpl.month1.text, self.inpl.year1.text, self.inpl.day2.text, self.inpl.month2.text, self.inpl.year2.text)):
                self.calculate_dates(*args, **kwargs)
            else:
                self.days_label.text = '0 days total'
        return None

    def texting(self, instance, value, *args, **kwargs):
        print('instance: {}'.format(instance))
        print('value: {}'.format(value))
        return None

    # # now can't be implemented because of conflict in realized checkbox logic
    # def test(self, *args, **kwargs):
    #     print('Args recieved: {}'.format(args))
    #     print('Kwargs recieved: {}'.format(kwargs))
    #     d = datetime.date.today()
    #     checks_for_checkbox1 = list(zip((self.inpl.day1.text, self.inpl.month1.text, self.inpl.year1.text), (d.day, d.month, d.year)))
    #     print('checks_for_checkbox1: {}'.format(checks_for_checkbox1))
    #     for (date_entered, date_today) in checks_for_checkbox1:
    #         print(date_entered, date_today)
    #         if self.inpl.today_date1.active and date_entered != str(date_today):
    #             self.inpl.today_date1.active = False
    #             print('checkbox1 status changed')
    #     checks_for_checkbox2 = list(zip((self.inpl.day2.text, self.inpl.month2.text, self.inpl.year2.text), (d.day, d.month, d.year)))
    #     print('checks_for_checkbox2: {}'.format(list(checks_for_checkbox2)))
    #     for date_entered, date_today in checks_for_checkbox2:
    #         if self.inpl.today_date2.active and date_entered != str(date_today):
    #             self.inpl.today_date2.active = False
    #             print('checkbox2 status changed')
    #     return None


class InputLayout(GridLayout):

    def __init__(self, **kwargs):
        super(InputLayout, self).__init__(**kwargs)
        self.cols = 6
        self.height = 40
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Label(text='Day', size_hint=(.2, None)))
        self.add_widget(Label(text='Month', size_hint=(.2, None)))
        self.add_widget(Label(text='Year', size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.1, None)))
        self.add_widget(Widget(size_hint=(.1, None)))
        self.day1 = TextInput(multiline=False, size_hint=(.2, None))
        self.month1 = TextInput(multiline=False, size_hint=(.2, None))
        self.year1 = TextInput(multiline=False, size_hint=(.2, None))
        self.today_date1 = CheckBox(size_hint=(.1, None))
        self.add_widget(Label(text='Date 1', size_hint=(.2, None)))
        self.add_widget(self.day1)
        self.add_widget(self.month1)
        self.add_widget(self.year1)
        self.add_widget(self.today_date1)
        self.add_widget(Label(text='Today',size_hint=(.1, None)))
        self.day2 = TextInput(multiline=False, size_hint=(.2, None))
        self.month2 = TextInput(multiline=False, size_hint=(.2, None))
        self.year2 = TextInput(multiline=False, size_hint=(.2, None))
        self.today_date2 = CheckBox(size_hint=(.1, None))
        self.add_widget(Label(text='Date 2', size_hint=(.2, None)))
        self.add_widget(self.day2)
        self.add_widget(self.month2)
        self.add_widget(self.year2)
        self.add_widget(self.today_date2)
        self.add_widget(Label(text='Today',size_hint=(.1, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.last_day_checkbox = CheckBox(size_hint=(.1, None))
        self.last_day_label = Label(text='Include\nlast day', size_hint=(.1, None))
        self.add_widget(self.last_day_checkbox)
        self.add_widget(self.last_day_label)


class DayCalcApp(App):

    def build(self):
        self.title = 'Date calculator'
        root = MainLayout()
        root.bind(pos=self.update_rect, size=self.update_rect)
        with root.canvas.before:
            Color(0.3, 0.5, 0.5, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def update_rect(self, instance, value):
        # print('update_rect received: {}'.format((instance, value)))
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    print('Args rcvd: {}'.format(sys.argv))
    DayCalcApp().run()
    # print('*' * 12 + ' Some tests ' + '*' * 12)
    # t = MainLayout()
    # test_cases = [(2012, 2, 28),
    #               (2012, 3, 1),
    #               (2012, 6, 30),
    #               (2012, 8, 8),
    #               (1999, 12, 31),
    #               (2012, 1, 1),
    #               (2012, 1, 1),
    #               (2011, 6, 30),
    #               (2011, 1, 1),
    #               (1900, 1, 1),
    #               (2012, 2, 29),
    #               (2013, 2, 29),
    #               (2018, 10, 45),
    #               (2018, 15, 12),
    #               (2011, -12, 2),]
    # for test in test_cases:
    #     print('Tested: {:15} with result {}'.format(str(test), t.validate(test)))
