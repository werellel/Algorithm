import heapq

def initialize():
    return [], [], 0

def solution(operations):
    operations_dic = {}
    max_q = []
    min_q = []
    d_len = 0
    for operation in operations:
        operate, number = operation.split(' ')
        number = int(number)
        if operate == 'I':
            heapq.heappush(max_q, (-number, number))
            heapq.heappush(min_q, number)
            if operations_dic.get(number, None) == None:
                operations_dic[number] = 1
            else:
                operations_dic[number] += 1

        else:
            d_len += 1
            if len(max_q) == 0 or len(min_q) == 0:
                max_q, min_q, d_len = initialize()
                continue
            if number == 1:
                pop_number = heapq.heappop(max_q)[1]
                 
            else:
                pop_number = heapq.heappop(min_q)
            operations_dic[pop_number] -= 1

            if operations_dic[pop_number] < 0:
                max_q, min_q, d_len = initialize()

        if d_len == len(max_q) + len(min_q):
            max_q, min_q, d_len = initialize()

    if len(max_q) == 0 or len(min_q) == 0:
        return [0,0]
    else:
        return [heapq.heappop(max_q)[1], heapq.heappop(min_q)]

if __name__ == '__main__':
    operations = ['I 16', 'I 6', 'I 2', 'D 1', 'D 1', 'D 1', 'D 1'] 
    print(solution(operations))