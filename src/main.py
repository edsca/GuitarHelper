from guitar import Guitar
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
        if self.lefty:
            order = -1
        else:
            order = 1

        self.guitar = Guitar(number_of_frets=self.frets,tuning=self.strings,is_lefty=self.lefty)

        self.cols=self.frets
        self.rows=len(self.strings)
        for string in self.guitar.strings:
            for note in string.notes[::order]:
                self.add_widget(Label(text=str(note[0])))




class MyApp(App):
    #set up guitar

    def build(self):
        return GuitarScreen()


if __name__ == '__main__':
    MyApp().run()
