class BoyesMooreSubstring:
    def __init__(self, string):
        self.string = string
        self.alphabet = 256

    def precompile(self, sting, size):
        bad_char = [-1] * self.alphabet
        for i in range(size):
            bad_char[ord(sting[i])] = i
        return bad_char

    def search(self, pattern):
        result = []
        len_pattern = len(pattern)
        len_txt = len(self.string)
        bad_char = self.precompile(pattern, len_pattern)
        shift = 0
        count_res = 0
        while shift <= (len_txt - len_pattern):
            align = len_pattern - 1

            while align >= 0 and pattern[align] == self.string[shift + align]:
                align -= 1

            if align < 0:
                result.append(shift)
                count_res += 1
                if (shift + len_pattern) >= len_txt: break
                next_letter = self.string[shift + len_pattern]
                next_shift = bad_char[ord(next_letter)]
                shift += len_pattern - next_shift
            else:
                if (shift + align) >= len_txt: break
                align_letter = self.string[shift + align]
                next_shift = bad_char[ord(align_letter)]
                shift += max(1, align - next_shift)

        return result

# O(len_txt + len_patter + alphabet)
