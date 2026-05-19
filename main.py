import fretboard
from details import get_details


def main():
    key, tuning, num_frets, scale = get_details()

    kwargs = {}
    if key is not None:
        kwargs["key"] = key
    if tuning is not None:
        kwargs["tuning"] = list(tuning)
    if num_frets is not None:
        kwargs["num_frets"] = num_frets
    if scale is not None:
        kwargs["scale"] = scale

    fb = fretboard.make_fretboard(**kwargs)
    tuning_for_chords = tuning if tuning is not None else ("E", "A", "D", "G", "B", "E")
    fretboard.chords(fb, tuning=tuning_for_chords)


if __name__ == "__main__":
    main()