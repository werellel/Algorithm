import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0])
    heap = []
    time = 0
    index = 0
    answer = 0
    while True:
        if index == len(jobs) and len(heap) == 0:
            break

        for i in range(index, len(jobs)):
            if time >= jobs[i][0]:
                heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
                index = i + 1
            else:
                break
        if len(heap) == 0:
            time += 1
            pass
        else:
            pop_data = heapq.heappop(heap)
            wait_time = abs(pop_data[1] - time)
            time += pop_data[0]
            answer += pop_data[0] + wait_time

    return int(answer/len(jobs))

if __name__ == '__main__':
    jobs = [[0, 1], [7, 9], [7, 9]]
    print(solution(jobs))