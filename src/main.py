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

noteButtons = []
def highlight(notes):
    global noteButtons

    nums  = [(i+1)/len(notes) for i in range(len(notes))]

    for nB in noteButtons:
        colour = 0
        nB.color=[1,1,1,0.1]
        for i in range(len(notes)):
            if notes[i] == nB.text:
                nB.color = [1-nums[i],0.5,1,0.5*(1+nums[i])]


class GuitarScreen(GridLayout):
    def __init__(self,**kwargs):
        super(GuitarScreen,self).__init__(**kwargs)

        self.frets = 24
        self.strings=[('E',3),('A',4),('D',4),('G',4),('B',5),('E',5)]
        self.lefty = True
        global noteButtons
        if self.lefty:
            order = -1
        else:
            order = 1

        self.guitar = Guitar(number_of_frets=self.frets,tuning=self.strings,is_lefty=self.lefty)
        self.cols=self.frets
        self.rows=len(self.strings)+2
        for string in self.guitar.strings:
            for note in string.notes[::order]:
                a = Button(text=str(note[0]))
                a.bind(on_press=self.callback)
                noteButtons.append(a)
                self.add_widget(a)

        for i in range(self.frets)[::order]:
            self.add_widget(Label(text=str(i)))
        for fret_marker in self.guitar.fret_markers:
            self.add_widget(Label(text=str(fret_marker)))

    def callback(self,dt):
        scale = Scale(dt.text,'Root')
        highlight(scale.notes)
        self.parent.children[0].root.text = dt.text
        self.parent.children[1].root.text = dt.text




class ScaleOptions(GridLayout):
    def __init__(self,**kwargs):
        super(ScaleOptions,self).__init__(**kwargs)
        self.cols=3
        self.rows=1
        self.root = TextInput(text='Root Note')

        #self.scaleType = TextInput(text='Scale Type')

        self.scaleDropDown = DropDown()
        for scale in SCALETABLE:
            btn = Button(text=scale[0])
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.scaleDropDown.select(btn.text))
            self.scaleDropDown.add_widget(btn)
        self.scaleType = Button(text='Scale Type')
        self.scaleType.bind(on_release=self.scaleDropDown.open)
        self.scaleDropDown.bind(on_select=lambda instance, x: setattr(self.scaleType, 'text', x))

        self.loadButton = Button(text='Show Scale')

        self.loadButton.bind(on_press=self.callback)
        self.add_widget(self.root)
        self.add_widget(self.scaleType)
        self.add_widget(self.loadButton)

    def callback(self,dt):

        scale = Scale(self.root.text,self.scaleType.text)
        highlight(scale.notes)

class ChordOptions(GridLayout):
    def __init__(self,**kwargs):
        super(ChordOptions,self).__init__(**kwargs)
        self.cols=4
        self.rows=1
        self.root = TextInput(text='Root Note')
        #self.triadType = TextInput(text='Scale Type')
        self.triadDropDown = DropDown()
        for triad in TRIADTABLE:
            btn = Button(text=triad[0])
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.triadDropDown.select(btn.text))
            self.triadDropDown.add_widget(btn)
        self.triadType = Button(text='Chord')
        self.triadType.bind(on_release=self.triadDropDown.open)
        self.triadDropDown.bind(on_select=lambda instance, x: setattr(self.triadType, 'text', x))

        self.extensions = TextInput(text='Extensions')


        self.loadButton = Button(text='Show Chord')

        self.loadButton.bind(on_press=self.callback)
        self.add_widget(self.root)
        self.add_widget(self.triadType)
        self.add_widget(self.extensions)
        self.add_widget(self.loadButton)

    def callback(self,dt):

        chord = Chord(self.root.text,self.triadType.text,extensions=self.extensions.text.split(','))

        highlight(chord.notes)

class Main(GridLayout):
    def __init__(self,**kwargs):
        super(Main,self).__init__(**kwargs)
        self.cols=1
        self.rows=4
        self.add_widget(Label(text="Guitar Helper Tool"))
        self.add_widget(GuitarScreen())
        self.add_widget(ScaleOptions())
        self.add_widget(ChordOptions())


class MyApp(App):
    #set up guitar

    def build(self):
        return Main()


if __name__ == '__main__':
    MyApp().run()
