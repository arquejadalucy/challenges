
def reduce_str_old(k, str):
    while k <= len(str):
        breakpoint()
        prev = 0
        if len(str) <= 2:
            break
        for index in range(1, len(str) - 1):
            c = 0
            if str[index] == str[prev]:
                c = 2
                for char in str[index + 1:index + k - c + 1]:
                    breakpoint()
                    if str[index] == char:
                        c += 1
                    else:
                        break
                if c == k:
                    breakpoint()
                    str = str[:prev - 1] + str[index + k - c + 1:]
                    break
            prev += 1
    return str


def reduce_str_2(k, str):
    while k <= len(str):
        breakpoint()
        prev = 0
        if len(str) <= 2:
            break
        for index in range(1, len(str) - 1):
            sub = str[prev]
            c = 0
            while c < k and c < len(str) - index:
                if str[index + c] != str[prev]:
                    break
                sub += str[index + c]
                c += 1

            if len(sub) == k:
                breakpoint()
                str = str.replace(sub, '')
                break
            prev += 1
    return str


class CharFreq:
    char: str
    freq: int

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


def reduce_str(k, str):
    char_freq_list = []
    result = ""

    for char in str:
        if not char_freq_list:
            char_freq_list.append(CharFreq(char, 1))
            continue
        top = char_freq_list[-1]
        if not char_freq_list or char != top.char:
            char_freq_list.append(CharFreq(char, 1))
        else:
            top.freq += 1
        if top.freq == k:
            char_freq_list.pop(-1)
    for char_freq in char_freq_list:
        result += char_freq.char
    return result


print(reduce_str(3, "qddxxxd"))
print(reduce_str(2, "geeksforgeeks"))
