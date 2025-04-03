from collections import Counter
import sys
string = 'gogogopowerrangergogogopowerranger'
pattern = 'xxxyxxxy'
            
def get_match(string, pattern):
    counts = dict(Counter(pattern))
    list_all_subscrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i:j] in string]
    counts_sub = dict(Counter(list_all_subscrings))
    pair_match = {}
    for x in set(list_all_subscrings):
        for y in set(list_all_subscrings):
            if counts_sub[x] == counts['x'] and counts_sub[y] == counts['y']:
                pair_to_check = {'x': x, 'y': y}
                if len(counts.keys())==len(pair_to_check.keys()):
                    collect_string = pattern.replace('x', pair_to_check['x']).replace('y', pair_to_check['y'])
                    if collect_string == string:
                        pair_match = pair_to_check
    return pair_match


print(get_match(string, pattern))
