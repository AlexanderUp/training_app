# encoding:utf-8
# additional layout for date addition/substraction for kivy framework application
# which calculate days between dates with leap years been taken into account.

from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import datetime


MONTH = {1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'}


try:
    import config
except ImportError as err:
    print('Can\'t import config')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Config imported by add_layout successfully')


class AddLayout(GridLayout):

    def __init__(self, **kwargs):
        super(AddLayout, self).__init__(**kwargs)
        self.cols = 5
        self.height = 40
        # first row
        self.add_widget(Button(text='Go to main', size_hint=(.2, None), on_press=self.go_back))
        self.add_widget(Label(text='Day', size_hint=(.2, None)))
        self.add_widget(Label(text='Month', size_hint=(.2, None)))
        self.add_widget(Label(text='Year', size_hint=(.2, None),))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.day = TextInput(multiline=False, size_hint=(.2, None))
        self.month = TextInput(multiline=False, size_hint=(.2, None))
        self.year = TextInput(multiline=False, size_hint=(.2, None))
        # second row
        self.add_widget(Label(text='Initial date', size_hint=(.2, None)))
        self.add_widget(self.day)
        self.add_widget(self.month)
        self.add_widget(self.year)
        self.today_button = Button(text='Today', size_hint=(.2, None), on_press=self.pressed_btn_today)
        self.add_widget(self.today_button)
        # third row
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_button = Button(text='Add', size_hint=(.2, None), on_press=self.pressed_btn_add)
        self.add_widget(self.add_button)
        self.add_widget(Widget(size_hint=(.2, None)))
        self.substract_button = Button(text='Substract', size_hint=(.2, None), on_press=self.pressed_btn_substract)
        self.add_widget(self.substract_button)
        self.add_widget(Button(text='Clear', size_hint=(.2, None), on_press=self.pressed_btn_clear))
        # fourth row
        self.add_widget(Label(text='Number of days', size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.days_difference = TextInput(multiline=False, size_hint=(.2, None))
        self.add_widget(self.days_difference)
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        # fifth row
        self.add_widget(Label(text='Target date', size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.target_date = Label(text='Awaiting input...', size_hint=(.2, None))
        self.add_widget(self.target_date)
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))

    def go_back(self, *args, **kwargs):
        config.sm.current = 'MainScr'

    def pressed_btn_add(self, *args, **kwarg):
        self.target_date.text = self.aux_f(sign=True)

    def pressed_btn_substract(self, *args, **kwargs):
        self.target_date.text = self.aux_f(sign=False)

    def pressed_btn_today(self, *args, **kwargs):
        d = datetime.date.today()
        self.day.text = str(d.day)
        self.month.text = str(d.month)
        self.year.text = str(d.year)
        return None

    def pressed_btn_clear(self, *args, **kwargs):
        self.day.text = ''
        self.month.text = ''
        self.year.text = ''
        self.days_difference.text = ''
        self.target_date.text = 'Awaiting input'

    def aux_f(self, sign=None, *args, **kwargs):
        initial_date = datetime.date(int(self.year.text), int(self.month.text), int(self.day.text))
        delta = datetime.timedelta(int(self.days_difference.text))
        if sign:
            d = initial_date + delta
        else:
            d = initial_date - delta
        return '{} of {} {}'.format(d.day, MONTH[d.month], d.year)
