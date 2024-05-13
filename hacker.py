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


def find_key_len(message: str) -> int:
    res = 1
    nod = -1
    replicas_pos = __find_replicas_pos(message)
    if (len(replicas_pos) != 0):
        nod = reduce(gcd, replicas_pos)
    return res if nod == -1 else nod


def __find_replicas_pos(message: str) -> list:
    replicas_pos = []
    sub_str_len = 3
    for i in range(len(message) - 2):
        tmp = message[i:i + sub_str_len]
        if (i + sub_str_len > len(message)):
            break
        for j in range(i + 3, len(message) - sub_str_len, sub_str_len):
            if (tmp == message[j:j + sub_str_len]):
                replicas_pos.append(j - i)

    return replicas_pos


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
                summ += (freq_table[mv_chr] - i[mv_chr])**2
            if(summ < min_s):
                min_s = summ
                m = j
        res += chr(1072+m)
    print(res)
    return res


def __get_moved_chr(c: str, move: int) -> str:
    return chr(ord(c)+move) if ord(c)+move <= ord('я') else chr(ord(c)+move-32)


def hack(message: str) -> str:
    key_len = find_key_len(message)
    loc_freq_table = __get_loc_freq_table(message, key_len)
    coder = Coder()
    return coder.decode(message, __get_key(loc_freq_table))


