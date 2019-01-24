# encoding:utf-8
# configuration file for MemoWords kivy framework application
# mainly for screen manager instance distribution between modules

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SlideTransition

import class_dictionary

# height for almost all widgets
HEIGHT = 100 # some widgets (labels, etc) inherit their own heights
RANDOM_WORD = None

# screen manager
sm = ScreenManager()
sm.transition = SlideTransition()

# dictionary object
dictionary = class_dictionary.Dictionary()

# auxillary functions
def test(instance, value=None, *args, **kwargs):
    print('Instance: {}, value: {}'.format(instance, value))
    if 'text' in dir(instance):
        print('Text {} in {}'.format(instance.text, instance))
    return None

def print_args(args, kwargs, args_name='args', kwargs_name='kwargs'):
    print('Rcvd {args_name}: {args}'.format(args=args, args_name=args_name))
    print('Rcvd {kwargs_name}: {kwargs}'.format(kwargs=kwargs, kwargs_name=kwargs_name))
    return None

# def print_args(args_name='args', kwargs_name='kwargs'):
#     nonlocal args, kwargs
#     print('Rcvd {args_name}: {args}'.format(args=args, args_name=args_name))
#     print('Rcvd {kwargs_name}: {kwargs}'.format(kwargs=kwargs, kwargs_name=kwargs_name))
#     return None

def recycleview_data_formatter(data):
    # sorted list to be returned
    # res =[{'text':'{} - {}'.format(key, ' // '.join(value))} for key, value in data.items()]
    # return res.sort(key=key)
    return [{'text':'{} - {}'.format(key, ' // '.join(value))} for key, value in data.items()]
