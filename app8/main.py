# encoding:utf-8
# eighth kivy framework training app

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    pass

class LayoutsApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    LayoutsApp().run()
