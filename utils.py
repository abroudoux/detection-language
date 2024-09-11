from data import languages, language_names

def find_lowest_value(dict):
    min_quotient = min(dict, key=dict.get)

    return min_quotient