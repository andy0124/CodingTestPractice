import heapq  

def solution(n, s, a, b, fares):
    answer = 0
    #각 노드 간의 정보 그래프 
    fare_graph = dict()
    for i in range(n):
        temp = dict()
        fare_graph[i+1] = temp
            
    for inform in fares :
        fare_graph[inform[0]][inform[1]] = inform[2]
        fare_graph[inform[1]][inform[0]] = inform[2]

    #출발지 s에서 각 노드에 대한 요금표
    S_Fare = dijkstra(fare_graph, s)

    #A, B 각각의 도착지에 대한 요금 합
    answer = S_Fare[a] + S_Fare[b]

    #s를 제외한 모든 노드에서 a, b 각각의 요금 + s에서 그 노드까지의 요금 합

    for i in range(n):
        if i + 1 == s :
            continue
        i_fare = dijkstra(fare_graph, i+1)
        temp_answer = i_fare[a] + i_fare[b] + S_Fare[i+1]
        if temp_answer < answer :
            answer = temp_answer

    
    return answer



def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances


if __name__ == '__main__' :
    result = solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/72413
"""