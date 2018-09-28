# encoding:utf-8

from kivy.uix.screenmanager import ScreenManager, SlideTransition
from screens.screen import BaseScreen

sm = ScreenManager(transition=SlideTransition())
screens = {
'main': BaseScreen,
}
