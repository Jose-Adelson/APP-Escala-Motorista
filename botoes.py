from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import Screen

class ImageButton(ButtonBehavior , Image):
        pass

class LabelButton(ButtonBehavior , Label):
    pass