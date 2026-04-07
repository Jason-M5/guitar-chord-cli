CHOROMATIC_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]

MAJOR_SCALE_NOTES = []

#this returns a major scale for a key.  TODO: make it a function
def get_major_scale():
    key = input("Enter the key: ").upper()

    if key in CHOROMATIC_SCALE:
        key_index = CHOROMATIC_SCALE.index(key)

    else:
        print("Invalid key")
        exit()

    for i in MAJOR_SCALE:
        i += key_index
        MAJOR_SCALE_NOTES.append(CHOROMATIC_SCALE[i % len(CHOROMATIC_SCALE)])

    print(MAJOR_SCALE_NOTES)