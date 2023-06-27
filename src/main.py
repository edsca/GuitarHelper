from xml.etree.ElementTree import tostring
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
from kivy.uix.screenmanager import ScreenManager, Screen

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


class ChordProgressionOptions(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=5
        self.rows=1
        self.clearProg = Button(text="Clear")
        self.clearProg.bind(on_press=self.clearProgCallback)
        self.chordPrev = Button(text="<<")
        self.chord = Label(text="CURRENT")
        self.chordNext = Button(text=">>")
        self.scroll    = Button(text="Scroll")
        self.add_widget(self.clearProg)
        self.add_widget(self.chordPrev)
        self.add_widget(self.chord)
        self.add_widget(self.chordNext)
        self.add_widget(self.scroll)
        
        
    def clearProgCallback(self,dt):
        print(self.parent.children)
        chordProg = self.parent.children[1]
        chordProg.text=""



class ChordProgressionScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chordProg = []

        self.cols=1
        self.rows=3
        self.root=Label(text='Chord Progression')
        self.progText = TextInput(text="")
        self.progOptions = ChordProgressionOptions()
        self.add_widget(self.root)
        self.add_widget(self.progText)
        self.add_widget(self.progOptions)
        


class GuitarScreen(GridLayout):
    def __init__(self,**kwargs):
        self.frets = kwargs.pop('frets')
        self.strings=kwargs.pop('strings')
        self.lefty = kwargs.pop('lefty')
        super(GuitarScreen,self).__init__(**kwargs)


        global noteButtons
        print(self.lefty)
        print(ORIENTATIONTABLE[0])
        if self.lefty==ORIENTATIONTABLE[0]:
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
        self.cols=5
        self.rows=1
        self.root = TextInput(text='Root Note')
        #self.triadType = TextInput(text='Scale Type')
        self.triadDropDown = DropDown()
        for triad in CHORDTYPETABLE:
            btn = Button(text=triad[0])
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.triadDropDown.select(btn.text))
            self.triadDropDown.add_widget(btn)
        self.triadType = Button(text='Chord')
        self.triadType.bind(on_release=self.triadDropDown.open)
        self.triadDropDown.bind(on_select=lambda instance, x: setattr(self.triadType, 'text', x))

        self.extensions = TextInput(text='')


        self.loadButton = Button(text='Show Chord')
        self.loadButton.bind(on_press=self.loadCallback)

        self.addToProgButton = Button(text='Add to Progression')
        self.addToProgButton.bind(on_press=self.addToProgression)

        self.add_widget(self.root)
        self.add_widget(self.triadType)
        self.add_widget(self.extensions)
        self.add_widget(self.loadButton)
        self.add_widget(self.addToProgButton)
        

    def loadCallback(self,dt):
        self.chord = Chord(self.root.text,self.triadType.text,extensions=self.extensions.text.split(','))
        highlight(self.chord.notes)
        progScreen = self.parent.children[3] # TODO find a better way of linking between widgets
        label = progScreen.children[2]
        label.text = self.chord.name

        
    def addToProgression(self,dt):
        self.loadCallback(dt)
        progScreen = self.parent.children[3] # TODO find a better way of linking between widgets
        chordProg= progScreen.children[1]
        chordProg.text = chordProg.text+self.chord.name+","

class Main(GridLayout):
    def __init__(self,**kwargs):
        self.frets = kwargs.pop('frets')
        self.strings=kwargs.pop('strings')
        self.lefty = kwargs.pop('lefty')
        super(Main,self).__init__(**kwargs)
        self.cols=1
        self.rows=5
        self.add_widget(Label(text="Guitar Helper Tool"))
        self.add_widget(ChordProgressionScreen())
        self.add_widget(GuitarScreen(frets=self.frets,strings=self.strings,lefty=self.lefty))
        self.add_widget(ScaleOptions())
        self.add_widget(ChordOptions())

class InitOptions(GridLayout):
    def __init__(self,**kwargs):
        super(InitOptions,self).__init__(**kwargs)
        self.cols=3
        self.rows=2
        self.add_widget(Label(text='Number of frets'))
        self.add_widget(Label(text='Tuning'))
        self.add_widget(Label(text='Orientation'))

        self.fretDropDown = DropDown()
        for scaleLength in SCALELENGTHTABLE:
            btn = Button(text=scaleLength)
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.fretDropDown.select(btn.text))
            self.fretDropDown.add_widget(btn)
        self.frets = Button(text='24')
        self.frets.bind(on_release=self.fretDropDown.open)
        self.fretDropDown.bind(on_select=lambda instance, x: setattr(self.frets, 'text', x))

        self.tuningDropDown = DropDown()
        for tuning in TUNINGTABLE:
            btn = Button(text=tuning[0])
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.tuningDropDown.select(btn.text))
            self.tuningDropDown.add_widget(btn)
        self.tunings = Button(text='Standard')
        self.tunings.bind(on_release=self.tuningDropDown.open)
        self.tuningDropDown.bind(on_select=lambda instance, x: setattr(self.tunings, 'text', x))

        self.orientationDropDown = DropDown()
        for orientation in ORIENTATIONTABLE:
            btn = Button(text=orientation)
            btn.size_hint_y = None
            btn.height = 44
            btn.bind(on_release=lambda btn: self.orientationDropDown.select(btn.text))
            self.orientationDropDown.add_widget(btn)
        self.orientations = Button(text='LEFT HANDED')
        self.orientations.bind(on_release=self.orientationDropDown.open)
        self.orientationDropDown.bind(on_select=lambda instance, x: setattr(self.orientations,'text',x))   

        self.add_widget(self.frets)
        self.add_widget(self.tunings)
        self.add_widget(self.orientations)

class Landing(GridLayout):
    def __init__(self,**kwargs):
        super(Landing,self).__init__(**kwargs)
        self.cols=1
        self.rows=3
        self.add_widget(Label(text="Landing Page"))
        self.add_widget(InitOptions())

        self.bt = Button(text='Load Screen')
        self.bt.bind(on_press=self.callback)
        self.add_widget(self.bt)

    def callback(self,dt):
        #print(int(self.children[1].children[2].text))
        #print([entry[1] for entry in TUNINGTABLE if entry[0]==self.children[1].children[1].text][0])
        try:
            print(self.children[1].children[0].text)
            frets_in = int(self.children[1].children[2].text)
            strings_in=list([entry[1] for entry in TUNINGTABLE if entry[0]==self.children[1].children[1].text][0]) #horrible code that gets tuning info
            lefty_in = self.children[1].children[0].text
           

            mn = Screen(name='Main')
            main = Main(frets=frets_in,strings=strings_in,lefty=lefty_in)
            mn.add_widget(main)
        except:
            print('error: please check whether frets and strings are correctly selected')


        self.parent.parent.add_widget(mn)
        self.parent.parent.current = 'Main'

class MyApp(App):
    #set up guitar
    sm = ScreenManager()

    ld = Screen(name='Landing')
    ld.add_widget(Landing())


    sm.add_widget(ld)


    def build(self):
        return self.sm


if __name__ == '__main__':
    MyApp().run()
