# encoding:utf-8
# menu layout for MemoWords kivy framework application

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
# ------------------------ Block from example ---------------------------------
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.properties import BooleanProperty
# --------------------- End of Block from example -----------------------------
from kivy.graphics import Color
from kivy.graphics import Rectangle


import config

import pprint

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
        self.btn_edit_word = Button(text='Edit word', size_hint=(.25, None), height=config.HEIGHT, on_press=self.btn_edit_word_pressed)
        self.add_widget(self.btn_edit_word)

    def btn_menu_pressed(self, *args, **kwargs):
        print('Menu button pressed')
        config.sm.current = 'MenuScr'

    def btn_edit_word_pressed(self, *args, **kwargs):
        print('Edit word button pressed')
        config.sm.current = 'EditScr'


# ------------------------ Block from example ---------------------------------
# -----------------------------------------------------------------------------
class RV(RecycleView):

    def __init__(self, *args, **kwargs):
        super(RV, self).__init__(**kwargs)
        vocabulary = config.dictionary.show_dictionary()
        print('vocabulary: {}'.format(vocabulary))
        # self.data = [{'text':'{} - {}'.format(key, ' // '.join(value))} for key, value in vocabulary.items()]
        self.data = config.recycleview_data_formatter(vocabulary)


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
        # print('Rcvd rv: {}'.format(rv))
        # print('Rcvd index: {}'.format(index))
        # print('Rcvd is_selected: {}'.format(is_selected))
        self.selected = is_selected
        if is_selected:
            print('selection changed to {}'.format(rv.data[index]))
            # config.word_selected = rv.data[index]
            # print('selection returned: {}'.format(config.word_selected))
        else:
            print('selection removed for {}'.format(rv.data[index]))
# -----------------------------------------------------------------------------
# --------------------- End of Block from example -----------------------------


class FindBarLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(FindBarLayout,self).__init__(**kwargs)
        self.height = config.HEIGHT
        self.add_widget(Label(text='Type to find', size_hint=(.25, None), height=config.HEIGHT))
        self.find_field = TextInput(hint_text='Search here...', multiline=False, size_hint=(.5, None), height=config.HEIGHT)
        # print('Previous _line_option["anchor_y"]: {}'.format(self.find_field._line_options['anchor_y']))
        # self.find_field._line_options['anchor_y'] = 'center'
        # print('New _line_option[\'anchor_y\']: {}'.format(self.find_field._line_options['anchor_y']))
        # self.find_field._line_options['anchor_x'] = 'right'
        self.add_widget(self.find_field)
        # print('find_field.__dict__:')
        # pprint.pprint(self.find_field.__dict__)
        self.add_widget(Button(text='Clear', size_hint=(.25, None), on_press=self.btn_clear_pressed, height=config.HEIGHT))

    def btn_clear_pressed(self, *args, **kwargs):
        print('btn clear from find bar pressed')
        self.find_field.text = ''


class DictionaryLayout(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(DictionaryLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.upper_bar_layout = UpperBarLayout(size_hint=(1.0, None))
        self.add_widget(self.upper_bar_layout)
        self.rv = RV()
        self.add_widget(self.rv)
        # print('RV.data: {}'.format(self.rv.data))
        self.find_bar_layout = FindBarLayout(size_hint=(1.0, None))
        self.add_widget(self.find_bar_layout)

        self.find_bar_layout.find_field.bind(text=self.search_word)
        # self.upper_bar_layout.btn_edit_word.bind(on_press=self.btn_edit_word_pressed)


    def search_word(self, instance, value):
        config.print_args(instance, value, args_name='instance', kwargs_name='value')
        res = config.dictionary.search_word(value)
        print('Search result: {}'.format(res))
        # self.rv.data = [{'text':'{} - {}'.format(key, ' // '.join(value))} for key, value in res.items()]
        self.rv.data = config.recycleview_data_formatter(res)
        return None

    # def btn_edit_word_pressed(self, *args, **kwargs):
    #     print('Edit word button pressed')
