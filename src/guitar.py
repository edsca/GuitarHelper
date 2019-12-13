from guitar_string import GuitarString

class Guitar:
    # a guitar object that has some GuitarString s and some other parameters
    def __init__(self,number_of_frets,tuning,is_lefty):
        self.strings =[]
        self.is_lefty = is_lefty
        string_order = tuning.reverse()
        for note in tuning:
            self.strings.append(GuitarString(note,number_of_frets))

    def on_string(self,string_number): #informal getter function for string
        return self.strings[string_number-1]

    def display_fretboard(self):
        if self.is_lefty:
            for string in self.strings:
                print(string.notes[::-1])
        else:
            for string in self.strings:
                print(string.notes)
