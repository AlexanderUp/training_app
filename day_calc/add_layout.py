# encoding:utf-8
# additional layout for date addition/substraction for kivy framework application
# which calculate days between dates with leap years been taken into account.

from kivy.uix.widget import Widget


class AddLayout(Widget):

    def __init__(self, **kwargs):
        super(AddLayout, self).__init__(**kwargs)
        self.add_widget(Widget())
