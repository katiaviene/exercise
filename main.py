from collections import Counter
import sys
string = 'gogogopowerrangergogogopowerranger'
pattern = 'xxxyxxxy'


counts = dict(Counter(pattern))

def get_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] in string]

def match(liss):
    if len(counts.keys())==len(liss.keys()):
        collect_string = pattern.replace('x', liss['x']).replace('y', liss['y'])
        if collect_string == string:
            sys.exit(0)
            return liss.values()
    
list = sorted(get_all_substrings(string))
counts_sub = dict(Counter(list))

liss = {}
for sub in set(list):
    for key, value in counts.items():
        if counts_sub[sub] == counts[key]:
            liss[key]=sub
    match(liss)          
            
for x in set(list):
    for y in set(list):
        if counts_sub[x] == counts['x'] and counts_sub[y] == counts['y']:
            print(match({'x': x, 'y': y}))
            

   


    
