def make_fretboard(tuning=['E', 'A', 'D', 'G', 'B', 'E']):
    fret = "---|"
    for string in tuning:
        print(f"|{string}| |{fret * 22}")
    
make_fretboard()