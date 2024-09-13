import re

from collections import Counter

from data import languages, language_names
from utils import find_lowest_value

def guess_languages(string):
    frequencies = __calculate_frequencies(string)
    quotients = {}

    for lan in languages:
        quotient = __compare_frequencies(frequencies, lan)
        quotients[language_names[str(lan)]] = quotient

    lan = find_lowest_value(quotients)

    return lan

def __calculate_frequencies(string):
    string_len = len(string)
    frequencies = {}

    string_lower = string.lower()
    string_regex = re.sub('[^a-zA-Zàáâäãåāçćčèéêëēìíîïīñòóôõöøōùúûüūýÿœšžß]','', string_lower)
    letter_count = dict(Counter(string_regex))

    for occurence in letter_count:
        frequence = round((letter_count[occurence] / string_len) * 100, 2)
        frequencies[occurence] = frequence

    return frequencies

def __compare_frequencies(dict_text, dict_language):
    quotient = 0

    for key in dict_text:
        if key in dict_language:
            quotient += abs(dict_language[key] - dict_text[key])

    return quotient