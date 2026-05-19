from notes import NOTES, MAJOR_SCALE, MINOR_SCALE

STANDARD_TUNING = ("E", "A", "D", "G", "B", "E")



def get_tuning():
    num_strings = input("Number of strings (default 6, blank = standard EADGBE): ").strip()
    if not num_strings:
        print("Defaulting...")
        return None

    if not num_strings.isdigit() or int(num_strings) < 1:
        print("Invalid number of strings")
        return get_tuning()

    num_strings = int(num_strings)

    print("Notes: 1=A  2=A#  3=B  4=C  5=C#  6=D  7=D#  8=E  9=F  10=F#  11=G  12=G#")

    tuning = []
    for i in range(num_strings):
        if i < len(STANDARD_TUNING):
            default_note = STANDARD_TUNING[i]
        else:
            default_note = "E"
        default = NOTES.index(default_note) + 1

        inpt = input(
            f"Enter the number associated with the string {i + 1} (default {default}): "
        ).strip()

        if not inpt:
            tuning.append(default_note)
        elif inpt.isdigit() and 1 <= int(inpt) <= len(NOTES):
            tuning.append(NOTES[int(inpt) - 1])
        else:
            print("Invalid number, using default")
            tuning.append(default_note)

    return tuple(tuning)

def get_details():

    key_raw = input("Enter the key (default F): ").strip().upper()
    if not key_raw:
        key = None
    elif key_raw not in NOTES:
        print("Invalid key")
        return get_details()
    else:
        key = key_raw

    scale_raw = input("Enter the scale, major or minor (default major): ").strip().lower()
    if not scale_raw:
        scale = None
    elif scale_raw == "major":
        scale = MAJOR_SCALE
    elif scale_raw == "minor":
        scale = MINOR_SCALE
    else:
        print("Invalid scale")
        return get_details()

    frets_raw = input("Enter the number of frets (default 22): ").strip()
    if not frets_raw:
        num_frets = None
    elif not frets_raw.isdigit() or int(frets_raw) < 1:
        print("Invalid fret count")
        num_frets = None
    else:
        num_frets = int(frets_raw)

    tuning = get_tuning()

    return key, tuning, num_frets, scale
