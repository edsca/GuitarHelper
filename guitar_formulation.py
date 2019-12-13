note_reference = ['A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab']

class GuitarString:
    #A guitar String maps a position on a fretboard to a note value
    def __init__(self,tuning,number_of_frets):
        self.number_of_frets = number_of_frets
        self.tuning = tuning
        self.notes = self.tune(self.tuning)

    # function that allows you to tune/retune a string
    def tune(self,new_tuning):
        #determine the order of notes
        global note_reference
        n = note_reference.index(new_tuning)
        tuned_string = note_reference[n:] + note_reference[:n]

        #extend to fill the rest of the fretboard
        fulls,remainder = divmod(self.number_of_frets,len(note_reference))
        notes  = []
        for i in range(fulls):
            notes.extend(tuned_string)
        notes.extend(tuned_string[:remainder])
        return notes

    def fret(self,position):
        return self.notes[position]

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


if __name__ == '__main__':
    test = Guitar(number_of_frets=24,tuning=['D','A','D','G'],is_lefty=False)
    test.display_fretboard()
    print(test.on_string(4).fret(0))
