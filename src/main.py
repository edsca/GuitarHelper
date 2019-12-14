from guitar import Guitar

if __name__ == '__main__':
    test = Guitar(number_of_frets=24,tuning=[('D',2),('A',3),('D',3),('G',3)],is_lefty=False)
    test.display_fretboard()
    print(test.on_string(4).fret(0))
