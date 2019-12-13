from guitar import Guitar

if __name__ == '__main__':
    test = Guitar(number_of_frets=24,tuning=['D','A','D','G'],is_lefty=False)
    test.display_fretboard()
    print(test.on_string(4).fret(0))
