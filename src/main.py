from guitar import Guitar
from common import *

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

widgets = []
def highlight(notes):
    global widgets
    for w in widgets:
        colour = 0
        for n in notes:
            colour= colour + 1 / len(notes)
            if n == w.text:
                w.color = [1-colour,colour,colour,1]

class GuitarScreen(GridLayout):
    def __init__(self,**kwargs):
        super(GuitarScreen,self).__init__(**kwargs)

        self.frets = 24
        self.strings=[('E',3),('A',4),('D',4),('G',4),('B',5),('E',5)]
        self.lefty = True
        global widgets
        if self.lefty:
            order = -1
        else:
            order = 1

        self.guitar = Guitar(number_of_frets=self.frets,tuning=self.strings,is_lefty=self.lefty)
        self.cols=self.frets
        self.rows=len(self.strings)+2
        for string in self.guitar.strings:
            for note in string.notes[::order]:
                a = Label(text=str(note[0]))
                widgets.append(a)
                self.add_widget(a)
        for i in range(self.frets)[::order]:
            self.add_widget(Label(text=str(i)))
        for fret_marker in self.guitar.fret_markers:
            self.add_widget(Label(text=str(fret_marker)))




class ScaleOptions(GridLayout):
    def __init__(self,**kwargs):
        super(ScaleOptions,self).__init__(**kwargs)
        self.cols=3
        self.rows=1
        self.root = TextInput(text='Root Note')
        self.scaleType = TextInput(text='Scale Type')

        self.loadButton = Button(text='Show Scale')

        self.loadButton.bind(on_press=self.callback)
        self.add_widget(self.root)
        self.add_widget(self.scaleType)
        self.add_widget(self.loadButton)

    def callback(self,dt):
        print(self.root.text)
        print(self.scaleType.text)
        scale = Scale(self.root.text,self.scaleType.text)
        print(scale.notes)
        highlight(scale.notes)

class ChordOptions(GridLayout):
    def __init__(self,**kwargs):
        super(ChordOptions,self).__init__(**kwargs)
        self.cols=4
        self.rows=1
        self.root = TextInput(text='Root Note')
        self.triadType = TextInput(text='Scale Type')
        self.extensions = TextInput(text='Extensions')
        self.loadButton = Button(text='Show Chord')

        self.loadButton.bind(on_press=self.callback)
        self.add_widget(self.root)
        self.add_widget(self.triadType)
        self.add_widget(self.extensions)
        self.add_widget(self.loadButton)

    def callback(self,dt):
        print(self.root.text)
        print(self.triadType.text)
        print(self.extensions.text)
        chord = Chord(self.root.text,self.triadType.text,extensions=self.extensions.text.split(','))
        print(chord.notes)
        highlight(chord.notes)

class Main(GridLayout):
    def __init__(self,**kwargs):
        super(Main,self).__init__(**kwargs)
        self.cols=1
        self.rows=4
        self.add_widget(Label(text="title"))
        self.add_widget(GuitarScreen())
        self.add_widget(ScaleOptions())
        self.add_widget(ChordOptions())


class MyApp(App):
    #set up guitar

    def build(self):
        return Main()


if __name__ == '__main__':
    MyApp().run()
