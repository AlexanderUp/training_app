# encoding:utf-8
# input layout for kivy framework application
# which calculate days between two dates with leap years been taken into account

from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox


try:
    import config
except ImportError as err:
    print('Can\'t import config')
    print('Error: {}'.format(err))
    sys.exit()
else:
    print('Config imported by input_layout successfully')


class InputLayoutDifference(GridLayout):

    def __init__(self, **kwargs):
        super(InputLayoutDifference, self).__init__(**kwargs)
        self.cols = 5
        self.height = 40
        # self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Button(text='Go to adds', size_hint=(.2, None), on_press=self.btn_to_adds_pressed))
        self.add_widget(Label(text='Day', size_hint=(.2, None)))
        self.add_widget(Label(text='Month', size_hint=(.2, None)))
        self.add_widget(Label(text='Year', size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.1, None)))
        self.day1 = TextInput(multiline=False, size_hint=(.2, None))
        self.month1 = TextInput(multiline=False, size_hint=(.2, None))
        self.year1 = TextInput(multiline=False, size_hint=(.2, None))
        self.today_date1 = Button(text='Today', size_hint=(.2, None))
        self.add_widget(Label(text='Date 1', size_hint=(.2, None)))
        self.add_widget(self.day1)
        self.add_widget(self.month1)
        self.add_widget(self.year1)
        self.add_widget(self.today_date1)
        self.day2 = TextInput(multiline=False, size_hint=(.2, None))
        self.month2 = TextInput(multiline=False, size_hint=(.2, None))
        self.year2 = TextInput(multiline=False, size_hint=(.2, None))
        self.today_date2 = Button(text='Today', size_hint=(.2, None))
        self.add_widget(Label(text='Date 2', size_hint=(.2, None)))
        self.add_widget(self.day2)
        self.add_widget(self.month2)
        self.add_widget(self.year2)
        self.add_widget(self.today_date2)
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.add_widget(Widget(size_hint=(.2, None)))
        self.last_day_checkbox = CheckBox(size_hint=(.2, None))
        self.last_day_label = Label(text='Include\nlast day', size_hint=(.2, None))
        self.add_widget(self.last_day_checkbox)
        self.add_widget(self.last_day_label)

    def btn_to_adds_pressed(self, *args, **kwargs):
        config.sm.current = 'AddScr'
