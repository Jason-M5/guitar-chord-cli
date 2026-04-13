CHOROMATIC_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
KEY = input("Enter the key: ").upper()
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]

MAJOR_SCALE_NOTES = []


def get_major_scale():


    if KEY in CHOROMATIC_SCALE:
        key_index = CHOROMATIC_SCALE.index(KEY)

    else:
        print("Invalid key")
        exit()

    for i in MAJOR_SCALE:
        i += key_index
        MAJOR_SCALE_NOTES.append(CHOROMATIC_SCALE[i % len(CHOROMATIC_SCALE)])

    return MAJOR_SCALE_NOTES

