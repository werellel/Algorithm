triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

def solution(triangle):
    last_calculated = [triangle[0][0]]
    for idx, i in enumerate(triangle[1:]):
        tmp_cal = []
        for jdx, j in enumerate(i):
            max_list = last_calculated[max(0, jdx-1):jdx+1]
            max_list.append(0)
            tmp_cal.append(j + max(max_list))
        last_calculated = tmp_cal
    return max(last_calculated)
 
if __name__ == '__main__':
    print(solution(triangle))
