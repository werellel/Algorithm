# 풀지 않는게 좋은 것 같다.
# 테스트 코드를 통과하는 코드가 아래의 예에서 잘못된 값을 반환한다.
if __name__ == '__main__':
    people = [41, 41, 41, 41, 41, 119, 119]   
    limit = 240
    print(solution(people, limit))
