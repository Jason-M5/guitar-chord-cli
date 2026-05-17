import fretboard
from notes import NOTES

def get_key():
    key = input("Enter the key: ").upper()
    if key not in NOTES:
        print("Invalid key")
        return get_key()
    print("\n")
    if key:
        print(f"Key of {key}")
    else:
        print("Key of F")
    return key

key = get_key()
def main():
    
    if key:
        fb = fretboard.make_fretboard(key)
    else:
        fb = fretboard.make_fretboard()
    fretboard.chords(fb)


if __name__ == "__main__":
    main()
