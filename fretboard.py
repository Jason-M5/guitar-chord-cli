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



def iter_frets(frets):
    result = []
    fret_window_start = 0
    for fret in frets:
    
        while fret_window_start <= fret:
            wndw = []
            for window in frets[fret_window_start:fret + 1]:

                wndw.append(window)
            
            fret_window_start += 1
            if wndw:
                result.append(wndw)
        
        if fret < 3:
            fret_window_start = 0
        else:
            fret_window_start = fret - 2
    return result #returns a list of lists that contain every fret <= 4 combo





def chords(fretboard, tuning=("E", "A", "D", "G", "B", "E")):

    num_frets = list(fretboard[tuning[0]])
    chords = {}
    num_chords_found = 0
    print(num_frets)
    intervals = [1, 3, 5]




    for window in iter_frets(num_frets):

        chord = {}       
        for fret in window:
            
            
            for number, string in enumerate(tuning):
                pass
            '''
                if fretboard[string][fret] in intervals:
                    chord[f"{string}{number}"] = fretboard[string]               
                    chord[f"{string}{number}"][window] = fretboard[string][window]
            ''' 

       


        #need to figure how to make a chord and ill call print_chord() here somewhere.
    #pprint(chords)




            #just print the fstring if 135 in frets on each string and += frets
        


chords(chrds)