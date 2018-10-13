# encoding:utf-8
# kivy framework training app
# subject - TextInput widget

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


class TextApp(App):

    # content1 = StringProperty('Content 1')
    # content2 = StringProperty('Content 2')

    def build(self):
        self.title = 'TextInput test app'
        root = GridLayout(cols=2)
        self.l1 = Label(text='Input field', size_hint_x=.5)
        self.t1 = TextInput(multiline=False, size_hint_x=.5)
        self.l2 = Label(text='Input field 2', size_hint_x=.5)
        self.t2 = TextInput(multiline=False, size_hint_x=.5)
        # l3 = Label(text=self.content1)
        # l4 = Label(text=self.content2)
        self.l3 = Label(text='Content 1')
        self.l4 = Label(text='Content 2')
        root.add_widget(self.l1)
        root.add_widget(self.t1)
        root.add_widget(self.l2)
        root.add_widget(self.t2)
        root.add_widget(self.l3)
        root.add_widget(self.l4)
        # t1.bind(text=self.on_text)
        # t2.bind(text=self.on_text)
        self.t1.bind(text=self.label3_update)
        self.t2.bind(text=self.label4_update)
        print(root.__dict__)
        return root

    # def on_text(self, instance, value):
    #     print('the widget {} have: {}'.format(str(instance)[-15:-1], value))

    def label3_update(self, instance, value):
        print('the widget {} have: {}'.format(str(instance)[-15:-1], value))
        self.l3.text = value

    def label4_update(self, instance, value):
        print('the widget {} have: {}'.format(str(instance)[-15:-1], value))
        self.l4.text = value



if __name__ == '__main__':
    TextApp().run()
