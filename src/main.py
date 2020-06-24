from guitar import Guitar
from common import *

import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class GuitarScreen(GridLayout):
    def __init__(self,**kwargs):
        super(GuitarScreen,self).__init__(**kwargs)

        self.frets = 24
        self.strings=[('E',3),('A',4),('D',4),('G',4),('B',5),('E',5)]
        self.lefty = True
        self.widgets = []
        if self.lefty:
            order = -1
        else:
            order = 1

        self.guitar = Guitar(number_of_frets=self.frets,tuning=self.strings,is_lefty=self.lefty)
        self.cols=self.frets
        self.rows=len(self.strings)+2
        for i in range(self.frets)[::order]:
            self.add_widget(Label(text=str(i)))
        for string in self.guitar.strings:
            for note in string.notes[::order]:
                a = Label(text=str(note[0]))
                self.widgets.append(a)
                self.add_widget(a)

        for fret_marker in self.guitar.fret_markers:
            self.add_widget(Label(text=str(fret_marker)))
        scale = Scale('C','Major').notes
        chord = Chord('C','Major', 'M7').notes
        print(filter)
        self.highlight(chord)

    def highlight(self,notes):
        for w in self.widgets:
            if w.text in notes:
                w.color = [1,0,1,1]

class Options(GridLayout):
    def __init__(self,**kwargs):
        super(Options,self).__init__(**kwargs)
        self.cols=2
        self.rows=1
        self.add_widget(Label(text="123"))
        self.add_widget(Label(text="test"))

class Main(GridLayout):
    def __init__(self,**kwargs):
        super(Main,self).__init__(**kwargs)
        self.cols=1
        self.rows=3
        self.add_widget(Label(text="title"))
        self.add_widget(GuitarScreen())
        self.add_widget(Options())


class MyApp(App):
    #set up guitar

    def build(self):
        return Main()


if __name__ == '__main__':
    MyApp().run()
