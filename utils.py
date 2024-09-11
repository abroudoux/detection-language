def find_lowest_value(dict):
    min_quotient = min(dict, key=dict.get)

    return min_quotient