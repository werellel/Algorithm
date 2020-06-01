# 개선할 점: 모든 경우의 수에 대해서 생각해야 하며 
# 프로그램의 구조에 대한 정확한 이해가 필요하다.

def solution(n, lost, reserve):
    n -= len(lost)
    reserve_dic = {i:2 for i in reserve}
    lost_dic = {i:True for i in lost}
    for i in reversed(range(len(lost))):
        if reserve_dic.get(lost[i], None) == None:
            pass
        else:
            n += 1
            del reserve_dic[lost[i]]
            del lost[i]
            continue
    for i in lost:
        if reserve_dic.get(i+1, None) == None:
            pass
        else:
            n += 1
            reserve_dic[i+1] -= 1
            if reserve_dic[i+1] == 0:
                n -= 1
                del reserve_dic[i+1]
            continue

        if reserve_dic.get(i-1, None) == None:
            pass
        else:
            n += 1
            reserve_dic[i-1] -= 1
            if reserve_dic[i-1] == 0:
                n -= 1
                del reserve_dic[i-1]
            continue
    return n

if __name__ == '__main__':
    n = 5
    lost = [1, 2, 3]
    reserve = [1, 3, 4]

    print(solution(n, lost, reserve))