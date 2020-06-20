from common import TwelveTET as note_reference
from common import TriadTable,SeventhTable,ExtensionTable

class Chord:
    def __init__(self,root,triad_type,seventh_type, *argv):
        self.note_reference=note_reference+note_reference
        print(self.note_reference)
        self.root = root
        self.notes = []
        print(self.notes)
        self.add_triad(triad_type)
        print(self.notes)
        self.add_sevenths(seventh_type)
        print(self.notes)
        self.add_extensions(*argv)
        print(self.notes)



    def add_triad(self,triad_type):
        global TriadTable
        try:
            intervals = [entry[1] for entry in TriadTable if entry[0]==triad_type][0]
        except:
            print("error occured")
            return
        n = self.note_reference.index(self.root)
        self.notes.append(self.root)
        for interval in intervals:
            n+=interval
            self.notes.append(self.note_reference[n])

    def add_sevenths(self,seventh_type):
        global SeventhTable
        try:
            intervals = [entry[1] for entry in SeventhTable if entry[0]==seventh_type][0]
        except:
            print("error occured")
            return
        n = self.note_reference.index(self.root)
        for interval in intervals:
            n+=interval
            self.notes.append(self.note_reference[n])

    def add_extensions(self,*argv):
        global ExtensionTable
        try:
            intervals = [entry[1] for entry in ExtensionTable if entry[0] in argv]
        except:
            print("error occured")
            return

        for interval in intervals:
            n = self.note_reference.index(self.root)
            n+=interval
            self.notes.append(self.note_reference[n])

a = Chord('C','Major','M7','add9','sus4')
 #Chord (root,triad,seventh)
