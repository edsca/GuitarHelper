
########## PRIMATIVES #############
TwelveTET = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

SCALETABLE = [
    ("Root",[]),
    ("Major",[2,2,1,2,2,2]),
    ("Blues",[3,2,1,1,3]),
    ("Natural Minor", [2,1,2,2,1,2]),
    ("Minor Pentatonic", [3,2,2,3])
]

TRIADTABLE = [
    ("Major", [4,3]),
    ("Augmented",[4,4]),
    ("Minor",[3,4]),
    ("Diminished",[3,3]),
    ("Suspended 4", [5,2]),
    ("Suspended 2", [2,5])
]

EXTENSIONTABLE = [
    ("b9",1),
    ("9", 2),
    ("m",3),
    ("M",4),
    ("11",5),
    ("#11",6),
    ("b5",6),
    ("#5",8),
    ("b6",8),
    ("b13",8),
    ("6",9),
    ("13",9),
    ("dim7",9),
    ("7", 10),
    ("M7", 11)
]


#############   Classes     ############
class Chord:
    def __init__(self,root,triad_type, **kwargs):
        global TwelveTET
        self.TwelveTET=TwelveTET+TwelveTET
        self.root = root
        self.notes = []
        self.add_triad(triad_type)

        for key, value in kwargs.items():
            if key=='extensions':
                self.add_extensions(value)



        print(self.notes)

    def add_triad(self,triad_type):
        global TRIADTABLE
        try:
            intervals = [entry[1] for entry in TRIADTABLE if entry[0]==triad_type][0]
        except:
            print("error occured")
            intervals = []
        n = self.TwelveTET.index(self.root)
        self.notes.append(self.root)
        for interval in intervals:
            n+=interval
            self.notes.append(self.TwelveTET[n])

    def add_extensions(self,extensions):
        global EXTENSIONTABLE

        try:
            intervals = [entry[1] for entry in EXTENSIONTABLE if entry[0] in extensions]
        except:
            print("error occured")
            intervals = []
        print(extensions)
        print(intervals)
        for interval in intervals:
            n = self.TwelveTET.index(self.root)
            n+=interval
            self.notes.append(self.TwelveTET[n])

class Scale:
    def __init__(self,root,name):
        global TwelveTET
        TwelveTET+=TwelveTET
        try:
            intervals = [entry[1] for entry in SCALETABLE if entry[0]==name][0]
        except:
            print("error occured")
            return

        self.name = root+name

        n = TwelveTET.index(root)



        self.notes = []
        self.notes.append(root)

        for interval in intervals:
            n+=interval
            self.notes.append(TwelveTET[n])
