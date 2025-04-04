from collections import Counter

def get_match(string, pattern):
    counts = Counter(pattern)
    count_x, count_y = counts.get('x', 0), counts.get('y', 0)
  
    if count_x == 0:
        substr = string[0:int(len(string) // count_y)] 
        result =  ["", substr if string == substr * count_y else ""]
        return result if result[1] != "" else []
    if count_y == 0:
        substr = string[0:int(len(string) // count_x)] 
        result =  [substr if string == substr * count_x else "", ""] 
        return  result if result[0] != "" else []

    max_len_x = len(string) // count_x

    for len_x in range(1, max_len_x + 1):
        remaining_length = len(string) - len_x * count_x
        
        if remaining_length % count_y != 0:
            continue
        
        len_y = remaining_length // count_y
        idx = 0
        sub_x, sub_y = "", ""
        
        for char in pattern:
            if char == 'x':
                substring = string[idx:idx + len_x]
                if not sub_x:
                    sub_x = substring  
                elif sub_x != substring: 
                    break
                idx += len_x
            
            elif char == 'y':
                substring = string[idx:idx + len_y]
                if not sub_y:
                    sub_y = substring 
                elif sub_y != substring:
                    break
                idx += len_y
        else:
            return [sub_x, sub_y]

    return []


num = 10000000
string = 'go' * num + 'bu'*num
pattern = 'x' * num + 'y'* num
print(get_match(string, pattern))
