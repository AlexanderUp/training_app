# encoding:utf-8
# menu layout for MemoWords kivy framework application

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
# -----------------------------------------------------------------------------
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.properties import BooleanProperty
# -----------------------------------------------------------------------------
from kivy.graphics import Color
from kivy.graphics import Rectangle


import config

# print(dir(config))
# # print(config.__dict__)
# print('dictionary' in config.__dict__)

# ------------------------ Block from example ---------------------------------
# -----------------------------------------------------------------------------
from kivy.lang import Builder

Builder.load_string(
'''
<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
''')
# -----------------------------------------------------------------------------
# --------------------- End of Block from example -----------------------------


class UpperBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(UpperBarLayout, self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Button(text='Menu', size_hint=(.25, None), on_press=self.btn_menu_pressed, height=config.HEIGHT))
        self.add_widget(Label(text='Words in dictionary', size_hint=(.5, None), height=config.HEIGHT))
        self.add_widget(Widget(size_hint=(.25, None), height=config.HEIGHT))

    def btn_menu_pressed(self, *args, **kwargs):
        print('Menu button pressed')
        config.sm.current = 'MenuScr'


# ------------------------ Block from example ---------------------------------
# -----------------------------------------------------------------------------
class RV(RecycleView):

    def __init__(self, *args, **kwargs):
        super(RV, self).__init__(**kwargs)
        # vocabulary = config.dictionary.show_dictionary()
        self.data = [{'text':str(x)} for x in range(100)]
        # self.data = [{'text':str(x) for x in vocabulary}]

        self.bind(pos=self.update_rect, size=self.update_rect)
        with self.canvas.before:
            Color(0.2, 0.4, 0.2, 1.0)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view.'''
    pass


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label. '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes. '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down. '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print('selection changed to {}'.format(rv.data[index]))
        else:
            print('selection removed for {}'.format(rv.data[index]))
# -----------------------------------------------------------------------------
# --------------------- End of Block from example -----------------------------


class FindBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(FindBarLayout,self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Label(text='Type to find', size_hint=(.25, None), height=config.HEIGHT))
        self.find_field = TextInput(multiline=False, size_hint=(.5, None), height=config.HEIGHT)
        self.add_widget(self.find_field)
        self.add_widget(Button(text='Clear', size_hint=(.25, None), on_press=self.btn_clear_pressed, height=config.HEIGHT))

    def btn_clear_pressed(self, *args, **kwargs):
        print('btn clear from find bar pressed')
        self.find_field.text = ''


class DictionaryLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(DictionaryLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(UpperBarLayout(size_hint=(1.0, None)))
        self.add_widget(RV())
        find_bar_layout = FindBarLayout(size_hint=(1.0, None))
        self.add_widget(find_bar_layout)
