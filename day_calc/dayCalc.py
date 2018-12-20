# encoding:utf-8
# calculate days between two dates with leap years been taken into account


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
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
except ImportError as err:
    print('Can\'t import module LeapCalendar')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Import successfull!')


try:
    from input_layout import InputLayoutDifference
except ImportError as err:
    print('Can\'t import input layouts')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Layouts imported succsessfully')


class MainLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.inpl = InputLayoutDifference()
        self.cal = LeapCalendar()
        self.add_widget(self.inpl)
        self.days_label = Label(text='Awaiting input...', size_hint=(0.2, None), pos_hint={'center_x':.5})
        self.add_widget(self.days_label)
        self.add_widget(Button(text='Clear', on_press=self.clear, size_hint=(1, 0.2)))

        self.inpl.today_date1.bind(on_press=self.on_today_date1)
        self.inpl.today_date2.bind(on_press=self.on_today_date2)
        self.inpl.last_day_checkbox.bind(active=self.on_last_day_checkbox_active)
        self.inpl.day1.bind(text=self.calculate_dates)
        self.inpl.month1.bind(text=self.calculate_dates)
        self.inpl.year1.bind(text=self.calculate_dates)
        self.inpl.day2.bind(text=self.calculate_dates)
        self.inpl.month2.bind(text=self.calculate_dates)
        self.inpl.year2.bind(text=self.calculate_dates)

    def calculate_dates(self, instance=None, value=None):
        # print('Instance: {}'.format(instance))
        # print('Value: {}'.format(value))
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
                if self.cal.validate(dates[:3]) and self.cal.validate(dates[3:]) and self.cal.validate_date_sequence(dates):
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

    def on_today_date1(self, instance=None, value=None, *args, **kwargs):
        print('Instance: {}'.format(instance))
        print('Value: {}'.format(value))
        d = datetime.date.today()
        self.inpl.day1.text = str(d.day)
        self.inpl.month1.text = str(d.month)
        self.inpl.year1.text = str(d.year)
        return None

    def on_today_date2(self, instance=None, value=None, *args, **kwargs):
        print('Instance: {}'.format(instance))
        print('Value: {}'.format(value))
        d = datetime.date.today()
        self.inpl.day2.text = str(d.day)
        self.inpl.month2.text = str(d.month)
        self.inpl.year2.text = str(d.year)
        return None

    def on_last_day_checkbox_active(self, checkbox, value, *args, **kwargs):
        # print('Rcvd: {}, value: {}'.format(checkbox, value))
        if value:
            self.calculate_dates()
        else:
            if all((self.inpl.day1.text, self.inpl.month1.text, self.inpl.year1.text, self.inpl.day2.text, self.inpl.month2.text, self.inpl.year2.text)):
                self.calculate_dates()
            else:
                self.days_label.text = '0 days total'
        return None

    def checking(self, instance=None, value=None, *args, **kwargs):
        print('instance: {}'.format(instance))
        print('value: {}'.format(value))
        print('args: {}'.format(args))
        print('kwargs: {}'.format(kwargs))
        return None


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
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    print('Args rcvd: {}'.format(sys.argv))
    DayCalcApp().run()
