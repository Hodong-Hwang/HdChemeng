import itertools
import random

# 선수 리스트
players = [1, 2, 3, 4, 5, 6, 7]  # 숫자 팀
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 영문 팀

# 선수 출전 횟수 초기화
player_games = {player: 0 for player in players}
used_pairs = set()  # 중복 페어를 저장할 집합
# 페어 조합 생성
matches = []
for _ in range(14):
    while True:
        # 리스트에서 선수 선택
        available_players = [p for p in players if player_games[p] < 4]
        if len(available_players) < 4:  # 남아 있는 선수가 4명 미만이면 종료
            print("더 이상 경기에 출전할 수 있는 선수가 없습니다.")
            break
        
        # 랜덤으로 4명 선택
        selected_players = random.sample(available_players, 4)
        selected_teams = random.sample(teams, 4)

        # 페어 구성
        pairs =[
            (selected_players[0],selected_players[1])
            (selected_teams[0], selected_teams[1])
            (selected_players[2], selected_players[3])
            (selected_teams[2], selected_teams[3])
        ]
        # 경기 추가
        matches.append((pair1, pair2, pair3, pair4))
        
        # 출전 횟수 증가
        for p in selected_players:
            player_games[p] += 1
        break

# 결과 출력
for i, match in enumerate(matches, 1):
    print(f"경기 {i}: {match[0]} vs {match[1]}, {match[2]} vs {match[3]}")

# 선수 출전 횟수 출력
print("\n선수 출전 횟수:")
for player, games in player_games.items():
    print(f"선수 {player}: {games}경기")