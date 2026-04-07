from calendar import c
from chords import get_major_scale
from chords import CHOROMATIC_SCALE

def make_fretboard(tuning=[CHOROMATIC_SCALE[7], CHOROMATIC_SCALE[0], CHOROMATIC_SCALE[5], CHOROMATIC_SCALE[10], CHOROMATIC_SCALE[2], CHOROMATIC_SCALE[7]]):
    fretboard = []
    major_scale = get_major_scale()
    fret = "---|"
    fret_note = "-O-|"
    for string in tuning:
        
        print(f"|{string}| |{fret * 11 + fret_note * 11}")

make_fretboard()