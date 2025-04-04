from collections import Counter

def get_match(string, pattern):
    counts = Counter(pattern)
    count_x, count_y = counts.get('x', 0), counts.get('y', 0)
    max_len_x = len(string)//count_x if count_x else 0
    print(max_len_x)
    for len_x in range(0, max_len_x+1):
        print(len_x)
        remaining_length = len(string) - len_x *count_x
        len_y = remaining_length // count_y if count_y and not remaining_length % count_y else 0
        print(len_y)
        pos = 0
        sub_x, sub_y = '', ''
        for char in pattern:
            print(char)
            print(len_x)
            if char == 'x' and len_x:
                sub_x = string[pos:pos+len_x]
                print(sub_x)
                if string[pos:pos+len_x] != sub_x:
                    break 
                pos += len_x
            elif char == 'y' and len_y:
                sub_y = string[pos:pos+len_y]
                if string[pos:pos+len_y] != sub_y:
                    break  
                pos += len_y
            else:
                continue
        else:
            return [sub_x, sub_y]  # Found a match!

    return []

num = 10
string = 'go'*num
pattern = 'x'*num
print(get_match(string,pattern))
