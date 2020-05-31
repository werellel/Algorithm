import heapq

def cal_scoville(first, second):
	return first + (second * 2)

def solution(scoville, K):
	heap = []
	for i in scoville:
		heapq.heappush(heap, i)
	
	answer = 0
	while len(heap) > 1:	
		first = heapq.heappop(heap)
		second = heapq.heappop(heap)
		if first >= K:
			break
		heapq.heappush(heap, cal_scoville(first, second))
		answer += 1
	
	if len(heap) >= 1:
		first = heapq.heappop(heap)
		if first < K:
			answer = -1

	return answer



if __name__ == '__main__':
	scoville = [1, 12]
	K = 2
	print(solution(scoville, K))