from guitar_string import GuitarString

class Guitar:
    # a guitar object that has some GuitarString s and some other parameters
    def __init__(self,number_of_frets,tuning,is_lefty):
        self.strings =[]
        self.is_lefty = is_lefty
        string_order = tuning.reverse()
        for note in tuning:
            self.strings.append(GuitarString(note,number_of_frets,tuning.index(note)+1))

    def on_string(self,string_number): #informal getter function for string
        return self.strings[string_number-1]

    def find_note(self,note):
        location_list = []
        for string in self.strings:
            if note in string.notes:
                location_list.append((string.string_number,string.notes.index(note)))
        return location_list

    def fretboard(self):
        if self.is_lefty:
            for string in self.strings:
                return string.notes[::-1] #flip board to increase pitch right to left.
        else:
            for string in self.strings:
                return string.notes
