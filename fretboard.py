
import enum
from notes import string_notes, notes_of_scale, MAJOR_SCALE, key
#from pprint import pprint


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

def chords(fretboard, tuning=("E", "A", "D", "G", "B", "E")):
    current_fret = 0
    fret_span = 0 #between 0 and -3 back from current, we'll walk up and span back. making 4 fret max
    num_frets = len(fretboard[tuning[0]])
    chords = {}
    num_chords_found = 0
    print(num_frets)


    while current_fret < num_frets: #iterate over each fret

        chord = {} #temp chord dict with num_chords_found as the key, chord data as value... add to chords
        
        for string_num, string in enumerate(tuning): #go through each string
            current_string = f"{string}{string_num + 1}" #number each string to handle low and high e
            chord[current_string] = {} #add current string to the temp chord

            if fretboard[string][current_fret] in (1, 3 ,5):
                #add fretboard[string][fret] if its 1, 3 or 5. to the temp chord data
                pass
        
        print(current_fret)        
        print(chord)   
        
            #TODO: figure out chord data structure and fix above
        current_fret += 1
                
                


        


chords(chrds)