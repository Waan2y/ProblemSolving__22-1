import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []
for _ in range(N):
  city.append(list( map(int, sys.stdin.readline().split())))   # 도시의 지도

chicken = []    # [ 치킨집 좌표들 ]
home = []       # [ 집 좌표들 ]

for i in range(N):
  for j in range(N):
    if(city[i][j] == 1):
      home.append([i, j])      # 집 좌표 저장
    elif(city[i][j] == 2):
      chicken.append([i, j])   # 치킨집 좌표 저장
    else:
      continue

city_distance = 9999                    # 최소 도시의 치킨거리값
for comb in combinations(chicken, M):   # [ 조합 내부 M 개의 치킨집 ] in [ 전체 치킨집 중에 M 개 뽑은 조합 ]
  tmp_city_distance = 0                 # 임시 도시의 치킨거리

  for tmp_home in home:                 # [ 집 좌표 ] in [ 전체 집 ]
    chicken_distance = 9999             # 치킨 거리

    for tmp_comb in comb:               # [ 치킨집 좌표 ] in [ 조합 내부 M 개의 치킨집 ]
      #                                 # 현재 집에서 현재 치킨집 사이의 치킨거리
      tmp_chicken_distance = abs(tmp_comb[0] - tmp_home[0]) + abs(tmp_comb[1] - tmp_home[1])
      ##                               ## 전체 치킨집을 순회하며 현재 집 좌표의 치킨거리 계산
      chicken_distance = min(chicken_distance, tmp_chicken_distance)

    ##                                 ## 모든 집을 순회하며 현재 조합의 도시의 치킨거리에 합산
    tmp_city_distance += chicken_distance

  ##                                   ## 최소 도시의 치킨거리인지 확인, 반영
  city_distance = min(city_distance, tmp_city_distance)

sys.stdout.write(str(city_distance))
