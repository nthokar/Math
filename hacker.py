from math import gcd
from functools import reduce
from collections import Counter
from typing import List
from Coder import Coder

freq_table = {
    'а': 0.0801, 'б': 0.0159,
    'в': 0.0454, 'г': 0.017,
    'д': 0.0298, 'е': 0.0845,
    'ж': 0.0094, 'з': 0.0165,
    'и': 0.0735, 'й': 0.0121,
    'к': 0.0349, 'л': 0.044,
    'м': 0.0321, 'н': 0.067,
    'о': 0.1097, 'п': 0.0281,
    'р': 0.0473, 'с': 0.0547,
    'т': 0.0626, 'у': 0.0262,
    'ф': 0.0026, 'х': 0.0097,
    'ц': 0.0048, 'ч': 0.0144,
    'ш': 0.0073, 'щ': 0.0036,
    'ъ': 0.0004, 'ы': 0.019,
    'ь': 0.0174, 'э': 0.0032,
    'ю': 0.0064, 'я': 0.0201
}

def __find_key_len(message: str, replicas_pos: dict) -> int:
    nod = -1
    ranges = _find_ranges(replicas_pos)
    if (len(ranges) != 0):
        nod = reduce(gcd, ranges)
    return nod

def _find_key_len(message: str, sub_str_len:int) -> int:
    replicas_pos = find_replicas_pos(message, sub_str_len)
    return __find_key_len(message, replicas_pos)


def find_key_len(message: str) -> int:
    tries = []
    for i in range(2, len(message)):
        nod = _find_key_len(message, i)
        if nod > 1:
            return nod
        if nod == 1:
            tries.append(i)
    print(tries)
    return _xd(message, tries)

def _xd(message: str, sub_str_len_tries: int) -> int:
    min = float('inf')
    for i in sub_str_len_tries:
        replicas = find_replicas_pos(message, i)
        keys = list(replicas.keys())
        j = 2**(len(keys))
        while 0b0 < j:
            j -= 0b1
            j_str = str(bin(j))[2::]
            replicas_tmp = {}
            for k in range(len(j_str)):
                k_ch = j_str[k]
                if k_ch == '1':
                    replicas_tmp.update({keys[k]: replicas[keys[k]]})
            nod = __find_key_len(message, replicas_tmp)
            if nod > 1 and min > nod:
                min = nod
                print(nod)


    return min

def find_replicas_pos(message: str, sub_str_len: int) -> dict:
    replicas_pos = {}
    for i in range(0, len(message) - sub_str_len):
        repeat = message[i:i + sub_str_len]
        count = 1
        if not replicas_pos.keys().__contains__(repeat):
            for j in range(i, len(message) - sub_str_len):
                repeat_2 = message[j:j + sub_str_len]
                if repeat_2 == repeat:
                    count += 1
                    if count > 3:
                        replicas_pos[repeat].append(j)
                    elif count > 2:
                        replicas_pos.update({repeat: [i, j]})

    return replicas_pos
def __find_ranges(ls: list):
    ranges = []
    for i in range(1, len(ls), 2):
        _range = ls[i] - ls[i - 1]
        ranges.append(_range)
    return ranges

5^13
def _find_ranges(dct: dict):
    ranges = []
    for key in dct.keys():
        ranges_tmp = __find_ranges(dct[key])
        for item in ranges_tmp:
            ranges.append(item)
    return ranges


