import re

from collections import Counter

from data import languages, language_names
from utils import find_lowest_value

def guess_languages(s):
    frequencies = __calculate_frequencies(s)
    quotients = {}

    for lan in languages:
        quotient = __compare_frequencies(frequencies, lan)
        quotients[language_names[str(lan)]] = quotient

    lan = find_lowest_value(quotients)

    return lan

def __calculate_frequencies(s):
    s_len = len(s)
    frequencies = {}

    s_lower = s.lower()
    s_regex = re.sub('[^a-zA-Zéàèçćčâôœöôòóõ7ō]','', s_lower)
    letter_count = dict(Counter(s_regex))

    for occ in letter_count:
        freq = round((letter_count[occ] / s_len) * 100, 2)
        frequencies[occ] = freq

    return frequencies

def __compare_frequencies(dict_text, dict_language):
    quotient = 0

    for key in dict_text:
        if key in dict_language:
            quotient += abs(dict_language[key] - dict_text[key])

    return quotient