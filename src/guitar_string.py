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
        n = note_reference.index(new_tuning[0])
        current_octave = new_tuning[1]
        #get to the end of the starting octave
        notes = []
        for note in note_reference[n:]:
            notes.append((note,current_octave))
        remaining_fretboard = self.number_of_frets - len(notes)

        #compute how many full octaves we can fit on the fretboard and how much 'hangs over'
        fulls,remainder = divmod(remaining_fretboard,len(note_reference))
        # for each complete octave add to our note lists
        current_octave += 1
        for i in range(fulls):
            notes.extend([(n,current_octave) for n in note_reference])
            current_octave += 1
        # add the little thing that hangs over the edge.
        notes.extend([(n,current_octave) for n in note_reference[:n]])
        return notes

    def fret(self,position):
        return self.notes[position]
