from notes import string_notes, notes_of_scale, MAJOR_SCALE, MINOR_SCALE


def make_fretboard(key="F", tuning=("E", "A", "D", "G", "B", "E"), num_frets=22, scale=MAJOR_SCALE):

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
        scale_notes = notes_of_scale(scale, key)
        current_fret = 0
        if string in scale_notes:
            if len(string) == 1:
                print(string, end=f" |{scale_notes.index(string) + 1}||")
            else:
                print(string, end=f"|{scale_notes.index(string) + 1}||")
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
        (" " * 4), 21,
        "\n\n"
    )
    #pprint(result, sort_dicts=False, width=120)
    return(result)
#chrds = make_fretboard()



def print_chord(chor, tuning, window, fretboard):

    n_strings = len(tuning)
    window_set = set(window)

    base = ["x"] * n_strings
    free = []

    for i, pitch in enumerate(tuning):
        
        if pitch in chor and chor[pitch]:
            base[i] = min(chor[pitch])
        else:
            free.append(i)

    rows = [base[:]]

    for i in free:
        pitch = tuning[i]
        can_open = fretboard[pitch][0] != 0
        next_rows = []
        for row in rows:
            next_rows.append(row)
            if can_open:
                open_row = row[:]
                open_row[i] = 0
                next_rows.append(open_row)
        rows = next_rows

    for simplified in rows:
        if not all(
            v == "x" or v == 0 or v in window_set for v in simplified
        ):
            continue
       

        top = []
        for v in simplified:
            if v == "x":
                top.append("x")
            elif isinstance(v, int) and v > 0:
                top.append(" ")
            else:
                top.append("O")

        def body_for_fret(fret_num):


            parts = []
            for v in simplified:
                if v == fret_num:
                    parts.append("0")
                else:
                    parts.append("|")
            return " ".join(parts)


        BOX = 5

        finger_frets = [v for v in simplified if isinstance(v, int) and v > 0]
        if finger_frets:
            lo, hi = min(finger_frets), max(finger_frets)
            span = hi - lo + 1
            if span <= BOX:
                w0_lo = max(1, hi - BOX + 1)
                w0_hi = lo
                w0 = (w0_lo + w0_hi) // 2
            else:
                mid = (lo + hi) / 2
                w0 = int(round(mid - (BOX - 1) / 2))
                upper = max(1, hi - BOX + 1)
                w0 = max(1, min(w0, upper))
        else:
            w0 = 1

        fret_rows = [w0 + i for i in range(BOX)]
        label_w = max(
            1,
            len(str(w0)),
            max(len(str(f)) for f in fret_rows),
            len("F"),
        )

        body_line = body_for_fret(w0)
        bar = "=" * len(body_line)
        print(" " * label_w + "  " + " ".join(top))
        print(str(0).ljust(label_w) + "  " + bar)

        for fret_row in fret_rows:
            print(str(fret_row).ljust(label_w) + "  " + body_for_fret(fret_row))

        print(label_w * "  " + bar)
        print()

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





def chords(fretboard, tuning=("E", "A", "D", "G", "B", "E"), intervals=[1, 3, 5]):

    num_frets = list(fretboard[tuning[0]])
    chords_result = {}
    num_chords_found = 0

    for window in iter_frets(num_frets):
        chord = {}     
        
        for fret in window:           
            for number, string in enumerate(tuning):
                if fretboard[string][fret] in intervals:
                    chord[f"{string}"] = {fret: fretboard[string][fret]}
        
        chord_check = set()

        for i in intervals:
            for stng in chord:
                for frt in chord[stng]:
                    if i == chord[stng][frt]:
                        chord_check.add(i)

        if intervals == sorted(list(chord_check)):
            
            num_chords_found += 1
            chords_result[num_chords_found] = {}
            chords_result[num_chords_found] = chord
            print_chord(chord, tuning, window, fretboard)

    return chords_result, tuning