def __get_loc_freq_table(message: str, key_len: int) -> List[dict]:
    chars = [[] for i in range(key_len)]
    loc_freq_table = [dict(zip([chr(i) for i in range(ord('а'), ord('я')+1)], [0 for _ in range((ord('я')-ord('а'))+1)]))
                      for _ in range(key_len)]

    for i in range(key_len):
        for j in range((len(message)//key_len)+1):
            if(i+j*key_len>=len(message)):
                break
            chars[i].append(message[i+j*key_len])

    for i in range(key_len):
        gg = Counter(chars[i])
        for c in gg.items():
            loc_freq_table[i][c[0]] = c[1]/(len(chars[i]))

    return loc_freq_table


def __get_key(loc_freq_table: List[dict]) -> str:
    res = ''
    for i in loc_freq_table:
        min_s = 999999
        m = 0
        for j in range(32):
            summ = 0
            for h in i.items():
                mv_chr = __get_moved_chr(h[0], j)
                summ += (freq_table[h[0]] - i[mv_chr])**2
            if(summ < min_s):
                min_s = summ
                m = j
        res += chr(1072+m)
    print(res)
    return res

def __get_key_2(loc_freq_table: List[dict]) -> List[tuple]:
    res = ''
    count = 3
    ls_full = []
    for i_1 in range(len(loc_freq_table)):
        i = loc_freq_table[i_1]
        ls_ch = []
        for j in range(32):
            summ = 0
            for h in i.items():
                mv_chr = __get_moved_chr(h[0], j)
                summ += (freq_table[h[0]] - i[mv_chr])**2
            ls_ch.append((chr(1072+j), summ))
        ls_ch = sorted(ls_ch, key=lambda x: x[1])
        ls_ch = ls_ch[:count]
        ls_full.append(ls_ch)
    print(res)
    plain_list = []
    # for i in range(len(ls_full)):
    #     for j in range(len(i)):
    #         plain_list.append()
    fullly = ttt(ls_full, 0)
    fullly = sorted(fullly, key=lambda x: x[1])
    return fullly[:count]


def ttt(table: List[dict], depth: int) -> List[tuple]:
    result = []
    if depth >= len(table):
        return [('', 0)]
    place = table[depth]
    for letter in place:
        sub = ttt(table, depth+1)
        for sub_word in sub:
            result.append((letter[0] + sub_word[0], sub_word[1] + letter[1]))
    return result

def __get_moved_chr(c: str, move: int) -> str:
    return chr(ord(c)+move) if ord(c)+move <= ord('я') else chr(ord(c)+move-32)


def hack(message: str) -> str:
    key_len = find_key_len(message)
    loc_freq_table = __get_loc_freq_table(message, key_len)
    coder = Coder()
    return coder.decode(message, __get_key(loc_freq_table))

def hack_key(message: str) -> List[tuple]:
    key_len = find_key_len(message)
    loc_freq_table = __get_loc_freq_table(message, key_len)
    coder = Coder()
    return __get_key_2(loc_freq_table)


if __name__ == "__main__":
    print(hack("\u043f\u0434\u0435\u0432\u043d\u0441\u044e\u0448\u0441\u043d\u044e\u044c\u0445\u0430\u0431\u0443\u0442\u0440\u044f\u0431\u0431\u044a\u0449\u0432\u0440\u044d\u043d\u0442\u0447\u044d\u0448\u0448\u0431\u0445\u0442\u044b\u043c\u0435\u0443\u0430\u044e\u044a\u0446\u0445\u043b\u043e\u0434\u0443\u044e\u0444\u0449\u0442\u044e\u044d\u0430\u044b\u043b\u0436\u043b\u044a\u044b\u0438\u0446\u043a\u044d\u043e\u0441\u0438\u0440\u044f\u043f\u043d\u0437\u044b\u043d\u0441\u043d\u043c\u043b\u0435\u044c\u0438\u0441\u043f\u044c\u0449\u0442\u0442\u043d\u0445\u044a\u043a\u0448\u0442\u0447\u043d\u043f\u044d\u0438\u0432\u0430\u0445\u044f\u0446\u0441\u043c\u0443\u0441\u044f\u044b\u0440\u043e\u0441\u0449\u0432\u0440\u044a\u043d\u044a\u043c\u0445\u0430\u0437\u0442\u0446\u0434\u043c\u0440\u043a\u044b\u043b\u044c\u0442\u043b\u0446\u043e\u044a\u043d\u0447\u0447\u0444\u044c\u0442\u0440\u044d\u0435\u0444\u0447\u0449\u0433\u044e\u044c\u0443\u0446\u0445\u0443\u043d\u0445\u0445\u0446\u0437\u0448\u043f\u043d\u044e\u0449\u0448\u0434\u043f\u0445\u0441\u0432\u0430\u0437\u0431\u044a\u0449\u0447\u0445\u0449\u043d\u043f\u044c\u0449\u0442\u0442\u043d\u0445\u044a\u043a\u0448\u0442\u044a\u043d\u043f\u0430\u0444\u043b\u0437\u0440\u0448\u0443\u0433\u0436\u044e\u0441\u044f\u0442\u044d\u044f\u0448\u044a\u043e\u0444\u0441\u0435\u0447\u044c\u044c\u044f\u0442\u0444\u0440\u0430\u0446\u044e\u043f\u0430\u044b\u0436\u044d\u043f\u0447\u0430\u0431\u043e\u043a\u0445\u044d\u0434\u0438\u044c\u0447\u0440\u0440\u0431\u0449\u043c\u0438\u0445\u0449\u0432\u043a\u043d\u0438\u0446\u0442\u0442\u0447\u044a\u043b\u0441\u044e\u044e\u0447\u0430\u0442\u044d\u0432\u0432\u044b\u0441\u0439\u044c\u0449\u043a\u0430\u0445\u0444\u0434\u0448\u043b\u043d\u0440\u0448\u043d\u0434\u0442\u0445\u0438\u044c\u0442\u043a\u0434\u044b\u044d\u0430\u0432\u0445\u0446\u0434\u0442\u0432\u0435\u0431\u0447\u0448\u0440\u0442\u0448\u0444\u044e\u044d\u0441\u0442\u0430\u0443\u044e\u044e\u0447\u0440\u0440\u0431\u0440\u0438\u043d\u044f\u0435\u044a\u0447\u044f\u043e\u0430\u0449\u0435\u0438\u0442\u043a\u0431\u0433\u0441\u043a\u0434\u0448\u044d\u0440\u0440\u0443\u0435\u0434\u0436\u044c\u044f\u0442\u0435\u043d\u0436\u044a\u0449\u0432\u0440\u044a\u0442\u0430\u0446\u044d\u0435\u044a\u044e\u0447\u0447\u043f\u044c\u043b\u0448\u0447\u0440\u0440\u0431\u043f\u0435\u0449\u044e\u0447\u0444\u0442\u044d\u0435\u044b\u0439\u0442\u0430\u044b\u0446\u0443\u0437\u043d\u043e\u044f\u0435\u0444\u0435\u0443\u044b\u0439\u044d\u0442\u0448\u0430\u0430\u043d\u0437\u044f\u043a\u043f\u043b\u0448\u044a\u043a\u0433\u0448\u0449\u0431\u0439\u0442\u0442\u044a\u0439\u0443\u043e\u044d\u0445\u0446\u0431\u0448\u0446\u044c\u0447\u044b\u0437\u0442\u0445\u044c\u044f\u0445\u0441\u043d\u044f\u0448\u0441\u0434\u043b\u044f\u0443\u043a\u0442\u044f\u0440\u0442\u0445\u043b\u0447\u0447\u0440\u0440\u0440\u044f\u043a\u0430\u044a\u0440\u0442\u0448\u0434\u043a\u0433\u0444\u0443\u0431\u0433\u0441\u043a\u0434\u0447\u0440\u0432\u0447\u0448\u0435\u044e\u0435\u043d\u0430\u0445\u0449\u0430\u044e\u0447\u0449\u0442\u0440\u0447\u043d\u0447\u044b\u0443\u0441\u0432\u0442\u0441\u043d\u044d\u0441\u0435\u044e\u044f\u0442\u0430\u044b\u043a\u0442\u0431\u043c\u043f\u044c\u0445\u043b\u0441\u0431\u0430\u0446\u044a\u044b\u044d\u0435\u044c\u044b\u0439\u044f\u0448\u044b\u0430\u0447\u044b\u0437\u0430\u043d\u0449\u043a\u044e\u0441\u0435\u044a\u0445\u0443\u043e\u0444\u044a\u0443\u0432\u043a\u0442\u043e\u0442\u044b\u0438\u0430\u0432\u0443\u0444\u0430\u043e\u0440\u0430\u0444\u0448\u043e\u0432\u043d\u0443\u044f\u0442\u043f\u0435\u0449\u044e\u0447\u0444\u0442\u044d\u0435\u044b\u0439\u0442\u0430\u0447\u0440\u043f\u044e\u0441\u0439\u0442\u0438\u044d\u0441\u043f\u043f\u043c\u044d\u0448\u0447\u0443\u044e\u0441\u0442\u0442\u0444\u0449\u0438\u0435\u044c\u0445\u0442\u0444\u044d\u0438\u0437\u0442\u0446\u044c\u0448\u0440\u043f\u0430\u0445\u0441\u0447\u0447\u0440\u043d\u0448\u0442\u0439\u0430\u043c\u0449\u043b\u043c\u044a\u0443\u0449\u043a\u044d\u0440\u0433\u0441\u0442\u044a\u044c\u0440\u043b\u043c\u044a\u0443"))
