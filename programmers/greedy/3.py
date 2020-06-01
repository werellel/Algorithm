# 개선할 부분: 코딩할 때 변수들(max_index, max_value)에 대한 
# 단위 테스트 혹은 변수의 값이 어떻게 흘러가는지 관리해야 한다. 
# 외 상황에 대한 정확한 확인이 필요하다. 

def solution(number, k):
    answer = ''
    n = len(number) - k

    for i in range(n, 0, -1):
        max_index = 0
        max_value = 0
        for index, j in enumerate(number[:len(number) - i+1]):
            if int(j) > max_value:
                max_value = int(j)
                max_index = index
                if max_value == 9:
                    break
        answer = answer + number[max_index]
        number = number[max_index+1:]
    return answer

if __name__ == '__main__':
    number = '10000'
    k = 2
    print(solution(number, k))
