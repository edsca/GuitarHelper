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
