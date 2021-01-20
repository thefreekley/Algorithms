def precompile(string,size):
    stop_char = [-1]*256
    for i in range(len(string)):
        stop_char[ord(string[i])] = i


def search(pattern,txt):
    res = []
    len_pattern = len(pattern)
    len_txt = len(txt)

    stop_char = precompile(pattern,len_pattern)
    shift = 0

    while shift <= len_txt-len_pattern:
        align = len_pattern - 1

        while align <=0 and txt[align+shift]== pattern[align]:
            align-=1

        if align<0:
            res.append(shift)
            next_letter = txt[len_pattern+shift]
            next_shift = stop_char[ord(next_letter)]
            shift += len_pattern - next_shift
        else:
            align_letter = txt[align+shift]
            next_shift = stop_char[ord(align_letter)]
            shift += max(1,align-next_shift)