if __name__ == "__main__":
    print(hack("\u043f\u0434\u0435\u0432\u043d\u0441\u044e\u0448\u0441\u043d\u044e\u044c\u0445\u0430\u0431\u0443\u0442\u0440\u044f\u0431\u0431\u044a\u0449\u0432\u0440\u044d\u043d\u0442\u0447\u044d\u0448\u0448\u0431\u0445\u0442\u044b\u043c\u0435\u0443\u0430\u044e\u044a\u0446\u0445\u043b\u043e\u0434\u0443\u044e\u0444\u0449\u0442\u044e\u044d\u0430\u044b\u043b\u0436\u043b\u044a\u044b\u0438\u0446\u043a\u044d\u043e\u0441\u0438\u0440\u044f\u043f\u043d\u0437\u044b\u043d\u0441\u043d\u043c\u043b\u0435\u044c\u0438\u0441\u043f\u044c\u0449\u0442\u0442\u043d\u0445\u044a\u043a\u0448\u0442\u0447\u043d\u043f\u044d\u0438\u0432\u0430\u0445\u044f\u0446\u0441\u043c\u0443\u0441\u044f\u044b\u0440\u043e\u0441\u0449\u0432\u0440\u044a\u043d\u044a\u043c\u0445\u0430\u0437\u0442\u0446\u0434\u043c\u0440\u043a\u044b\u043b\u044c\u0442\u043b\u0446\u043e\u044a\u043d\u0447\u0447\u0444\u044c\u0442\u0440\u044d\u0435\u0444\u0447\u0449\u0433\u044e\u044c\u0443\u0446\u0445\u0443\u043d\u0445\u0445\u0446\u0437\u0448\u043f\u043d\u044e\u0449\u0448\u0434\u043f\u0445\u0441\u0432\u0430\u0437\u0431\u044a\u0449\u0447\u0445\u0449\u043d\u043f\u044c\u0449\u0442\u0442\u043d\u0445\u044a\u043a\u0448\u0442\u044a\u043d\u043f\u0430\u0444\u043b\u0437\u0440\u0448\u0443\u0433\u0436\u044e\u0441\u044f\u0442\u044d\u044f\u0448\u044a\u043e\u0444\u0441\u0435\u0447\u044c\u044c\u044f\u0442\u0444\u0440\u0430\u0446\u044e\u043f\u0430\u044b\u0436\u044d\u043f\u0447\u0430\u0431\u043e\u043a\u0445\u044d\u0434\u0438\u044c\u0447\u0440\u0440\u0431\u0449\u043c\u0438\u0445\u0449\u0432\u043a\u043d\u0438\u0446\u0442\u0442\u0447\u044a\u043b\u0441\u044e\u044e\u0447\u0430\u0442\u044d\u0432\u0432\u044b\u0441\u0439\u044c\u0449\u043a\u0430\u0445\u0444\u0434\u0448\u043b\u043d\u0440\u0448\u043d\u0434\u0442\u0445\u0438\u044c\u0442\u043a\u0434\u044b\u044d\u0430\u0432\u0445\u0446\u0434\u0442\u0432\u0435\u0431\u0447\u0448\u0440\u0442\u0448\u0444\u044e\u044d\u0441\u0442\u0430\u0443\u044e\u044e\u0447\u0440\u0440\u0431\u0440\u0438\u043d\u044f\u0435\u044a\u0447\u044f\u043e\u0430\u0449\u0435\u0438\u0442\u043a\u0431\u0433\u0441\u043a\u0434\u0448\u044d\u0440\u0440\u0443\u0435\u0434\u0436\u044c\u044f\u0442\u0435\u043d\u0436\u044a\u0449\u0432\u0440\u044a\u0442\u0430\u0446\u044d\u0435\u044a\u044e\u0447\u0447\u043f\u044c\u043b\u0448\u0447\u0440\u0440\u0431\u043f\u0435\u0449\u044e\u0447\u0444\u0442\u044d\u0435\u044b\u0439\u0442\u0430\u044b\u0446\u0443\u0437\u043d\u043e\u044f\u0435\u0444\u0435\u0443\u044b\u0439\u044d\u0442\u0448\u0430\u0430\u043d\u0437\u044f\u043a\u043f\u043b\u0448\u044a\u043a\u0433\u0448\u0449\u0431\u0439\u0442\u0442\u044a\u0439\u0443\u043e\u044d\u0445\u0446\u0431\u0448\u0446\u044c\u0447\u044b\u0437\u0442\u0445\u044c\u044f\u0445\u0441\u043d\u044f\u0448\u0441\u0434\u043b\u044f\u0443\u043a\u0442\u044f\u0440\u0442\u0445\u043b\u0447\u0447\u0440\u0440\u0440\u044f\u043a\u0430\u044a\u0440\u0442\u0448\u0434\u043a\u0433\u0444\u0443\u0431\u0433\u0441\u043a\u0434\u0447\u0440\u0432\u0447\u0448\u0435\u044e\u0435\u043d\u0430\u0445\u0449\u0430\u044e\u0447\u0449\u0442\u0440\u0447\u043d\u0447\u044b\u0443\u0441\u0432\u0442\u0441\u043d\u044d\u0441\u0435\u044e\u044f\u0442\u0430\u044b\u043a\u0442\u0431\u043c\u043f\u044c\u0445\u043b\u0441\u0431\u0430\u0446\u044a\u044b\u044d\u0435\u044c\u044b\u0439\u044f\u0448\u044b\u0430\u0447\u044b\u0437\u0430\u043d\u0449\u043a\u044e\u0441\u0435\u044a\u0445\u0443\u043e\u0444\u044a\u0443\u0432\u043a\u0442\u043e\u0442\u044b\u0438\u0430\u0432\u0443\u0444\u0430\u043e\u0440\u0430\u0444\u0448\u043e\u0432\u043d\u0443\u044f\u0442\u043f\u0435\u0449\u044e\u0447\u0444\u0442\u044d\u0435\u044b\u0439\u0442\u0430\u0447\u0440\u043f\u044e\u0441\u0439\u0442\u0438\u044d\u0441\u043f\u043f\u043c\u044d\u0448\u0447\u0443\u044e\u0441\u0442\u0442\u0444\u0449\u0438\u0435\u044c\u0445\u0442\u0444\u044d\u0438\u0437\u0442\u0446\u044c\u0448\u0440\u043f\u0430\u0445\u0441\u0447\u0447\u0440\u043d\u0448\u0442\u0439\u0430\u043c\u0449\u043b\u043c\u044a\u0443\u0449\u043a\u044d\u0440\u0433\u0441\u0442\u044a\u044c\u0440\u043b\u043c\u044a\u0443"))
