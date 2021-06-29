def get_moves(char):

  # 알파벳 O부터 Z까지 커서 최소 이동횟수
  if ord(char) > ord('N'):
    return 26 - ord(char) % 65
  # 알파벳 A부터 N까지 커서 최소 이동횟수
  else:
    return ord(char) % 65

def solution(name):
  answer = 0

  init_string = ['A'] * len(name)

  incorrect_char_idx = list()
  # 각 문자마다 변경하는데 드는 최솟값
  # 위 아래 커서이동은 좌우 움직임과 무관함
  for input_char_and_idx, correct_char in zip(enumerate(name), init_string):
    input_char, idx = list(input_char_and_idx)[1], list(input_char_and_idx)[0]
    if input_char != correct_char:
      answer += get_moves(input_char)
      incorrect_char_idx.append(idx)

  if len(incorrect_char_idx) != 0:
    # 초기 커서는 맨 왼쪽
    current_pos = 0
    while len(incorrect_char_idx) != 0:
      distance_list = list()
      # 수정해야할 알파벳의 위치
      for idx in incorrect_char_idx:
        # 왼쪽 1번 --- 고쳐야할 위치 ----- 현재 위치 라면 ---- 끝위치
        # 커서는 왼쪽으로 이동할수밖에 없음
        # 오른쪽끝에서 왼쪽 1번으로 갈수는 없음 ( 중요 조건)
        if idx <= current_pos:
          distance_list.append(current_pos - idx)

        # 왼쪽 1번 --- 현재위치 ----- 고쳐야할 위치 ---- 끝 위치 라면
        # 두가지 방법이 있음
        # -> 이렇게 가서 찾거나
        # <- 이렇게 가서 왼쪽 1번에서 끝 위치로 가거나
        # 두 방법 중 짧은것을 택해야함
        elif idx > current_pos:
          distance_list.append(
              min((current_pos - idx) % len(name), idx - current_pos))

      # 가장 짧게 움직이는것
      min_move = min(distance_list)
      # 다음 조이스틱의 위치
      next_index = incorrect_char_idx[distance_list.index(min_move)]

      answer += min_move
      # 현재 커서를 가장 거리가 가까운 곳으로 옮김
      current_pos = next_index

      incorrect_char_idx.remove(next_index)

  return answer
