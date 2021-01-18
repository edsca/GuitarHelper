from guitar_string import GuitarString

class Guitar:
    # a guitar object that has some GuitarString s and some other parameters
    def __init__(self,number_of_frets,tuning,is_lefty):
        self.strings =[]
        self.is_lefty = is_lefty
        string_order = tuning.reverse()
        for note in tuning:
            self.strings.append(GuitarString(note,number_of_frets,tuning.index(note)+1))
        self.assign_fret_markers(number_of_frets)

    def on_string(self,string_number): #informal getter function for string
        return self.strings[string_number-1]

    def find_note(self,note):
        location_list = []
        for string in self.strings:
            if note in string.notes:
                location_list.append((string.string_number,string.notes.index(note)))
        return location_list


    def assign_fret_markers(self,frets):
        self.fret_markers = []
        for i in range(frets):

            if i in [12,24]:
                self.fret_markers.append("oo")
            elif i in [3,5,7,9,15,17,19,21]:
                self.fret_markers.append("o")
            elif i == 0:
                self.fret_markers.append("|")
            else:
                self.fret_markers.append(" ")
        if self.is_lefty:
            self.fret_markers = self.fret_markers[::-1]
