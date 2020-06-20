from common import TwelveTET as note_reference
from common import ScaleTable

class Scale:
    def __init__(self,root,name):
        global note_reference
        note_reference+=note_reference
        try:
            intervals = [entry[1] for entry in ScaleTable if entry[0]==name][0]
        except:
            print("error occured")
            return
        print(intervals)
        self.name = root+name
        print(self.name)
        n = note_reference.index(root)
        print(n)


        self.notes = []
        self.notes.append(root)

        for interval in intervals:
            n+=interval
            self.notes.append(note_reference[n])
        print(self.notes)


a = Scale('C','Blues')
