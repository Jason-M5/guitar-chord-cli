from sys import exception


NOTES = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
key = input("Enter the key: ").upper()
MAJOR_SCALE = (2, 2, 1, 2, 2, 2)
MINOR_SCALE = (2, 1, 2, 2, 1, 2)



def string_notes(string, num_frets):
    # returns a list of notes for each fret following the open string.
    result = []
    start_note = NOTES.index(string)
    start_note += 1

    for i in range(num_frets):
        result.append(NOTES[(i + start_note) % len(NOTES)])
    
    return result


def notes_of_scale(scale, key):
    start = NOTES.index(key)
    result = [NOTES[start]]
    current_fret = 0
    for i in scale:
        current_fret += i
        result.append(NOTES[(start + current_fret) % len(NOTES)])
    return result


    
        



print(notes_of_scale(MINOR_SCALE, key))



