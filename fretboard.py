from chords import get_major_scale
from chords import CHOROMATIC_SCALE

def make_fretboard(tuning=[
    CHOROMATIC_SCALE[7], #standard tuning...
    CHOROMATIC_SCALE[0], 
    CHOROMATIC_SCALE[5], 
    CHOROMATIC_SCALE[10], 
    CHOROMATIC_SCALE[2], 
    CHOROMATIC_SCALE[7]
    ]):
    
    fretboard = {i for i in tuning} #each string in the tuning
    major_scale = get_major_scale() #returns a list of each note in major scale
    num_frets = 22 #standard fretboard for now.  TODO: go to 12th and loop to one with a num_frets variable
    fret = "---|"
    fret_note = "-O-|"

    for string in tuning:
        
        print(f"|{string}", end="")

        if string in major_scale:
            print("|O|", end="")
        else:
            print("| |", end="")


        for f in range(num_frets):
            if CHOROMATIC_SCALE.index(string) in major_scale:
                print(fret, end="")
            else:
                print(fret_note, end="")
            
        print()    
            #print(f"|{string}| |{(fret + fret_note) * 11}")
    print(fretboard)
make_fretboard()