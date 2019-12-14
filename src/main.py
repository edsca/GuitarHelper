from guitar import Guitar

if __name__ == '__main__':
    test = Guitar(number_of_frets=24,tuning=[('E',3),('A',4),('D',4),('G',4),('B',5),('E',5)],is_lefty=True)
    test.display_fretboard()
    print(test.on_string(4).fret(0)) # essentially play a note
    print(test.find_note(('D',4))) # look up a note on the fretboard.
