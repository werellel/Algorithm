# 문제를 명확히 이해해야 한다.
from string import ascii_uppercase
alpha_list = list(ascii_uppercase)

def direction(name):
    reverse_index = 0
    forward_index = 0
    for index, i in enumerate(name[1:]):
        if i != 'A':
            reverse_index = index + 1
            break    
    for index, i in enumerate(reversed(name[1:])):
        if i != 'A':
            forward_index = index + 1
            break
    if forward_index > reverse_index:
        return forward_index
    else:
        return reverse_index

def count_alphabet_change(target):
    for index in range(len(alpha_list)):
        up = index + 1
        down = len(alpha_list) - (index + 1)
        if target == alpha_list[up]:
            return index + 1
        if target == alpha_list[down]:
            return index + 1

def return_value(down, start_name, name):
    count = count_alphabet_change(name[down])
    start_name = start_name[:down] + name[down] + start_name[down+1:]
    start_name = start_name[down:] + start_name[:down]
    name = name[down:] + name[:down]
    return count, start_name, name

def change(start_name, name):
    count = 0
    up = 0
    down = 0
    for index in range(0, len(name)):
        up = index
        if index == 0:
            down == 0
        else:
            down = len(name) - index 
        if name[down] != start_name[down] and name[up] != start_name[up]:
            down__index = direction(name[down:] + name[:down])
            up__index = direction(name[up:] + name[:up])
            if down__index > up__index:
                count, start_name, name = return_value(down, start_name, name)
                return count+index, start_name, name
            else:
                count, start_name, name = return_value(up,start_name, name)
                return count+index, start_name, name
                
        if name[up] != start_name[up]:
            count, start_name, name = return_value(up,start_name, name)
            return count+index, start_name, name
        if name[down] != start_name[down]:
            count, start_name, name = return_value(down, start_name, name)
            return count+index, start_name, name

def solution(name):
    start_name = 'A'*len(name)
    count = 0
    while start_name != name:
        temp_count, start_name, name = change(start_name, name)
        count += temp_count

    return count

if __name__ == '__main__':
    name = 'JAN'    
    print(solution(name))