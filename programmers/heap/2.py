import heapq

def solution(stock, dates, supplies, k):
	heap = []
	answer = 0
	index = 0
	while(stock < k):
		for i in range(index, len(dates)):
			if dates[i] <= stock:
				heapq.heappush(heap, -supplies[i])
				index = i+1
			else:
				break

		stock += abs(heapq.heappop(heap))
		answer +=1
		
	return answer

if __name__ == '__main__':
	stock = 4	
	dates = [4,10,15]	
	supplies = [20,5,10]	
	k = 30
	print(solution(stock, dates, supplies, k))