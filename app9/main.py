# encoding:utf-8
# kivy framework training app
# subject - TextInput widget

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


# class CustomWidget(BoxLayout):
#     pass

    # def __init__(self, **kvargs):
    #     super(BoxLayout, self).__init__(**kvargs)
    #     self.orientation = 'vertical'
    #     self.add_widget(Label(text='my text', size_hint=(.5, 1)))
    #     self.add_widget(TextInput(multiline=False , size_hint=(.5, 1)))


class TextApp(App):

    # content = StringProperty('')
    content = ''

    def build(self):
        self.title = 'TextInput test app'
        root = GridLayout(cols=2, rows=2)
        l1 = Label(text='Input field', size_hint=(.5, .5))
        t = TextInput(multiline=False, size_hint=(.5, .5))
        l2 = Label(text='Text got:', size_hint=(.5, .5))
        l3 = Label(text='default', size_hint=(.5, .5))
        root.add_widget(l1)
        root.add_widget(t)
        root.add_widget(l2)
        root.add_widget(l3)
        t.bind(text=self.on_text)
        return root

    def on_text(self, instance, value):
        print('the widget {} have: {}'.format(instance, value))
        self.content = value
        print('value stored is: {}'.format(self.content))




if __name__ == '__main__':
    TextApp().run()
