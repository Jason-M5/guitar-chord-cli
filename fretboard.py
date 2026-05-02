
import enum
from notes import string_notes, notes_of_scale, MAJOR_SCALE, key
from pprint import pprint


def make_fretboard(tuning=("E", "A", "D", "G", "B", "E"), num_frets=22):

    '''
    EXAMPLE:

    E |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    B |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    G |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    D |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    A |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    E |O|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

    '''
    result = {i: {j: None for j in range(num_frets)} for i in tuning}

    
    print()
    for string in tuning[-1::-1]:
        
        fret_notes = string_notes(string, num_frets)
        scale_notes = notes_of_scale(MAJOR_SCALE, key)
        current_fret = 0
        if string in scale_notes:
            print(string, end=f" |{scale_notes.index(string) + 1}||")
            result[string][current_fret] = scale_notes.index(string) + 1
            
        else:
            print(string, end=" |-||")
            result[string][current_fret] = 0
        
        for fret in fret_notes:

            current_fret += 1

            if fret in scale_notes:
                interval = scale_notes.index(fret) + 1
                if fret == key:
                    print(f"-{interval}-|", end="")
                    result[string][current_fret] = interval
                else:
                    print(f"-{interval}-|", end="")
                    result[string][current_fret] = interval
            else:
                print("---|", end="")
                result[string][current_fret] = 0
        print()

    print(
        "fret number:", 
        (" " * 1), 3, 
        (" " * 5), 5, 
        (" " * 5), 7, 
        (" " * 5), 9, 
        (" " * 9), 12, 
        (" " * 8), 15, 
        (" " * 4), 17, 
        (" " * 4), 19, 
        (" " * 4), 21
    )
    #pprint(result, sort_dicts=False, width=120)
    return(result)
chrds = make_fretboard()



def print_chord(chord):
    pass
#ill try it this way









def chords(fretboard, tuning=("E", "A", "D", "G", "B", "E")):
    current_fret = 0
    fret_window_start = 0
    #fret_span = 0 #between 0 and -3 back from current, we'll walk up and span back. making 4 fret max
    num_frets = list(fretboard[tuning[0]])
    chords = {}
    num_chords_found = 0
    print(num_frets)
    intervals = [1, 3, 5]
    #frm, to = 0, 0 #frets window


    for fret in num_frets:
        chord = {}    
        for window in num_frets[fret_window_start:fret]:

            for number, string in enumerate(tuning):

                if fretboard[string][fret] in intervals:
                    chord[f"{string}{number}"] = fretboard[string][fret]
            
            
            
            num_chords_found += 1
            chords[num_chords_found] = chord
            if fret - fret_window_start > 3:
                fret_window_start =+ 1
            


        #need to figure how to make a chord and ill call print_chord() here somewhere.
    pprint(chords)




            #just print the fstring if 135 in frets on each string and += frets
        


chords(chrds)