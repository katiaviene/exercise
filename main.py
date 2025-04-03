from collections import Counter
from itertools import product

string = 'gogogobb'
pattern = 'yyyxx'

# the order of result is always - x,y
            
def get_match(string, pattern):
    pattern_keys = ['x', 'y']
    counts_raw = dict(Counter(pattern))
    counts = {key: counts_raw[key] if key in counts_raw else 0 for key in pattern_keys}
    list_all_substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    counts_sub = dict(Counter(list_all_substrings))
    pair_match={}
    for x, y in product(set(list_all_substrings), repeat=2):
        pair_to_check = {'x': x if counts['x'] and counts_sub[x] == counts['x'] else '-',
                                 'y': y if counts['y'] and counts_sub[y] == counts['y' ] else '-'}
        collect_string = pattern.replace('x', pair_to_check['x']).replace('y', pair_to_check['y'])
        if collect_string == string:
            pair_match = pair_to_check
            break
    
    return [value.replace('-', '') for key,value in pair_match.items()] if pair_match else []


print(get_match(string, pattern))
